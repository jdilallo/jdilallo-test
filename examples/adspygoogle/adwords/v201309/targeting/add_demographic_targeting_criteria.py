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

"""This example adds demographic criteria to an ad group.

To get a list of ad groups, run get_ad_groups.py.

Tags: AdGroupCriterionService.mutate
"""

__author__ = 'api.jdilallo@gmail.com (Joseph Dilallo)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import AdWordsClient


GENDER_MALE = '10'
AGE_RANGE_UNDETERMINED = '503999'

ad_group_id = 'INSERT_AD_GROUP_ID_HERE'


def main(client, ad_group_id):
  # Initialize appropriate service.
  ad_group_criterion_service = client.GetAdGroupCriterionService(
      version='v201309')

  # Create the ad group criteria.
  ad_group_criteria = [
      # Targeting criterion.
      {
          'xsi_type': 'BiddableAdGroupCriterion',
          'adGroupId': ad_group_id,
          'criterion': {
              'xsi_type': 'Gender',
              # Create gender criteria. The IDs can be found in the
              # documentation:
              # https://developers.google.com/adwords/api/docs/appendix/genders.
              'id': GENDER_MALE
          }
      },
      # Exclusion criterion.
      {
          'xsi_type': 'NegativeAdGroupCriterion',
          'adGroupId': ad_group_id,
          'criterion': {
              'xsi_type': 'AgeRange',
              # Create age range criteria. The IDs can be found in the
              # documentation:
              # https://developers.google.com/adwords/api/docs/appendix/ages.
              'id': AGE_RANGE_UNDETERMINED
          }
      }
  ]

  # Create operations.
  operations = []
  for criterion in ad_group_criteria:
    operations.append({
        'operator': 'ADD',
        'operand': criterion
    })

  response = ad_group_criterion_service.Mutate(operations)[0]

  if response and response['value']:
    criteria = response['value']
    for ad_group_criterion in criteria:
      criterion = ad_group_criterion['criterion']
      print ('Ad group criterion with ad group ID %s, criterion ID %s and '
             'type \'%s\' was added.' %
             (ad_group_criterion['adGroupId'], criterion['id'],
              criterion['type']))
  else:
    print 'No criteria were returned.'


if __name__ == '__main__':
  # Initialize client object.
  client = AdWordsClient(path=os.path.join('..', '..', '..', '..', '..'))

  main(client, ad_group_id)
