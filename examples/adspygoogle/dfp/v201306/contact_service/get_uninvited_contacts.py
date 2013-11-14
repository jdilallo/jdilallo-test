#!/usr/bin/python
#
# Copyright 2013 Google Inc. All Rights Reserved.
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

"""This code example gets all contacts that aren't invited yet.

To create contacts, run create_contacts.py.

Tags: ContactService.getContactsByStatement
"""
__author__ = 'Vincent Tsao'

# Locate the client library. If module was installed via "setup.py" script, then
# the following two lines are not needed.
import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfpClient
from adspygoogle.dfp import DfpUtils


def main(client):
  # Initialize appropriate service.
  contact_service = client.GetService('ContactService', version='v201306')

  # Create statement object to only select contacts that are uninvited.
  values = [{
      'key': 'status',
      'value': {
          'xsi_type': 'TextValue',
          'value': 'UNINVITED'
      }
  }]
  query = 'WHERE status = :status'

  # Get contacts by statement.
  contacts = DfpUtils.GetAllEntitiesByStatementWithService(
      contact_service, query=query, bind_vars=values)

  # Display results.
  for contact in contacts:
    print ('Contact with ID \'%s\' and name \'%s\' was found.'
           % (contact['id'], contact['name']))

  print
  print 'Number of results found: %s' % len(contacts)

if __name__ == '__main__':
  # Initialize client object.
  dfp_client = DfpClient(path=os.path.join('..', '..', '..', '..', '..'))
  main(dfp_client)
