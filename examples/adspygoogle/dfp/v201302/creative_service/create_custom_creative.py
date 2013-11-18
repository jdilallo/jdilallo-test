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

"""This example creates a custom creative for a given advertiser. This feature
is only available to DFP premium solution networks. To determine which companies
are advertisers, run get_companies_by_statement.py. To determine which creative
templates exist, run get_all_creative_templates.py."""

__author__ = ('Jeff Sham',
              'Vincent Tsao')

# Locate the client library. If module was installed via "setup.py" script, then
# the following two lines are not needed.
import base64
import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfpClient
from adspygoogle.common import Utils


# Initialize client object.
client = DfpClient(path=os.path.join('..', '..', '..', '..', '..'))

# Initialize appropriate service.
creative_service = client.GetService('CreativeService', version='v201302')

# Set id of the advertiser (company) that the creative will be assigned to.
advertiser_id = 'INSERT_ADVERTISER_COMPANY_ID_HERE'

# Get the image data for the creative.
image_data = open(os.path.join(__file__[:__file__.rfind('/')], '..', 'data',
                               'medium_rectangle.jpg'), 'r').read()
image_data = base64.encodestring(image_data)

# Create the HTML snippet used in the custom creative.
html_snippet = ('<a href=\'%s%s\'><img src=\'%s\'/></a><br>Click above for '
                'great deals!') % ('%%CLICK_URL_UNESC%%', '%%DEST_URL%%',
                                   '%%FILE:IMAGE_ASSET%%')

# Create custom creative.
creative = {
    'type': 'CustomCreative',
    'name': 'Custom Creative #%s' % Utils.GetUniqueName(),
    'advertiserId': advertiser_id,
    'size': {'width': '300', 'height': '250'},
    'destinationUrl': 'http://google.com',
    'customCreativeAssets': [
        {
            'type': 'CustomCreativeAsset',
            'macroName': 'IMAGE_ASSET',
            'assetByteArray': image_data,
            'fileName': 'image%s.jpg' % Utils.GetUniqueName()
        }
    ],
    'htmlSnippet': html_snippet
}

# Call service to create the creative.
creative = creative_service.CreateCreative(creative)[0]

# Display results.
if creative:
  print ('Template creative with id \'%s\', name \'%s\', and type \'%s\' was '
         'created and can be previewed at \'%s\'.'
         % (creative['id'], creative['name'], creative['Creative_Type'],
            creative['previewUrl']))
