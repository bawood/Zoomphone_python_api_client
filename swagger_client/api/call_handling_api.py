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


class CallHandlingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_call_handling(self, extension_id, setting_type, **kwargs):  # noqa: E501
        """Add a call handling setting  # noqa: E501

        Adds Zoom Phone call handling subsettings for your phone system. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_call_handling(extension_id, setting_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :param str setting_type: The call handling setting type:  * `business_hours`  * `closed_hours`  * `holiday_hours` (required)
        :param SettingsSettingTypeBody2 body:
        :return: InlineResponse20116
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_call_handling_with_http_info(extension_id, setting_type, **kwargs)  # noqa: E501
        else:
            (data) = self.add_call_handling_with_http_info(extension_id, setting_type, **kwargs)  # noqa: E501
            return data

    def add_call_handling_with_http_info(self, extension_id, setting_type, **kwargs):  # noqa: E501
        """Add a call handling setting  # noqa: E501

        Adds Zoom Phone call handling subsettings for your phone system. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_call_handling_with_http_info(extension_id, setting_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :param str setting_type: The call handling setting type:  * `business_hours`  * `closed_hours`  * `holiday_hours` (required)
        :param SettingsSettingTypeBody2 body:
        :return: InlineResponse20116
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extension_id', 'setting_type', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_call_handling" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params or
                params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `add_call_handling`")  # noqa: E501
        # verify the required parameter 'setting_type' is set
        if ('setting_type' not in params or
                params['setting_type'] is None):
            raise ValueError("Missing the required parameter `setting_type` when calling `add_call_handling`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extension_id' in params:
            path_params['extensionId'] = params['extension_id']  # noqa: E501
        if 'setting_type' in params:
            path_params['settingType'] = params['setting_type']  # noqa: E501

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
            '/phone/extension/{extensionId}/call_handling/settings/{settingType}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20116',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_call_handling(self, extension_id, setting_type, **kwargs):  # noqa: E501
        """Delete a call handling setting  # noqa: E501

        Deletes a Zoom Phone's call handling settings. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_call_handling(extension_id, setting_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :param str setting_type: The type of call handling setting:  * `business_hours`  * `closed_hours`  * `holiday_hours` (required)
        :param str call_forwarding_id: The call forwarding's ID. Use this parameter if you pass the `call_forwarding_id` value for the `settingType` parameter.
        :param str holiday_id: The holiday's ID. Use this parameter if you pass the `holiday_id` value for the `settingType` parameter.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_call_handling_with_http_info(extension_id, setting_type, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_call_handling_with_http_info(extension_id, setting_type, **kwargs)  # noqa: E501
            return data

    def delete_call_handling_with_http_info(self, extension_id, setting_type, **kwargs):  # noqa: E501
        """Delete a call handling setting  # noqa: E501

        Deletes a Zoom Phone's call handling settings. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_call_handling_with_http_info(extension_id, setting_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :param str setting_type: The type of call handling setting:  * `business_hours`  * `closed_hours`  * `holiday_hours` (required)
        :param str call_forwarding_id: The call forwarding's ID. Use this parameter if you pass the `call_forwarding_id` value for the `settingType` parameter.
        :param str holiday_id: The holiday's ID. Use this parameter if you pass the `holiday_id` value for the `settingType` parameter.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extension_id', 'setting_type', 'call_forwarding_id', 'holiday_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_call_handling" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params or
                params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `delete_call_handling`")  # noqa: E501
        # verify the required parameter 'setting_type' is set
        if ('setting_type' not in params or
                params['setting_type'] is None):
            raise ValueError("Missing the required parameter `setting_type` when calling `delete_call_handling`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extension_id' in params:
            path_params['extensionId'] = params['extension_id']  # noqa: E501
        if 'setting_type' in params:
            path_params['settingType'] = params['setting_type']  # noqa: E501

        query_params = []
        if 'call_forwarding_id' in params:
            query_params.append(('call_forwarding_id', params['call_forwarding_id']))  # noqa: E501
        if 'holiday_id' in params:
            query_params.append(('holiday_id', params['holiday_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/extension/{extensionId}/call_handling/settings/{settingType}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_call_handling(self, extension_id, **kwargs):  # noqa: E501
        """Get call handling settings  # noqa: E501

        Gets information about a Zoom Phone's call handling settings. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_call_handling(extension_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_call_handling_with_http_info(extension_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_call_handling_with_http_info(extension_id, **kwargs)  # noqa: E501
            return data

    def get_call_handling_with_http_info(self, extension_id, **kwargs):  # noqa: E501
        """Get call handling settings  # noqa: E501

        Gets information about a Zoom Phone's call handling settings. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_call_handling_with_http_info(extension_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extension_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_call_handling" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params or
                params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `get_call_handling`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extension_id' in params:
            path_params['extensionId'] = params['extension_id']  # noqa: E501

        query_params = []

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
            '/phone/extension/{extensionId}/call_handling/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20030',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_call_handling(self, extension_id, setting_type, **kwargs):  # noqa: E501
        """Update a call handling setting  # noqa: E501

        Updates a Zoom Phone's call handling setting. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_call_handling(extension_id, setting_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :param str setting_type: The call handling setting type:  * `business_hours`  * `closed_hours`  * `holiday_hours` (required)
        :param SettingsSettingTypeBody3 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_call_handling_with_http_info(extension_id, setting_type, **kwargs)  # noqa: E501
        else:
            (data) = self.update_call_handling_with_http_info(extension_id, setting_type, **kwargs)  # noqa: E501
            return data

    def update_call_handling_with_http_info(self, extension_id, setting_type, **kwargs):  # noqa: E501
        """Update a call handling setting  # noqa: E501

        Updates a Zoom Phone's call handling setting. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_call_handling_with_http_info(extension_id, setting_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension_id: The extension ID. (required)
        :param str setting_type: The call handling setting type:  * `business_hours`  * `closed_hours`  * `holiday_hours` (required)
        :param SettingsSettingTypeBody3 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extension_id', 'setting_type', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_call_handling" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params or
                params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `update_call_handling`")  # noqa: E501
        # verify the required parameter 'setting_type' is set
        if ('setting_type' not in params or
                params['setting_type'] is None):
            raise ValueError("Missing the required parameter `setting_type` when calling `update_call_handling`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extension_id' in params:
            path_params['extensionId'] = params['extension_id']  # noqa: E501
        if 'setting_type' in params:
            path_params['settingType'] = params['setting_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/extension/{extensionId}/call_handling/settings/{settingType}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)