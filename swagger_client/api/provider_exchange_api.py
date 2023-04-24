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


class ProviderExchangeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_peering_phone_numbers(self, **kwargs):  # noqa: E501
        """Add peering phone numbers  # noqa: E501

        Adds phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_peering_phone_numbers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PeeringNumbersBody body:
        :return: InlineResponse20120
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_peering_phone_numbers_with_http_info(self, **kwargs):  # noqa: E501
        """Add peering phone numbers  # noqa: E501

        Adds phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_peering_phone_numbers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PeeringNumbersBody body:
        :return: InlineResponse20120
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_peering_phone_numbers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/peering/numbers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20120',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_peering_phone_numbers(self, **kwargs):  # noqa: E501
        """Remove peering phone numbers  # noqa: E501

        Removes phone numbers added to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes**: `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_peering_phone_numbers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PeeringNumbersBody1 body:
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_peering_phone_numbers_with_http_info(self, **kwargs):  # noqa: E501
        """Remove peering phone numbers  # noqa: E501

        Removes phone numbers added to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes**: `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_peering_phone_numbers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PeeringNumbersBody1 body:
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_peering_phone_numbers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/peering/numbers', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_carrier_peering_phone_numbers(self, **kwargs):  # noqa: E501
        """List carrier peering phone numbers.  # noqa: E501

        Returns phone numbers pushed by the carrier to different customers. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:read:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_carrier_peering_phone_numbers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The total number of records returned from a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str phone_number: To filter results by the given phone number.
        :return: InlineResponse20050
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_carrier_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_carrier_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_carrier_peering_phone_numbers_with_http_info(self, **kwargs):  # noqa: E501
        """List carrier peering phone numbers.  # noqa: E501

        Returns phone numbers pushed by the carrier to different customers. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:read:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_carrier_peering_phone_numbers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The total number of records returned from a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str phone_number: To filter results by the given phone number.
        :return: InlineResponse20050
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'next_page_token', 'phone_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_carrier_peering_phone_numbers" % key
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
        if 'phone_number' in params:
            query_params.append(('phone_number', params['phone_number']))  # noqa: E501

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
            '/phone/carrier_peering/numbers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20050',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_peering_phone_numbers(self, **kwargs):  # noqa: E501
        """List peering phone numbers  # noqa: E501

        Returns phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:read:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_peering_phone_numbers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The total number of records returned from a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str phone_number: The sender's or receiver's phone number that limits the list of SMS sessions.
        :param int carrier_code: The carrier's code. The `clientId` that maps to a carrier peered with Zoom.  This parameter is required if you do **not** use an OAuth token or the OAuth token does not contain the `clientId`.
        :return: InlineResponse20047
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_peering_phone_numbers_with_http_info(self, **kwargs):  # noqa: E501
        """List peering phone numbers  # noqa: E501

        Returns phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:read:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_peering_phone_numbers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The total number of records returned from a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str phone_number: The sender's or receiver's phone number that limits the list of SMS sessions.
        :param int carrier_code: The carrier's code. The `clientId` that maps to a carrier peered with Zoom.  This parameter is required if you do **not** use an OAuth token or the OAuth token does not contain the `clientId`.
        :return: InlineResponse20047
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'next_page_token', 'phone_number', 'carrier_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_peering_phone_numbers" % key
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
        if 'phone_number' in params:
            query_params.append(('phone_number', params['phone_number']))  # noqa: E501
        if 'carrier_code' in params:
            query_params.append(('carrier_code', params['carrier_code']))  # noqa: E501

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
            '/phone/peering/numbers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20047',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_peering_phone_numbers(self, **kwargs):  # noqa: E501
        """Update peering phone numbers  # noqa: E501

        Updates phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners that have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_peering_phone_numbers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PeeringNumbersBody2 body:
        :return: InlineResponse20049
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_peering_phone_numbers_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_peering_phone_numbers_with_http_info(self, **kwargs):  # noqa: E501
        """Update peering phone numbers  # noqa: E501

        Updates phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners that have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_peering_phone_numbers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PeeringNumbersBody2 body:
        :return: InlineResponse20049
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_peering_phone_numbers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/peering/numbers', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20049',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
