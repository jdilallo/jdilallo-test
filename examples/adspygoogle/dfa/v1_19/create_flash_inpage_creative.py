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

"""This example creates a "Flash InPage" creative in a given advertiser or
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
SWF_ASSET_FILE_NAME = 'INSERT_SWF_ASSET_FILE_NAME_HERE'
IMG_ASSET_FILE_NAME = 'INSERT_IMG_ASSET_FILE_NAME_HERE'
SIZE_ID = 'INSERT_SIZE_ID_HERE'


def main(client, campaign_id, advertiser_id, creative_name, swf_asset_file_name,
         img_asset_file_name, size_id):
  # Initialize appropriate service.
  creative_service = client.GetCreativeService(
      'https://advertisersapitest.doubleclick.net', 'v1.19')

  # Construct and save flash inpage creative structure.
  flash_inpage_creative = {
      'name': creative_name,
      'id': '0',
      'advertiserId': advertiser_id,
      'typeId': '24',
      'sizeId': size_id,
      'codeLocked': 'true',
      'active': 'true',
      'parentFlashAsset': {
          'assetFilename': swf_asset_file_name
      },
      'wmode': 'opaque',
      'backupImageAsset': {
          'assetFilename': img_asset_file_name
      },
      'backupImageTargetWindow': {
          'option': '_blank'
      }
  }

  result = creative_service.SaveCreative(flash_inpage_creative, campaign_id)[0]

  # Display results.
  print 'Flash inpage creative with ID \'%s\' was created.' % result['id']


if __name__ == '__main__':
  # Initialize client object.
  client = DfaClient(path=os.path.join('..', '..', '..', '..'))
  main(client, CAMPAIGN_ID, ADVERTISER_ID, CREATIVE_NAME, SWF_ASSET_FILE_NAME,
       IMG_ASSET_FILE_NAME, SIZE_ID)
