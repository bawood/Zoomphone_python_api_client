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
from swagger_client.api.call_handling_api import CallHandlingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCallHandlingApi(unittest.TestCase):
    """CallHandlingApi unit test stubs"""

    def setUp(self):
        self.api = CallHandlingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_call_handling(self):
        """Test case for add_call_handling

        Add a call handling setting  # noqa: E501
        """
        pass

    def test_delete_call_handling(self):
        """Test case for delete_call_handling

        Delete a call handling setting  # noqa: E501
        """
        pass

    def test_get_call_handling(self):
        """Test case for get_call_handling

        Get call handling settings  # noqa: E501
        """
        pass

    def test_update_call_handling(self):
        """Test case for update_call_handling

        Update a call handling setting  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()