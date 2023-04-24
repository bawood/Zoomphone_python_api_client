# coding: utf-8

"""
    Zoom Phone API

    The Zoom Phone API allows developers to access information from Zoom. You can use this API to build private services or public applications on the [Zoom App Marketplace](http://marketplace.zoom.us). To learn how to get your credentials and create private/public applications, read our [OAuth](https://developers.zoom.us/docs/integrations/oauth/) documentation. All endpoints are available via `https` and are located at `api.zoom.us/v2/`.  For instance, you can list all users on an account via `https://api.zoom.us/v2/users/`.  **Note**: You will get `403` response `Zoom Phone has not been enabled for this account` if the phone account is not set up.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SharedLineAppearanceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_shared_line_appearances(self, **kwargs):  # noqa: E501
        """List shared line appearances  # noqa: E501

        Use this API to list [shared line appearance](https://support.zoom.us/hc/en-us/articles/4406753208461-Enabling-or-disabling-shared-lines-privacy-mode) instances.  **Prerequisites:**  * Pro or higher account with Zoom Phone license  * Account owner or admin privileges    **Scopes:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_shared_line_appearances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned within a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_shared_line_appearances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_shared_line_appearances_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_shared_line_appearances_with_http_info(self, **kwargs):  # noqa: E501
        """List shared line appearances  # noqa: E501

        Use this API to list [shared line appearance](https://support.zoom.us/hc/en-us/articles/4406753208461-Enabling-or-disabling-shared-lines-privacy-mode) instances.  **Prerequisites:**  * Pro or higher account with Zoom Phone license  * Account owner or admin privileges    **Scopes:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_shared_line_appearances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned within a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'next_page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_shared_line_appearances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page_token' in params:
            query_params.append(('next_page_token', params['next_page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/shared_line_appearances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20063',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)