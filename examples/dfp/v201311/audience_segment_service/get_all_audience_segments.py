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

"""This code example gets all audience segments.

To create audience segments, run create_audience_segments.py.
"""

__author__ = ('Nicholas Chen',
              'Joseph DiLallo')

# Import appropriate classes from the client library.
from googleads import dfp

SUGGESTED_PAGE_LIMIT = 500


# Initialize client object.
client = dfp.DfpClient.LoadFromStorage()

# Initialize appropriate service.
audience_segment_service = client.GetService(
    'AudienceSegmentService', version='v201311')

# Get all audience segments.
offset, result_set_size = 0, 0

while True:
  # Create a statement to select audience segments.
  filter_statement = {'query': 'LIMIT %s OFFSET %s' % (
      SUGGESTED_PAGE_LIMIT, offset)}

  response = audience_segment_service.getAudienceSegmentsByStatement(
      filter_statement)

  if 'results' in response:
    segments = response['results']
    result_set_size = len(segments)

    for segment in segments:
      print ('Audience segment with id \'%s\' and name '
             '\'%s\' of size %s was found.' %
             (segment['id'], segment['name'], segment['size']))

    offset += result_set_size
    if result_set_size != SUGGESTED_PAGE_LIMIT:
      break
  elif offset == 0:
    print 'No Results Found'
    break

print 'Number of results found: %d' % offset
