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

"""This example displays all of the available permissions that a user role or
subnetwork may be endowed with. To get a subnetwork ID, run
get_subnetworks.py.

A user role may not be set with more permissions than the subnetwork it
belongs to. You may enter a subnetwork ID to see the maximum permissions a
user role belonging to it can have, or enter '0' as the subnetwork ID to see
all possible permissions.

Tags: userrole.getAvailablePermissions
"""

__author__ = 'api.jdilallo@gmail.com (Joseph DiLallo)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfaClient


SUBNETWORK_ID = 'INSERT_SUBNETWORK_ID_HERE'


def main(client, subnetwork_id):
  # Initialize appropriate service.
  user_role_service = client.GetUserRoleService(
      'https://advertisersapitest.doubleclick.net', 'v1.19')

  # Get available permissions.
  results = user_role_service.GetAvailablePermissions(subnetwork_id)

  # Display permission name and its ID.
  if results:
    for permission in results:
      print ('Permission with name \'%s\' and ID \'%s\' was found.'
             % (permission['name'], permission['id']))
  else:
    print 'No permissions found.'


if __name__ == '__main__':
  # Initialize client object.
  client = DfaClient(path=os.path.join('..', '..', '..', '..'))
  main(client, SUBNETWORK_ID)
