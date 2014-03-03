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

"""This example deletes an ad group by setting the status to 'DELETED'.

To get ad groups, run get_ad_groups.py.

Tags: AdGroupService.mutate
"""

__author__ = ('api.kwinter@gmail.com (Kevin Winter)'
              'Joseph DiLallo')

from datetime import datetime

from googleads import adwords


AD_GROUP_ID = 'INSERT_AD_GROUP_ID_HERE'


def main(client, ad_group_id):
  # Initialize appropriate service.
  ad_group_service = client.GetService('AdGroupService', version='v201309')

  # Construct operations and delete ad group.
  operations = [{
      'operator': 'SET',
      'operand': {
          'id': ad_group_id,
          # We recommend including the original name when renaming before
          # delete.
          'name': ('Deleted on %s' %
                   datetime.today().strftime('%Y%m%d %H:%M:%S.%f')),
          'status': 'DELETED'
      }
  }]
  result = ad_group_service.mutate(operations)

  # Display results.
  for ad_group in result['value']:
    print ('Ad group with name \'%s\' and id \'%s\' was deleted.'
           % (ad_group['name'], ad_group['id']))


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client, AD_GROUP_ID)