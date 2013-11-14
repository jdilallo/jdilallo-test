#!/usr/bin/python
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example gets the account hierarchy under the current account.

Note: this code example won't work with test accounts. See
https://developers.google.com/adwords/api/docs/test-accounts

Tags: ServicedAccountService.get
Api: AdWordsOnly
"""

__author__ = 'api.kwinter@gmail.com (Kevin Winter)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import AdWordsClient


def DisplayAccountTree(account, link, accounts, links, depth=0):
  """Displays an account tree.

  Args:
    account: dict The account to display.
    link: dict The link used to reach this account.
    accounts: dict Map from customerId to account.
    links: dict Map from customerId to child links.
    depth: int Depth of the current account in the tree.
  """
  prefix = '-' * depth * 2
  print '%s%s, %s, %s' % (prefix, account['login'], account['customerId'],
                          account['name'])
  if account['customerId'] in links:
    for child_link in links[account['customerId']]:
      child_account = accounts[child_link['clientCustomerId']]
      DisplayAccountTree(child_account, child_link, accounts, links, depth + 1)


def main(client):
  # Initialize appropriate service.
  managed_customer_service = client.GetManagedCustomerService(version='v201306')

  # Construct selector to get all accounts.
  selector = {
      'fields': ['Login', 'CustomerId', 'Name']
  }
  # Get serviced account graph.
  graph = managed_customer_service.Get(selector)[0]
  if 'entries' in graph and graph['entries']:
    # Create map from customerId to parent and child links.
    child_links = {}
    parent_links = {}
    if 'links' in graph:
      for link in graph['links']:
        if link['managerCustomerId'] not in child_links:
          child_links[link['managerCustomerId']] = []
        child_links[link['managerCustomerId']].append(link)
        if link['clientCustomerId'] not in parent_links:
          parent_links[link['clientCustomerId']] = []
        parent_links[link['clientCustomerId']].append(link)
    # Create map from customerID to account and find root account.
    accounts = {}
    root_account = None
    for account in graph['entries']:
      accounts[account['customerId']] = account
      if account['customerId'] not in parent_links:
        root_account = account
    # Display account tree.
    if root_account:
      print 'Login, CustomerId, Name'
      DisplayAccountTree(root_account, None, accounts, child_links, 0)
    else:
      print 'Unable to determine a root account'
  else:
    print 'No serviced accounts were found'

  print
  print ('Usage: %s units, %s operations' % (client.GetUnits(),
                                             client.GetOperations()))


if __name__ == '__main__':
  # Initialize client object.
  client = AdWordsClient(path=os.path.join('..', '..', '..', '..', '..'))
  client.use_mcc = True

  main(client)
