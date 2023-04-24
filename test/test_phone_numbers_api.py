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
from swagger_client.api.phone_numbers_api import PhoneNumbersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPhoneNumbersApi(unittest.TestCase):
    """PhoneNumbersApi unit test stubs"""

    def setUp(self):
        self.api = PhoneNumbersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_byoc_number(self):
        """Test case for add_byoc_number

        Add BYOC phone numbers  # noqa: E501
        """
        pass

    def test_assign_phone_number(self):
        """Test case for assign_phone_number

        Assign a phone number to a user  # noqa: E501
        """
        pass

    def test_assign_phone_number_to_emergency_number_pool(self):
        """Test case for assign_phone_number_to_emergency_number_pool

        Assign phone numbers to the emergency number pool  # noqa: E501
        """
        pass

    def test_delete_unassigned_phone_numbers(self):
        """Test case for delete_unassigned_phone_numbers

        Delete unassigned phone numbers  # noqa: E501
        """
        pass

    def test_get_phone_number_details(self):
        """Test case for get_phone_number_details

        Get a phone number  # noqa: E501
        """
        pass

    def test_list_account_phone_numbers(self):
        """Test case for list_account_phone_numbers

        List phone numbers  # noqa: E501
        """
        pass

    def test_unassign_phone_number(self):
        """Test case for unassign_phone_number

        Unassign a phone number  # noqa: E501
        """
        pass

    def test_unassign_phone_number_from_emergency_number_pool(self):
        """Test case for unassign_phone_number_from_emergency_number_pool

        Unassign phone numbers from the emergency number pool  # noqa: E501
        """
        pass

    def test_update_phone_number_details(self):
        """Test case for update_phone_number_details

        Update a phone number  # noqa: E501
        """
        pass

    def test_update_site_for_unassigned_phone_numbers(self):
        """Test case for update_site_for_unassigned_phone_numbers

        Update a site's unassigned phone numbers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
