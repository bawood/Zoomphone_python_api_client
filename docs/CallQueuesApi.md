# swagger_client.CallQueuesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cq_policy_sub_setting**](CallQueuesApi.md#add_cq_policy_sub_setting) | **POST** /phone/call_queues/{callQueueId}/policies/{policyType} | Add a policy setting to a call queue
[**add_members_to_call_queue**](CallQueuesApi.md#add_members_to_call_queue) | **POST** /phone/call_queues/{callQueueId}/members | Add members to a call queue
[**assign_phone_to_call_queue**](CallQueuesApi.md#assign_phone_to_call_queue) | **POST** /phone/call_queues/{callQueueId}/phone_numbers | Assign numbers to a call queue
[**change_call_queue_manager**](CallQueuesApi.md#change_call_queue_manager) | **PUT** /phone/call_queues/{callQueueId}/manager | Change call queue manager
[**create_call_queue**](CallQueuesApi.md#create_call_queue) | **POST** /phone/call_queues | Create a call queue
[**delete_a_call_queue**](CallQueuesApi.md#delete_a_call_queue) | **DELETE** /phone/call_queues/{callQueueId} | Delete a call queue
[**get_a_call_queue**](CallQueuesApi.md#get_a_call_queue) | **GET** /phone/call_queues/{callQueueId} | Get call queue details
[**get_call_queue_recordings**](CallQueuesApi.md#get_call_queue_recordings) | **GET** /phone/call_queues/{callQueueId}/recordings | Get call queue recordings
[**list_call_queue_members**](CallQueuesApi.md#list_call_queue_members) | **GET** /phone/call_queues/{callQueueId}/members | List call queue members
[**list_call_queues**](CallQueuesApi.md#list_call_queues) | **GET** /phone/call_queues | List call queues
[**remove_cq_policy_sub_setting**](CallQueuesApi.md#remove_cq_policy_sub_setting) | **DELETE** /phone/call_queues/{callQueueId}/policies/{policyType} | Delete a CQ policy setting
[**un_assign_phone_num_call_queue**](CallQueuesApi.md#un_assign_phone_num_call_queue) | **DELETE** /phone/call_queues/{callQueueId}/phone_numbers/{phoneNumberId} | Unassign a phone number
[**unassign_a_phone_num_call_queue**](CallQueuesApi.md#unassign_a_phone_num_call_queue) | **DELETE** /phone/call_queues/{callQueueId}/phone_numbers | Unassign all phone numbers
[**unassign_all_members**](CallQueuesApi.md#unassign_all_members) | **DELETE** /phone/call_queues/{callQueueId}/members | Unassign all members
[**unassign_member_from_call_queue**](CallQueuesApi.md#unassign_member_from_call_queue) | **DELETE** /phone/call_queues/{callQueueId}/members/{memberId} | Unassign a member
[**update_call_queue**](CallQueuesApi.md#update_call_queue) | **PATCH** /phone/call_queues/{callQueueId} | Update call queue details
[**update_cq_policy_sub_setting**](CallQueuesApi.md#update_cq_policy_sub_setting) | **PATCH** /phone/call_queues/{callQueueId}/policies/{policyType} | Update a CQ policy setting

# **add_cq_policy_sub_setting**
> InlineResponse2016 add_cq_policy_sub_setting(call_queue_id, policy_type, body=body)

Add a policy setting to a call queue

Use this API to add the policy sub-setting for a specific [call queue](https://support.zoom.us/hc/en-us/articles/360021524831) according to the `policyType`. For example, you can use this API to set up shared access members.   **Prerequisites:**  * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | The call queue ID, retrievable the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API.
policy_type = 'policy_type_example' # str | The policy sub-setting item that you wish to add. Allowed values: `voice_mail`.
body = swagger_client.PoliciesPolicyTypeBody2() # PoliciesPolicyTypeBody2 |  (optional)

try:
    # Add a policy setting to a call queue
    api_response = api_instance.add_cq_policy_sub_setting(call_queue_id, policy_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->add_cq_policy_sub_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| The call queue ID, retrievable the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API. | 
 **policy_type** | **str**| The policy sub-setting item that you wish to add. Allowed values: &#x60;voice_mail&#x60;. | 
 **body** | [**PoliciesPolicyTypeBody2**](PoliciesPolicyTypeBody2.md)|  | [optional] 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_members_to_call_queue**
> object add_members_to_call_queue(call_queue_id, body=body)

Add members to a call queue

Add phone users and/or [common areas](https://support.zoom.us/hc/articles/4481136653709) as members to a specific call queue.  **Prerequisites:** * Pro or higher account plan. * Zoom Phone license  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue.
body = swagger_client.CallQueueIdMembersBody() # CallQueueIdMembersBody |  (optional)

try:
    # Add members to a call queue
    api_response = api_instance.add_members_to_call_queue(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->add_members_to_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. | 
 **body** | [**CallQueueIdMembersBody**](CallQueueIdMembersBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_to_call_queue**
> object assign_phone_to_call_queue(call_queue_id, body=body)

Assign numbers to a call queue

After [buying phone number(s)](https://support.zoom.us/hc/en-us/articles/360020808292#h_007ec8c2-0914-4265-8351-96ab23efa3ad), you can assign it, allowing callers to directly dial a number to reach a [call queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues).   **Prerequisites:**  * Pro or higher account plan. * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue.
body = swagger_client.CallQueueIdPhoneNumbersBody() # CallQueueIdPhoneNumbersBody |  (optional)

try:
    # Assign numbers to a call queue
    api_response = api_instance.assign_phone_to_call_queue(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->assign_phone_to_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. | 
 **body** | [**CallQueueIdPhoneNumbersBody**](CallQueueIdPhoneNumbersBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_call_queue_manager**
> object change_call_queue_manager(call_queue_id, body=body)

Change call queue manager

A call queue manager has the privileges to manage the call queue's voicemail inbox and recordings, change all call queue settings and call queue policy settings.   Use this API to to set another phone user as the [call queue manager](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues#h_db06854b-e6a3-4afe-ba15-baf58f31f90c).   **Prerequisites:** * Pro or higher account plan. * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:write:admin`     **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue.
body = swagger_client.CallQueueIdManagerBody() # CallQueueIdManagerBody |  (optional)

try:
    # Change call queue manager
    api_response = api_instance.change_call_queue_manager(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->change_call_queue_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. | 
 **body** | [**CallQueueIdManagerBody**](CallQueueIdManagerBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_call_queue**
> InlineResponse2015 create_call_queue(body=body)

Create a call queue

[Creates a call queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues#h_e81faeeb-9184-429a-aaea-df49ff5ff413). Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service, and so on.  You can add phone users or common areas to call queues.  **Prerequisites:**  * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneCallQueuesBody() # PhoneCallQueuesBody |  (optional)

try:
    # Create a call queue
    api_response = api_instance.create_call_queue(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->create_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneCallQueuesBody**](PhoneCallQueuesBody.md)|  | [optional] 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_call_queue**
> object delete_a_call_queue(call_queue_id)

Delete a call queue

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.  Use this API to delete a Call Queue.   **Prerequisites:**  * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the call queue.

try:
    # Delete a call queue
    api_response = api_instance.delete_a_call_queue(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->delete_a_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the call queue. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_call_queue**
> InlineResponse20011 get_a_call_queue(call_queue_id)

Get call queue details

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.  Use this API to get information on a specific Call Queue.    **Prerequisites:**  * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:read:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue. This can be retrieved from [List Call Queues API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-call-queues/listcallqueues).

try:
    # Get call queue details
    api_response = api_instance.get_a_call_queue(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->get_a_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. This can be retrieved from [List Call Queues API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-call-queues/listcallqueues). | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_queue_recordings**
> InlineResponse20013 get_call_queue_recordings(call_queue_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)

Get call queue recordings

Use this API to view [call recordings](https://support.zoom.us/hc/en-us/articles/360038521091#h_cbc9f2a3-e06c-4daa-83d4-ddbceef9c77b) from the call queue.   **Prerequisites:**  * Pro or higher account with Zoom Phone license. * [Automatic call recordings](https://support.zoom.us/hc/en-us/articles/360033511872#h_fcb297bb-14e8-4094-91ca-dc61e1a18734) must be enabled in the Policy Settings for call queues.   **Scope:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`    

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data. The month defined should fall within the last six months. If unspecified, returns data within the 24 hours. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)

try:
    # Get call queue recordings
    api_response = api_instance.get_call_queue_recordings(call_queue_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->get_call_queue_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data. The month defined should fall within the last six months. If unspecified, returns data within the 24 hours. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_queue_members**
> InlineResponse20012 list_call_queue_members(call_queue_id)

List call queue members

Lists the call queue members.   **Prerequisites:**  * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:read:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | The call queue ID that is retrievable from the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API.

try:
    # List call queue members
    api_response = api_instance.list_call_queue_members(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->list_call_queue_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| The call queue ID that is retrievable from the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_queues**
> InlineResponse20010 list_call_queues(next_page_token=next_page_token, page_size=page_size, site_id=site_id, cost_center=cost_center, department=department)

List call queues

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.  Use this API to list Call queues.   **Prerequisites:**  * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:read:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned from a single API call. (optional) (default to 30)
site_id = 'site_id_example' # str | Unique identifier of the site. Get it from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. (optional)
cost_center = 'cost_center_example' # str | The call queue's cost center. (optional)
department = 'department_example' # str | The call queue's department. (optional)

try:
    # List call queues
    api_response = api_instance.list_call_queues(next_page_token=next_page_token, page_size=page_size, site_id=site_id, cost_center=cost_center, department=department)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->list_call_queues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned from a single API call. | [optional] [default to 30]
 **site_id** | **str**| Unique identifier of the site. Get it from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. | [optional] 
 **cost_center** | **str**| The call queue&#x27;s cost center. | [optional] 
 **department** | **str**| The call queue&#x27;s department. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cq_policy_sub_setting**
> object remove_cq_policy_sub_setting(call_queue_id, policy_type, shared_ids)

Delete a CQ policy setting

Use this API to remove the policy sub-setting for a specific [call queue](https://support.zoom.us/hc/en-us/articles/360021524831) according to the `policyType`. For example, you can use this API to remove shared access members.   **Prerequisites:**  * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | The call queue ID, retrievable from the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API.
policy_type = 'policy_type_example' # str | Corresponds to tbe policy sub-setting item you wish to remove. Allowed values: `voice_mail`
shared_ids = ['shared_ids_example'] # list[str] | Comma separated list of shared IDs to remove. The number is limited to the minimum value of 10 or the number of allowed access members account setting.

try:
    # Delete a CQ policy setting
    api_response = api_instance.remove_cq_policy_sub_setting(call_queue_id, policy_type, shared_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->remove_cq_policy_sub_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| The call queue ID, retrievable from the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API. | 
 **policy_type** | **str**| Corresponds to tbe policy sub-setting item you wish to remove. Allowed values: &#x60;voice_mail&#x60; | 
 **shared_ids** | [**list[str]**](str.md)| Comma separated list of shared IDs to remove. The number is limited to the minimum value of 10 or the number of allowed access members account setting. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_assign_phone_num_call_queue**
> object un_assign_phone_num_call_queue(call_queue_id, phone_number_id)

Unassign a phone number

After assigning a phone number, you can unbind it if you don't want it to be assigned to a [Call Queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues). Use this API to unbind a phone number from a Call Queue. After successful unbinding, the number will appear in the [Unassigned tab](https://zoom.us/signin#/numbers/unassigned).   **Prerequisites:** * Pro or higher account palan * Account owner or admin permissions * Zoom Phone license   **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue. This can be retrieved from the List Call Queues API.
phone_number_id = 'phone_number_id_example' # str | Unique identifier of the Phone Number. 

try:
    # Unassign a phone number
    api_response = api_instance.un_assign_phone_num_call_queue(call_queue_id, phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->un_assign_phone_num_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. This can be retrieved from the List Call Queues API. | 
 **phone_number_id** | **str**| Unique identifier of the Phone Number.  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_a_phone_num_call_queue**
> object unassign_a_phone_num_call_queue(call_queue_id)

Unassign all phone numbers

Use this API to unbind all phone numbers that are assigned to a [Call Queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues) After successful unbinding, the numbers will appear in the [Unassigned tab](https://zoom.us/signin#/numbers/unassigned).  If you only need to unassign a specific phone number, use the Unassign a Phone Number API instead.   **Prerequisites:** * Pro or higher account palan * Account owner or admin permissions * Zoom Phone license   **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue. This can be retrieved from List Call Queues API.

try:
    # Unassign all phone numbers
    api_response = api_instance.unassign_a_phone_num_call_queue(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->unassign_a_phone_num_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. This can be retrieved from List Call Queues API. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_all_members**
> object unassign_all_members(call_queue_id)

Unassign all members

Removes all members from a call queue who were previously assigned to that call queue. The members could be phone users or [common areas](https://support.zoom.us/hc/articles/4481136653709).  **Prerequisites:**  * Pro or higher account plan. * Zoom Phone license  **Scopes:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | 

try:
    # Unassign all members
    api_response = api_instance.unassign_all_members(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->unassign_all_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_member_from_call_queue**
> object unassign_member_from_call_queue(call_queue_id, member_id)

Unassign a member

Removes a member who was previously added to a call queue. The member could be a phone user or common area. Note that you cannot use this API to unassign a call queue manager.   **Prerequisites:**  * Pro or higher account plan. * Zoom Phone license  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue from which the member needs to be unassigned.
member_id = 'member_id_example' # str | Unique identifier of the member who needs to be unassigned.

try:
    # Unassign a member
    api_response = api_instance.unassign_member_from_call_queue(call_queue_id, member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->unassign_member_from_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue from which the member needs to be unassigned. | 
 **member_id** | **str**| Unique identifier of the member who needs to be unassigned. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_queue**
> object update_call_queue(call_queue_id, body=body)

Update call queue details

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.  Use this API to update information of a specific Call Queue.   **Prerequisites:**  * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license  **Scopes:** `phone:write:admin`     **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique identifier of the Call Queue.
body = swagger_client.CallQueuesCallQueueIdBody() # CallQueuesCallQueueIdBody |  (optional)

try:
    # Update call queue details
    api_response = api_instance.update_call_queue(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->update_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique identifier of the Call Queue. | 
 **body** | [**CallQueuesCallQueueIdBody**](CallQueuesCallQueueIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cq_policy_sub_setting**
> object update_cq_policy_sub_setting(call_queue_id, policy_type, body=body)

Update a CQ policy setting

Use this API to update the policy sub-setting for a specific [call queue](https://support.zoom.us/hc/en-us/articles/360021524831) according to the `policyType`. For example, you can use this API to update shared access members.  **Prerequisites:**  * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | The call queue ID, retrievable from the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API.
policy_type = 'policy_type_example' # str | Corresponds to the policy sub-setting item you wish to update. Allowed values: `voice_mail`.
body = swagger_client.PoliciesPolicyTypeBody3() # PoliciesPolicyTypeBody3 |  (optional)

try:
    # Update a CQ policy setting
    api_response = api_instance.update_cq_policy_sub_setting(call_queue_id, policy_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallQueuesApi->update_cq_policy_sub_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| The call queue ID, retrievable from the [List Call Queues](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Call-Queues/operation/listCallQueues) API. | 
 **policy_type** | **str**| Corresponds to the policy sub-setting item you wish to update. Allowed values: &#x60;voice_mail&#x60;. | 
 **body** | [**PoliciesPolicyTypeBody3**](PoliciesPolicyTypeBody3.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

