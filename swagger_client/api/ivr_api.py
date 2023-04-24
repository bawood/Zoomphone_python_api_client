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


class IVRApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_auto_receptionist_ivr(self, auto_receptionist_id, **kwargs):  # noqa: E501
        """Get auto receptionist IVR  # noqa: E501

        Gets an [interactive voice response (IVR) system](https://support.zoom.us/hc/en-us/articles/360038601971) of the specified auto receptionist.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_receptionist_ivr(auto_receptionist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auto_receptionist_id: The unique identifier of the auto receptionist. It can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. (required)
        :param str hours_type: The query hours type: `business_hours` or `closed_hours`, default `business_hours`.
        :param str holiday_id: The auto receptionist holiday hours ID. If both `holiday_id` and `hours_type` are passed, `holiday_id` has a high priority and `hours_type` is invalid.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_auto_receptionist_ivr_with_http_info(auto_receptionist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_auto_receptionist_ivr_with_http_info(auto_receptionist_id, **kwargs)  # noqa: E501
            return data

    def get_auto_receptionist_ivr_with_http_info(self, auto_receptionist_id, **kwargs):  # noqa: E501
        """Get auto receptionist IVR  # noqa: E501

        Gets an [interactive voice response (IVR) system](https://support.zoom.us/hc/en-us/articles/360038601971) of the specified auto receptionist.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_receptionist_ivr_with_http_info(auto_receptionist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auto_receptionist_id: The unique identifier of the auto receptionist. It can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. (required)
        :param str hours_type: The query hours type: `business_hours` or `closed_hours`, default `business_hours`.
        :param str holiday_id: The auto receptionist holiday hours ID. If both `holiday_id` and `hours_type` are passed, `holiday_id` has a high priority and `hours_type` is invalid.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auto_receptionist_id', 'hours_type', 'holiday_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_receptionist_ivr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auto_receptionist_id' is set
        if ('auto_receptionist_id' not in params or
                params['auto_receptionist_id'] is None):
            raise ValueError("Missing the required parameter `auto_receptionist_id` when calling `get_auto_receptionist_ivr`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auto_receptionist_id' in params:
            path_params['autoReceptionistId'] = params['auto_receptionist_id']  # noqa: E501

        query_params = []
        if 'hours_type' in params:
            query_params.append(('hours_type', params['hours_type']))  # noqa: E501
        if 'holiday_id' in params:
            query_params.append(('holiday_id', params['holiday_id']))  # noqa: E501

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
            '/phone/auto_receptionists/{autoReceptionistId}/ivr', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_auto_receptionist_ivr(self, auto_receptionist_id, **kwargs):  # noqa: E501
        """Update auto receptionist IVR  # noqa: E501

        Updates the [interactive voice response (IVR) system](https://support.zoom.us/hc/en-us/articles/360038601971) of the specified auto receptionist.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_auto_receptionist_ivr(auto_receptionist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auto_receptionist_id: The auto receptionist id. (required)
        :param AutoReceptionistIdIvrBody body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_auto_receptionist_ivr_with_http_info(auto_receptionist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_auto_receptionist_ivr_with_http_info(auto_receptionist_id, **kwargs)  # noqa: E501
            return data

    def update_auto_receptionist_ivr_with_http_info(self, auto_receptionist_id, **kwargs):  # noqa: E501
        """Update auto receptionist IVR  # noqa: E501

        Updates the [interactive voice response (IVR) system](https://support.zoom.us/hc/en-us/articles/360038601971) of the specified auto receptionist.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_auto_receptionist_ivr_with_http_info(auto_receptionist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auto_receptionist_id: The auto receptionist id. (required)
        :param AutoReceptionistIdIvrBody body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auto_receptionist_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_auto_receptionist_ivr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auto_receptionist_id' is set
        if ('auto_receptionist_id' not in params or
                params['auto_receptionist_id'] is None):
            raise ValueError("Missing the required parameter `auto_receptionist_id` when calling `update_auto_receptionist_ivr`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auto_receptionist_id' in params:
            path_params['autoReceptionistId'] = params['auto_receptionist_id']  # noqa: E501

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
            '/phone/auto_receptionists/{autoReceptionistId}/ivr', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
