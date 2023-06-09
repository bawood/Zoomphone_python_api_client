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


class GroupCallPickupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_gcp(self, **kwargs):  # noqa: E501
        """Add a group call pickup object  # noqa: E501

        Use this API to add a [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) instance to the account that has the Zoom Phone license assigned.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_gcp(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PhoneGroupCallPickupBody body:
        :return: InlineResponse20128
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_gcp_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_gcp_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_gcp_with_http_info(self, **kwargs):  # noqa: E501
        """Add a group call pickup object  # noqa: E501

        Use this API to add a [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) instance to the account that has the Zoom Phone license assigned.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_gcp_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PhoneGroupCallPickupBody body:
        :return: InlineResponse20128
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
                    " to method add_gcp" % key
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
            '/phone/group_call_pickup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20128',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_gcp_members(self, group_id, **kwargs):  # noqa: E501
        """Add members to a call pickup group  # noqa: E501

        Use this API to add members to the specified [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_gcp_members(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param GroupIdMembersBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_gcp_members_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_gcp_members_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def add_gcp_members_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Add members to a call pickup group  # noqa: E501

        Use this API to add members to the specified [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_gcp_members_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param GroupIdMembersBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_gcp_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `add_gcp_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

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
            '/phone/group_call_pickup/{groupId}/members', 'POST',
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

    def delete_gcp(self, group_id, **kwargs):  # noqa: E501
        """Delete group call pickup objects  # noqa: E501

        Use this API to remove a [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_gcp(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_gcp_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_gcp_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def delete_gcp_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Delete group call pickup objects  # noqa: E501

        Use this API to remove a [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_gcp_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_gcp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `delete_gcp`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/group_call_pickup/{groupId}', 'DELETE',
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

    def get_gcp(self, group_id, **kwargs):  # noqa: E501
        """Get call pickup group by ID  # noqa: E501

        Use this API to retrieve information on a specific [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object in an account.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gcp(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :return: InlineResponse20097
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gcp_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gcp_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def get_gcp_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Get call pickup group by ID  # noqa: E501

        Use this API to retrieve information on a specific [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object in an account.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gcp_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :return: InlineResponse20097
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gcp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_gcp`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

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
            '/phone/group_call_pickup/{groupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20097',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_gcp(self, **kwargs):  # noqa: E501
        """List group call pickup objects  # noqa: E501

        Use this API to retrieve a list of [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) objects in an account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_gcp(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned within a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str site_id: Unique identifier of the site. This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API.
        :return: InlineResponse20096
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_gcp_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_gcp_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_gcp_with_http_info(self, **kwargs):  # noqa: E501
        """List group call pickup objects  # noqa: E501

        Use this API to retrieve a list of [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) objects in an account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_gcp_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned within a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str site_id: Unique identifier of the site. This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API.
        :return: InlineResponse20096
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'next_page_token', 'site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_gcp" % key
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
        if 'site_id' in params:
            query_params.append(('site_id', params['site_id']))  # noqa: E501

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
            '/phone/group_call_pickup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20096',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_gcp_members(self, group_id, **kwargs):  # noqa: E501
        """List call pickup group members  # noqa: E501

        Use this API to retrieve members of a [call pickup group](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) in an account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_gcp_members(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param int page_size: The number of records returned within a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str site_id: Unique identifier of the site.
        :param str extension_type: Type of the assignee.
        :return: InlineResponse20098
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_gcp_members_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_gcp_members_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def list_gcp_members_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List call pickup group members  # noqa: E501

        Use this API to retrieve members of a [call pickup group](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) in an account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_gcp_members_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param int page_size: The number of records returned within a single API call.
        :param str next_page_token: The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :param str site_id: Unique identifier of the site.
        :param str extension_type: Type of the assignee.
        :return: InlineResponse20098
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'page_size', 'next_page_token', 'site_id', 'extension_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_gcp_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `list_gcp_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page_token' in params:
            query_params.append(('next_page_token', params['next_page_token']))  # noqa: E501
        if 'site_id' in params:
            query_params.append(('site_id', params['site_id']))  # noqa: E501
        if 'extension_type' in params:
            query_params.append(('extension_type', params['extension_type']))  # noqa: E501

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
            '/phone/group_call_pickup/{groupId}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20098',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_gcp_members(self, group_id, extension_id, **kwargs):  # noqa: E501
        """Remove members from call pickup group  # noqa: E501

        Use this API to remove member from the [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_gcp_members(group_id, extension_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param str extension_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_gcp_members_with_http_info(group_id, extension_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_gcp_members_with_http_info(group_id, extension_id, **kwargs)  # noqa: E501
            return data

    def remove_gcp_members_with_http_info(self, group_id, extension_id, **kwargs):  # noqa: E501
        """Remove members from call pickup group  # noqa: E501

        Use this API to remove member from the [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_gcp_members_with_http_info(group_id, extension_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param str extension_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'extension_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_gcp_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `remove_gcp_members`")  # noqa: E501
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params or
                params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `remove_gcp_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501
        if 'extension_id' in params:
            path_params['extensionId'] = params['extension_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phone/group_call_pickup/{groupId}/members/{extensionId}', 'DELETE',
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

    def update_gcp(self, group_id, **kwargs):  # noqa: E501
        """Update the group call pickup information  # noqa: E501

        Use this API to update a specific [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object information.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_gcp(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param GroupCallPickupGroupIdBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_gcp_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_gcp_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def update_gcp_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Update the group call pickup information  # noqa: E501

        Use this API to update a specific [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object information.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_gcp_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :param GroupCallPickupGroupIdBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_gcp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `update_gcp`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

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
            '/phone/group_call_pickup/{groupId}', 'PATCH',
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
