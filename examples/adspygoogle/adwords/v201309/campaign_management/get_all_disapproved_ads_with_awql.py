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

"""This example gets all disapproved ads for a given campaign with AWQL. To add
an ad, run add_ads.py.

Tags: AdGroupAdService.get
"""

__author__ = 'api.kwinter@gmail.com (Kevin Winter)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import AdWordsClient


campaign_id = 'INSERT_CAMPAIGN_ID_HERE'


def main(client, campaign_id):
  # Initialize appropriate service.
  ad_group_ad_service = client.GetAdGroupAdService(version='v201309')

  # Construct query and get all ads for a given campaign.
  query = ('SELECT Id, AdGroupAdDisapprovalReasons '
           'WHERE CampaignId = %s AND '
           'AdGroupCreativeApprovalStatus = DISAPPROVED '
           'ORDER BY Id' % campaign_id)
  ads = ad_group_ad_service.Query(query)[0]

  # Display results.
  if 'entries' in ads:
    for ad in ads['entries']:
      print ('Ad with id \'%s\' was disapproved for the following reasons: '
             % (ad['ad']['id']))
      if ad['ad'].get('disapprovalReasons'):
        for reason in ad['ad']['disapprovalReasons']:
          print '\t%s' % reason
      else:
        print '\tReason not provided.'
  else:
    print 'No disapproved ads were found.'

  print
  print ('Usage: %s units, %s operations' % (client.GetUnits(),
                                             client.GetOperations()))


if __name__ == '__main__':
  # Initialize client object.
  client = AdWordsClient(path=os.path.join('..', '..', '..', '..', '..'))

  main(client, campaign_id)
