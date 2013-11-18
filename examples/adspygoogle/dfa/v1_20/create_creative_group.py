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

"""This example creates a creative group associated with a given advertiser. To
get an advertiser ID, run get_advertisers.py. Valid group numbers are
limited to 1 or 2.

Tags: creativegroup.saveCreativeGroup
"""

__author__ = 'api.jdilallo@gmail.com (Joseph DiLallo)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfaClient


ADVERTISER_ID = 'INSERT_ADVERTISER_ID_HERE'
GROUP_NUMBER = 'INSERT_GROUP_NUMBER_HERE'
CREATIVE_GROUP_NAME = 'INSERT_CREATIVE_GROUP_NAME_HERE'


def main(client, advertiser_id, group_number, creative_group_name):
  # Initialize appropriate service.
  creative_group_service = client.GetCreativeGroupService(
      'https://advertisersapitest.doubleclick.net', 'v1.20')

  # Construct and save creative group.
  creative_group = {
      'name': creative_group_name,
      'id': '-1',
      'advertiserId': advertiser_id,
      'groupNumber': group_number
  }
  result = creative_group_service.SaveCreativeGroup(creative_group)[0]

  # Display results.
  print 'Creative group with ID \'%s\' was created.' % result['id']


if __name__ == '__main__':
  # Initialize client object.
  client = DfaClient(path=os.path.join('..', '..', '..', '..'))
  main(client, ADVERTISER_ID, GROUP_NUMBER, CREATIVE_GROUP_NAME)
