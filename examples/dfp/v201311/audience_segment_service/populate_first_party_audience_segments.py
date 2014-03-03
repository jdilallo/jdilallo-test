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

"""This example populates a specific first party audience segment.

To determine which first party audience segments exist, run
get_first_party_audience_segments.py.
"""

__author__ = ('Nicholas Chen',
              'Joseph DiLallo')

# Import appropriate classes from the client library.
from googleads import dfp

AUDIENCE_SEGMENT_ID = 'INSERT_AUDIENCE_SEGMENT_ID_HERE'


# Initialize client object.
client = dfp.DfpClient.LoadFromStorage()

# Initialize appropriate service.
audience_segment_service = client.GetService(
    'AudienceSegmentService', version='v201311')

# Specify bind value to filter on first party audience segments
values = [
    {
        'key': 'type',
        'value': {
            'xsi_type': 'TextValue',
            'value': 'FIRST_PARTY'
            }
    },
    {
        'key': 'audience_segment_id',
        'value': {
            'xsi_type': 'NumberValue',
            'value': AUDIENCE_SEGMENT_ID
            }
    }
]

# Create a statement to select specified first party audience segments.
filter_statement = {'query': ('WHERE Type = :type AND Id = :audience_segment_id'
                              ' LIMIT 1'),
                    'values': values}

response = audience_segment_service.getAudienceSegmentsByStatement(
    filter_statement)

if 'results' in response:
  segments = response['results']

  for segment in segments:
    print ('Audience segment with id \'%s\' and name \'%s\' will be populated.'
           % (segment['id'], segment['name']))

  action = {
      'AudienceSegmentAction.Type': 'PopulateAudienceSegments'
  }

  populated_audience_segments = (
      audience_segment_service.performAudienceSegmentAction(
          action, filter_statement))

  print ('%s audience segment populated' %
         populated_audience_segments['numChanges'])
else:
  print 'No Results Found'
