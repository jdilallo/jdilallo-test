#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
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

"""Creates and attaches a shared set to a campaign.

This example creates a shared list of negative broad match keywords and
attaches them to a campaign.

Note: Shared sets is a Beta feature.

Tags: SharedSetService.mutate, CampaignSharedSetService.mutate
Tags: SharedCriterionService.mutate
Api: AdWordsOnly
"""

__author__ = 'Joseph DiLallo'

from googleads import adwords


CAMPAIGN_ID = 'INSERT_CAMPAIGN_HERE'


def main(client, campaign_id):
  # Initialize appropriate service.
  shared_set_service = client.GetService('SharedSetService', version='v201309')

  keyword_texts = ['mars cruise', 'mars hotels']

  # Create shared negative Keyword Set.
  keyword_set = {
      'name': 'API Negative keyword list - %s' % ','.join(keyword_texts),
      'type': 'NEGATIVE_KEYWORDS'
  }

  operation = {
      'operator': 'ADD',
      'operand': keyword_set
  }

  result = shared_set_service.mutate([operation])

  # Get the shared set ID and print it.
  keyword_set = result['value'][0]
  shared_set_id = keyword_set['sharedSetId']
  print ('SharedSet \'%s\' has been created with ID \'%s\'' %
         (keyword_set['name'], shared_set_id))

  shared_criterion_service = client.GetService(
      'SharedCriterionService', version='v201309')

  operations = []
  for keyword_text in keyword_texts:
    shared_criterion = {
        'criterion': {
            'text': keyword_text,
            'matchType': 'BROAD',
            'xsi_type': 'Keyword'
        },
        'negative': 'true',
        'sharedSetId': shared_set_id
    }

    operations.append({'operator': 'ADD', 'operand': shared_criterion})

  result = shared_criterion_service.mutate(operations)

  for shared_criterion in result['value']:
    print ('Added shared criterion ID %s \'%s\' to shared set with ID %s.' %
           (shared_criterion['criterion']['id'],
            shared_criterion['criterion']['text'],
            shared_criterion['sharedSetId']))

  # Attach the articles to the campaign.
  campaign_set = {
      'campaignId': campaign_id,
      'sharedSetId': shared_set_id
  }

  campaign_shared_set_service = client.GetCampaignSharedSetService(
      version='v201309')

  result = campaign_shared_set_service.mutate([
      {'operator': 'ADD', 'operand': campaign_set}
  ])
  campaign_shared_set = result['value'][0]
  print ('Shared set ID %s was attached to campaign ID %s' %
         (campaign_shared_set['sharedSetId'],
          campaign_shared_set['campaignId']))


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client, CAMPAIGN_ID)
