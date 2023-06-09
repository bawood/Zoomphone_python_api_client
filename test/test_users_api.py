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
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_outbound_caller_numbers(self):
        """Test case for add_user_outbound_caller_numbers

        Add phone numbers for users' customized outbound caller ID  # noqa: E501
        """
        pass

    def test_add_user_setting(self):
        """Test case for add_user_setting

        Add a user's shared access setting  # noqa: E501
        """
        pass

    def test_assign_calling_plan(self):
        """Test case for assign_calling_plan

        Assign calling plan to a user  # noqa: E501
        """
        pass

    def test_batch_add_users(self):
        """Test case for batch_add_users

        Batch add users  # noqa: E501
        """
        pass

    def test_delete_user_outbound_caller_numbers(self):
        """Test case for delete_user_outbound_caller_numbers

        Remove users' customized outbound caller ID phone numbers  # noqa: E501
        """
        pass

    def test_delete_user_setting(self):
        """Test case for delete_user_setting

        Delete a user's shared access setting  # noqa: E501
        """
        pass

    def test_get_user_policy_details(self):
        """Test case for get_user_policy_details

        Get user policy details  # noqa: E501
        """
        pass

    def test_list_phone_users(self):
        """Test case for list_phone_users

        List phone users  # noqa: E501
        """
        pass

    def test_list_user_customize_outbound_caller_numbers(self):
        """Test case for list_user_customize_outbound_caller_numbers

        List users' phone numbers for a customized outbound caller ID  # noqa: E501
        """
        pass

    def test_phone_user(self):
        """Test case for phone_user

        Get a user's profile  # noqa: E501
        """
        pass

    def test_phone_user_settings(self):
        """Test case for phone_user_settings

        Get a user's profile settings  # noqa: E501
        """
        pass

    def test_unassign_calling_plan(self):
        """Test case for unassign_calling_plan

        Unassign user's calling plan  # noqa: E501
        """
        pass

    def test_update_calling_plan(self):
        """Test case for update_calling_plan

        Update user's calling plan  # noqa: E501
        """
        pass

    def test_update_user_policy(self):
        """Test case for update_user_policy

        Update user policy  # noqa: E501
        """
        pass

    def test_update_user_profile(self):
        """Test case for update_user_profile

        Update a user's profile  # noqa: E501
        """
        pass

    def test_update_user_setting(self):
        """Test case for update_user_setting

        Update a user's shared access setting  # noqa: E501
        """
        pass

    def test_update_user_settings(self):
        """Test case for update_user_settings

        Update a user's profile settings  # noqa: E501
        """
        pass

    def test_update_users_properties_in_batch(self):
        """Test case for update_users_properties_in_batch

        Update multiple users' properties in batch  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
