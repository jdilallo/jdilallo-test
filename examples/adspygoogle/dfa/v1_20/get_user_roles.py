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

"""This example displays user role name, ID, subnetwork ID, number of assigned
users, and assigned permissions for the given search criteria. Results are
limited to the first 10 records.

Tags: userrole.getUserRoles
"""

__author__ = 'api.jdilallo@gmail.com (Joseph DiLallo)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfaClient


def main(client):
  # Initialize appropriate service.
  user_role_service = client.GetUserRoleService(
      'https://advertisersapitest.doubleclick.net', 'v1.20')

  # Set user role search criteria.
  user_role_search_criteria = {
      'pageSize': '10'
  }

  # Get user roles that match the search criteria.
  results = user_role_service.GetUserRoles(user_role_search_criteria)[0]

  # Display user role names, IDs, subnetwork IDs, number of assigned users, and
  # assigned permissions.
  if results['userRoles']:
    for user_role in results['userRoles']:
      print ('User role with name \'%s\', ID \'%s\', subnetwork ID \'%s\', and '
             'assigned to \'%s\' users was found.'
             % (user_role['name'], user_role['id'], user_role['subnetworkId'],
                user_role['totalAssignedUsers']))
      if user_role['permissions']:
        print '    The above user role has the following permissions:'
        for permission in user_role['permissions']:
          print ('        Permission with name \'%s\' and ID \'%s\'.'
                 % (permission['name'], permission['id']))
      else:
        print '    The above user role has no permissions assigned.'
  else:
    print 'No user roles found for your criteria.'


if __name__ == '__main__':
  # Initialize client object.
  client = DfaClient(path=os.path.join('..', '..', '..', '..'))
  main(client)
