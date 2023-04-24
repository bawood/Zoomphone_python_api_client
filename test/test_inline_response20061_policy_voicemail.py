# coding: utf-8

"""
    Zoom Phone API

    The Zoom Phone API allows developers to access information from Zoom. You can use this API to build private services or public applications on the [Zoom App Marketplace](http://marketplace.zoom.us). To learn how to get your credentials and create private/public applications, read our [OAuth](https://developers.zoom.us/docs/integrations/oauth/) documentation. All endpoints are available via `https` and are located at `api.zoom.us/v2/`.  For instance, you can list all users on an account via `https://api.zoom.us/v2/users/`.  **Note**: You will get `403` response `Zoom Phone has not been enabled for this account` if the phone account is not set up.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.inline_response20061_policy_voicemail import InlineResponse20061PolicyVoicemail  # noqa: E501
from swagger_client.rest import ApiException


class TestInlineResponse20061PolicyVoicemail(unittest.TestCase):
    """InlineResponse20061PolicyVoicemail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse20061PolicyVoicemail(self):
        """Test InlineResponse20061PolicyVoicemail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.inline_response20061_policy_voicemail.InlineResponse20061PolicyVoicemail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()