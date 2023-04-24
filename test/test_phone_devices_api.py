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
from swagger_client.api.phone_devices_api import PhoneDevicesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPhoneDevicesApi(unittest.TestCase):
    """PhoneDevicesApi unit test stubs"""

    def setUp(self):
        self.api = PhoneDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_extensions_to_a_device(self):
        """Test case for add_extensions_to_a_device

        Assign an entity to a device  # noqa: E501
        """
        pass

    def test_add_phone_device(self):
        """Test case for add_phone_device

        Add a device  # noqa: E501
        """
        pass

    def test_delete_a_device(self):
        """Test case for delete_a_device

        Delete a device  # noqa: E501
        """
        pass

    def test_delete_extension_from_a_device(self):
        """Test case for delete_extension_from_a_device

        Unassign an entity from the device  # noqa: E501
        """
        pass

    def test_get_a_device(self):
        """Test case for get_a_device

        Get device details  # noqa: E501
        """
        pass

    def test_list_phone_devices(self):
        """Test case for list_phone_devices

        List devices  # noqa: E501
        """
        pass

    def test_reboot_phone_device(self):
        """Test case for reboot_phone_device

        Reboot a desk phone  # noqa: E501
        """
        pass

    def test_sync_phone_device(self):
        """Test case for sync_phone_device

        Sync deskphones  # noqa: E501
        """
        pass

    def test_update_a_device(self):
        """Test case for update_a_device

        Update a device  # noqa: E501
        """
        pass

    def test_update_provision_template_to_device(self):
        """Test case for update_provision_template_to_device

        Update provision template of a device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
