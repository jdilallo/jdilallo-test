#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
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

"""This example displays user filter criteria type names and IDs.

Tags: user.getAvailableUserFilterCriteriaTypes
"""

__author__ = 'Joseph DiLallo'

# Import appropriate classes from the client library.
from googleads import dfa


def main(client):
  # Initialize appropriate service.
  user_service = client.GetService(
      'user', 'v1.20', 'https://advertisersapitest.doubleclick.net')

  # Get user filter criteria types.
  results = user_service.getAvailableUserFilterCriteriaTypes()

  # Display user filter criteria types.
  if results:
    for filter_type in results:
      print ('User filter criteria type with name \'%s\' and ID \'%s\' was '
             'found.' % (filter_type['name'], filter_type['id']))
  else:
    print 'No user filter criteria types found.'


if __name__ == '__main__':
  # Initialize client object.
  dfa_client = dfa.DfaClient.LoadFromStorage()
  main(dfa_client)
