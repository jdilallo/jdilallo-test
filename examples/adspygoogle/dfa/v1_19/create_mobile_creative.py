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

"""This example creates a mobile display creative in a given advertiser or
campaign. If no campaign is specified then the creative is created in the
advertiser provided. To get assets file names, run create_html_asset.py and
create_image_asset.py. To get a size ID, run get_size.py. To get a creative
type ID, run get_creative_type.py.

Tags: creative.saveCreative
"""

__author__ = 'api.jdilallo@gmail.com (Joseph DiLallo)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfaClient


CAMPAIGN_ID = 'INSERT_CAMPAIGN_ID_HERE'
ADVERTISER_ID = 'INSERT_ADVERTISER_ID_HERE'
CREATIVE_NAME = 'INSERT_CREATIVE_NAME_HERE'
MOBILE_ASSET_FILE_NAME = 'INSERT_MOBILE_ASSET_FILE_NAME_HERE'


def main(client, campaign_id, advertiser_id, creative_name,
         mobile_asset_file_name):
  # Initialize appropriate service.
  creative_service = client.GetCreativeService(
      'https://advertisersapitest.doubleclick.net', 'v1.19')

  # Construct and save mobile creative.
  mobile_creative = {
      'name': creative_name,
      'advertiserId': advertiser_id,
      'typeId': '30',
      'archived': 'false',
      'creativeAssets': [{
          'assetFilename': mobile_asset_file_name
      }]
  }

  # If you don't specify an xsi_type for a creative, the client library will try
  # to infer it from the typeId.
  result = creative_service.SaveCreative(mobile_creative, campaign_id)[0]

  # Display results.
  print 'Mobile creative with ID \'%s\' was created.' % result['id']


if __name__ == '__main__':
  # Initialize client object.
  client = DfaClient(path=os.path.join('..', '..', '..', '..'))
  main(client, CAMPAIGN_ID, ADVERTISER_ID, CREATIVE_NAME,
       MOBILE_ASSET_FILE_NAME)
