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

"""Unit tests to cover the oauth2 module."""

__author__ = 'Joseph DiLallo'

import StringIO
import unittest
import urllib2

import mock
from oauthlib import oauth2

import googleads.oauth2


class GoogleOAuth2ClientTest(unittest.TestCase):
  """Tests for the googleads.oauth2.GoogleOAuth2Client class."""

  def testSetHeaders(self):
    """For coverage."""
    self.assertRaises(
        NotImplementedError,
        googleads.oauth2.GoogleOAuth2Client().CreateHttpHeader)


class GoogleRefreshTokenClientTest(unittest.TestCase):
  """Tests for the googleads.oauth2.GoogleRefreshTokenClient class."""

  def setUp(self):
    self.client_id = 'client_id'
    self.client_secret = 'itsasecret'
    self.refresh_token = 'refreshing'
    self.https_proxy = 'my.proxy.com:443'
    with mock.patch('oauthlib.oauth2.BackendApplicationClient'
                   ) as mock_oauthlib_client:
      self.oauthlib_client = mock_oauthlib_client.return_value
      self.googleads_client = googleads.oauth2.GoogleRefreshTokenClient(
          self.client_id, self.client_secret, self.refresh_token,
          self.https_proxy)

  def testHeaderHandler_noRefresh(self):
    header = {'Authorization': 'b'}
    self.oauthlib_client.add_token.return_value = ('unused', header, 'unusued')
    self.assertEquals(header, self.googleads_client.CreateHttpHeader())

  def testHeaderHandler_refresh(self):
    header = {u'Authorization': 'b'}
    post_body = 'post_body'
    content = 'content'
    fake_request = StringIO.StringIO()
    fake_request.write(content)
    fake_request.seek(0)
    self.oauthlib_client.add_token.side_effect = [oauth2.TokenExpiredError(),
                                                  ('unused', header, 'unusued')]
    self.oauthlib_client.prepare_refresh_body.return_value = post_body

    # TODO(user): Make work with Python 3.
    with mock.patch('urllib2.urlopen') as mock_urlopen:
      with mock.patch('urllib2.Request') as mock_request:
        mock_urlopen.return_value = fake_request
        returned_header = self.googleads_client.CreateHttpHeader()

        mock_request.assert_called_once_with(mock.ANY, post_body, mock.ANY)
        mock_urlopen.assert_called_once_with(mock_request.return_value)
    self.assertEquals(header, returned_header)
    self.oauthlib_client.parse_request_body_response.assert_called_once_with(
        content)
    self.assertEquals(2, len(self.oauthlib_client.add_token.call_args_list))
    self.assertEquals(str, type(returned_header.keys()[0]))

  def testHeaderHandler_refreshFails(self):
    post_body = 'post_body'
    error = urllib2.HTTPError('', 400, 'Bad Request', {}, None)

    self.oauthlib_client.add_token.side_effect = oauth2.TokenExpiredError()
    self.oauthlib_client.prepare_refresh_body.return_value = post_body

    # TODO(user): Make work with Python 3.
    with mock.patch('urllib2.urlopen') as mock_urlopen:
      with mock.patch('urllib2.Request') as mock_request:
        mock_urlopen.side_effect = error
        self.assertEquals({}, self.googleads_client.CreateHttpHeader())

        mock_request.assert_called_once_with(mock.ANY, post_body, mock.ANY)
        mock_urlopen.assert_called_once_with(mock_request.return_value)
    self.assertFalse(self.oauthlib_client.parse_request_body_response.called)
    self.oauthlib_client.add_token.assert_called_once_with(mock.ANY)


if __name__ == '__main__':
  unittest.main()
