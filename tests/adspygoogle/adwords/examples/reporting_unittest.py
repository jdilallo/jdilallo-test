#!/usr/bin/python
#
# Copyright 2011 Google Inc. All Rights Reserved.
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

"""Unit tests to cover Reporting examples."""

__author__ = 'api.kwinter@gmail.com (Kevin Winter)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))
import unittest

from examples.adspygoogle.adwords.v201309.reporting import download_criteria_report
from examples.adspygoogle.adwords.v201309.reporting import download_criteria_report_with_awql
from examples.adspygoogle.adwords.v201309.reporting import get_report_fields
from tests.adspygoogle.adwords import client
from tests.adspygoogle.adwords import SERVER_V201309
from tests.adspygoogle.adwords import TEST_VERSION_V201309
from tests.adspygoogle.adwords import VERSION_V201309


class Reporting(unittest.TestCase):

  """Unittest suite for Remarketing code examples."""

  SERVER = SERVER_V201309
  VERSION = VERSION_V201309
  client.debug = False

  def setUp(self):
    """Prepare unittest."""
    client.use_mcc = False

  def testDownloadCriteriaReport(self):
    """Tests whether we can download a criteria report."""
    download_criteria_report.main(client, '/tmp/report.rpt')

  def testDownloadCriteriaReportWithAwql(self):
    """Tests whether we can download a criteria report with AWQL."""
    download_criteria_report_with_awql.main(client, '/tmp/report.rpt')

  def testGetReportFields(self):
    """Test whether we can get report fields."""
    get_report_fields.main(client, 'CAMPAIGN_PERFORMANCE_REPORT')


if __name__ == '__main__':
  if TEST_VERSION_V201309:
    unittest.main()
