# swagger_client.BlockedListApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_anumber_to_blocked_list**](BlockedListApi.md#add_anumber_to_blocked_list) | **POST** /phone/blocked_list | Create a blocked list
[**delete_a_blocked_list**](BlockedListApi.md#delete_a_blocked_list) | **DELETE** /phone/blocked_list/{blockedListId} | Delete a blocked list
[**get_a_blocked_list**](BlockedListApi.md#get_a_blocked_list) | **GET** /phone/blocked_list/{blockedListId} | Get blocked list details
[**list_blocked_list**](BlockedListApi.md#list_blocked_list) | **GET** /phone/blocked_list | List blocked lists
[**update_blocked_list**](BlockedListApi.md#update_blocked_list) | **PATCH** /phone/blocked_list/{blockedListId} | Update a blocked list

# **add_anumber_to_blocked_list**
> InlineResponse2013 add_anumber_to_blocked_list(body=body)

Create a blocked list

A Zoom account owner or a user with the admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available. Use this API to create a block list and add a number to the list.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.BlockedListApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneBlockedListBody() # PhoneBlockedListBody |  (optional)

try:
    # Create a blocked list
    api_response = api_instance.add_anumber_to_blocked_list(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedListApi->add_anumber_to_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneBlockedListBody**](PhoneBlockedListBody.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_blocked_list**
> object delete_a_blocked_list(blocked_list_id)

Delete a blocked list

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers).  Use this API to delete a blocked list and therefore removing the associated number from the blocked list. The number will be unblocked after the deletion.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.BlockedListApi(swagger_client.ApiClient(configuration))
blocked_list_id = 'blocked_list_id_example' # str | Unique identifier of the blocked list. This can be retrieved from the List Blocked List API.

try:
    # Delete a blocked list
    api_response = api_instance.delete_a_blocked_list(blocked_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedListApi->delete_a_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocked_list_id** | **str**| Unique identifier of the blocked list. This can be retrieved from the List Blocked List API. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_blocked_list**
> InlineResponse2006 get_a_blocked_list(blocked_list_id)

Get blocked list details

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available. Use this API to get information about a specific blocked list.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:read:admin`     **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.BlockedListApi(swagger_client.ApiClient(configuration))
blocked_list_id = 'blocked_list_id_example' # str | Unique identifier of the blocked list.

try:
    # Get blocked list details
    api_response = api_instance.get_a_blocked_list(blocked_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedListApi->get_a_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocked_list_id** | **str**| Unique identifier of the blocked list. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocked_list**
> InlineResponse2005 list_blocked_list(next_page_token=next_page_token, page_size=page_size)

List blocked lists

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available.  Use this API to list all the blocked lists in an acccount.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.BlockedListApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)

try:
    # List blocked lists
    api_response = api_instance.list_blocked_list(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedListApi->list_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blocked_list**
> object update_blocked_list(blocked_list_id, body=body)

Update a blocked list

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available. Use this API to update the information on the blocked list.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.BlockedListApi(swagger_client.ApiClient(configuration))
blocked_list_id = 'blocked_list_id_example' # str | Unique identifier of the blocked list.
body = swagger_client.BlockedListBlockedListIdBody() # BlockedListBlockedListIdBody |  (optional)

try:
    # Update a blocked list
    api_response = api_instance.update_blocked_list(blocked_list_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedListApi->update_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocked_list_id** | **str**| Unique identifier of the blocked list. | 
 **body** | [**BlockedListBlockedListIdBody**](BlockedListBlockedListIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

