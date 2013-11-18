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

"""This example gets all ad group criteria in an account. To add keywords, run
add_keywords.py.

Tags: AdGroupCriterionService.get
Api: AdWordsOnly
"""

__author__ = 'api.kwinter@gmail.com (Kevin Winter)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import AdWordsClient


PAGE_SIZE = 500


def main(client):
  # Initialize appropriate service.
  ad_group_criterion_service = client.GetAdGroupCriterionService(
      version='v201309')

  # Construct selector and get all ad group criteria.
  offset = 0
  selector = {
      'fields': ['AdGroupId', 'Id', 'Text', 'KeywordMatchType', 'PlacementUrl'],
      'predicates': [{
          'field': 'CriteriaType',
          'operator': 'EQUALS',
          'values': ['KEYWORD']
      }],
      'paging': {
          'startIndex': str(offset),
          'numberResults': str(PAGE_SIZE)
      }
  }
  more_pages = True
  while more_pages:
    page = ad_group_criterion_service.Get(selector)[0]

    # Display results.
    if 'entries' in page:
      for criterion in page['entries']:
        print ('Keyword ad group criterion with ad group id \'%s\', criterion '
               'id \'%s\', text \'%s\', and match type \'%s\' was found.'
               % (criterion['adGroupId'], criterion['criterion']['id'],
                  criterion['criterion']['text'],
                  criterion['criterion']['matchType']))
    else:
      print 'No keywords were found.'
    offset += PAGE_SIZE
    selector['paging']['startIndex'] = str(offset)
    more_pages = offset < int(page['totalNumEntries'])

  print
  print ('Usage: %s units, %s operations' % (client.GetUnits(),
                                             client.GetOperations()))


if __name__ == '__main__':
  # Initialize client object.
  client = AdWordsClient(path=os.path.join('..', '..', '..', '..', '..'))

  main(client)
