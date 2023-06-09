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
from swagger_client.api.settings_api import SettingsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_main_company_number(self):
        """Test case for change_main_company_number

        Change main company number  # noqa: E501
        """
        pass

    def test_get_ported_numbers_details(self):
        """Test case for get_ported_numbers_details

        Get ported number details  # noqa: E501
        """
        pass

    def test_list_byocsip_trunk(self):
        """Test case for list_byocsip_trunk

        List BYOC SIP trunks  # noqa: E501
        """
        pass

    def test_list_ported_numbers(self):
        """Test case for list_ported_numbers

        List ported numbers  # noqa: E501
        """
        pass

    def test_list_sip_groups(self):
        """Test case for list_sip_groups

        List SIP groups  # noqa: E501
        """
        pass

    def test_phone_setting(self):
        """Test case for phone_setting

        Get phone account settings  # noqa: E501
        """
        pass

    def test_update_phone_settings(self):
        """Test case for update_phone_settings

        Update phone account settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
