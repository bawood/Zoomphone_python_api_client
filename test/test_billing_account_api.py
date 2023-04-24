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
from swagger_client.api.billing_account_api import BillingAccountApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBillingAccountApi(unittest.TestCase):
    """BillingAccountApi unit test stubs"""

    def setUp(self):
        self.api = BillingAccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_a_billing_account(self):
        """Test case for get_a_billing_account

        Get billing account details  # noqa: E501
        """
        pass

    def test_list_billing_account(self):
        """Test case for list_billing_account

        List billing accounts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
