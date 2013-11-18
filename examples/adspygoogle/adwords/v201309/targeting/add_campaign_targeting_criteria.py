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

"""This example adds various types of targeting criteria to a given campaign. To
get campaigns, run get_campaigns.py.

Tags: CampaignCriterionService.mutate
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
  campaign_criterion_service = client.GetCampaignCriterionService(
      version='v201309')

  # Create locations. The IDs can be found in the documentation or retrieved
  # with the LocationCriterionService.
  california = {
      'xsi_type': 'Location',
      'id': '21137'
  }
  mexico = {
      'xsi_type': 'Location',
      'id': '2484'
  }

  # Create languages. The IDs can be found in the documentation or retrieved
  # with the ConstantDataService.
  english = {
      'xsi_type': 'Language',
      'id': '1000'
  }
  spanish = {
      'xsi_type': 'Language',
      'id': '1003'
  }

  # Create a negative campaign criterion operation.
  negative_campaign_criterion_operand = {
      'xsi_type': 'NegativeCampaignCriterion',
      'campaignId': campaign_id,
      'criterion': {
          'xsi_type': 'Keyword',
          'matchType': 'BROAD',
          'text': 'jupiter cruise'
      }
  }

  # Create operations
  operations = []
  for criterion in [california, mexico, english, spanish]:
    operations.append({
        'operator': 'ADD',
        'operand': {
            'campaignId': campaign_id,
            'criterion': criterion
        }
    })
  # Add the negative campaign criterion.
  operations.append({
      'operator': 'ADD',
      'operand': negative_campaign_criterion_operand
  })

  # Make the mutate request.
  result = campaign_criterion_service.mutate(operations)[0]

  # Display the resulting campaign criteria.
  for campaign_criterion in result['value']:
    print ('Campaign criterion with campaign id \'%s\', criterion id \'%s\', '
           'and type \'%s\' was added.'
           % (campaign_criterion['campaignId'],
              campaign_criterion['criterion']['id'],
              campaign_criterion['criterion']['type']))

if __name__ == '__main__':
  # Initialize client object.
  client = AdWordsClient(path=os.path.join('..', '..', '..', '..', '..'))

  main(client, campaign_id)
