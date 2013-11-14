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

"""Unit tests to cover Targeting examples."""

__author__ = 'api.kwinter@gmail.com (Kevin Winter)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))
import time
import unittest

from examples.adspygoogle.adwords.v201309.targeting import add_campaign_targeting_criteria
from examples.adspygoogle.adwords.v201309.targeting import add_demographic_targeting_criteria
from examples.adspygoogle.adwords.v201309.targeting import get_campaign_targeting_criteria
from examples.adspygoogle.adwords.v201309.targeting import get_targetable_languages_and_carriers
from examples.adspygoogle.adwords.v201309.targeting import lookup_location
from tests.adspygoogle.adwords import client
from tests.adspygoogle.adwords import SERVER_V201309
from tests.adspygoogle.adwords import TEST_VERSION_V201309
from tests.adspygoogle.adwords import util
from tests.adspygoogle.adwords import VERSION_V201309


class Targeting(unittest.TestCase):

  """Unittest suite for Targeting code examples."""

  SERVER = SERVER_V201309
  VERSION = VERSION_V201309
  client.debug = False
  loaded = False

  def setUp(self):
    """Prepare unittest."""
    time.sleep(3)
    client.use_mcc = False
    if not self.__class__.loaded:
      self.__class__.campaign_id = util.CreateTestCampaign(client)
      self.__class__.ad_group_id = util.CreateTestAdGroup(
          client, self.__class__.campaign_id)
      self.__class__.loaded = True

  def testAddCampaignTargetingCriteria(self):
    """Test whether we can add campaign targeting criteria."""
    add_campaign_targeting_criteria.main(client, self.__class__.campaign_id)

  def testAddDemographicTargetingCriteria(self):
    """Test whether we can add ad group targeting criteria."""
    add_demographic_targeting_criteria.main(client, self.__class__.ad_group_id)

  def testGetCampaignTargetingCriteria(self):
    """Test whether we can get campaign targeting criteria."""
    get_campaign_targeting_criteria.main(client)

  def testGetTargetableLanguagesAndCarriers(self):
    """Test whether we can get targetable languages and carriers."""
    get_targetable_languages_and_carriers.main(client)

  def testLookupLocation(self):
    """Test whether we can get lookup locations."""
    lookup_location.main(client)


if __name__ == '__main__':
  if TEST_VERSION_V201309:
    unittest.main()
