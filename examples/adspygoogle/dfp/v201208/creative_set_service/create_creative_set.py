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

"""This code example creates new creative sets.

To determine which creative sets exist, run get_all_creative_sets.py.

Tags: CreativeSetService.createCreativeSet
"""

__author__ = 'api.shamjeff@gmail.com (Jeff Sham)'

# Locate the client library. If module was installed via "setup.py" script, then
# the following two lines are not needed.
import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfpClient
from adspygoogle.common import Utils

MASTER_CREATIVE_ID = 'INSERT_MASTER_CREATIVE_ID_HERE'
COMPANION_CREATIVE_ID = 'INSERT_COMPANION_CREATIVE_ID_HERE'


def main(client, master_creative_id, companion_creative_id):
  # Initialize appropriate service.
  creative_set_service = client.GetService('CreativeSetService',
                                           version='v201208')

  # Create creative set objects.
  creative_set = {'name': 'Creative set #%s' % Utils.GetUniqueName(),
                  'masterCreativeId': master_creative_id,
                  'companionCreativeIds': [companion_creative_id]}

  # Add creative sets.
  creative_set = creative_set_service.CreateCreativeSet(creative_set)[0]

  # Display results.
  if creative_set:
    print (('Creative set with ID \'%s\', master creative ID \'%s\', and '
            'companion creative IDs {%s} was created.')
           % (creative_set['id'], creative_set['masterCreativeId'],
              ','.join(creative_set['companionCreativeIds'])))

if __name__ == '__main__':
  # Initialize client object.
  dfp_client = DfpClient(path=os.path.join('..', '..', '..', '..', '..'))
  main(dfp_client, MASTER_CREATIVE_ID, COMPANION_CREATIVE_ID)
