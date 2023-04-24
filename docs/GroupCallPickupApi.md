# swagger_client.GroupCallPickupApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_gcp**](GroupCallPickupApi.md#add_gcp) | **POST** /phone/group_call_pickup | Add a group call pickup object
[**add_gcp_members**](GroupCallPickupApi.md#add_gcp_members) | **POST** /phone/group_call_pickup/{groupId}/members | Add members to a call pickup group
[**delete_gcp**](GroupCallPickupApi.md#delete_gcp) | **DELETE** /phone/group_call_pickup/{groupId} | Delete group call pickup objects
[**get_gcp**](GroupCallPickupApi.md#get_gcp) | **GET** /phone/group_call_pickup/{groupId} | Get call pickup group by ID
[**list_gcp**](GroupCallPickupApi.md#list_gcp) | **GET** /phone/group_call_pickup | List group call pickup objects
[**list_gcp_members**](GroupCallPickupApi.md#list_gcp_members) | **GET** /phone/group_call_pickup/{groupId}/members | List call pickup group members
[**remove_gcp_members**](GroupCallPickupApi.md#remove_gcp_members) | **DELETE** /phone/group_call_pickup/{groupId}/members/{extensionId} | Remove members from call pickup group
[**update_gcp**](GroupCallPickupApi.md#update_gcp) | **PATCH** /phone/group_call_pickup/{groupId} | Update the group call pickup information

# **add_gcp**
> InlineResponse20128 add_gcp(body=body)

Add a group call pickup object

Use this API to add a [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) instance to the account that has the Zoom Phone license assigned.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneGroupCallPickupBody() # PhoneGroupCallPickupBody |  (optional)

try:
    # Add a group call pickup object
    api_response = api_instance.add_gcp(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->add_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneGroupCallPickupBody**](PhoneGroupCallPickupBody.md)|  | [optional] 

### Return type

[**InlineResponse20128**](InlineResponse20128.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gcp_members**
> add_gcp_members(group_id, body=body)

Add members to a call pickup group

Use this API to add members to the specified [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
body = swagger_client.GroupIdMembersBody() # GroupIdMembersBody |  (optional)

try:
    # Add members to a call pickup group
    api_instance.add_gcp_members(group_id, body=body)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->add_gcp_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **body** | [**GroupIdMembersBody**](GroupIdMembersBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gcp**
> delete_gcp(group_id)

Delete group call pickup objects

Use this API to remove a [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # Delete group call pickup objects
    api_instance.delete_gcp(group_id)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->delete_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp**
> InlineResponse20097 get_gcp(group_id)

Get call pickup group by ID

Use this API to retrieve information on a specific [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object in an account.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # Get call pickup group by ID
    api_response = api_instance.get_gcp(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->get_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gcp**
> InlineResponse20096 list_gcp(page_size=page_size, next_page_token=next_page_token, site_id=site_id)

List group call pickup objects

Use this API to retrieve a list of [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) objects in an account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
site_id = 'site_id_example' # str | Unique identifier of the site. This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. (optional)

try:
    # List group call pickup objects
    api_response = api_instance.list_gcp(page_size=page_size, next_page_token=next_page_token, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->list_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **site_id** | **str**| Unique identifier of the site. This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. | [optional] 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gcp_members**
> InlineResponse20098 list_gcp_members(group_id, page_size=page_size, next_page_token=next_page_token, site_id=site_id, extension_type=extension_type)

List call pickup group members

Use this API to retrieve members of a [call pickup group](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) in an account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
site_id = 'site_id_example' # str | Unique identifier of the site. (optional)
extension_type = 'extension_type_example' # str | Type of the assignee. (optional)

try:
    # List call pickup group members
    api_response = api_instance.list_gcp_members(group_id, page_size=page_size, next_page_token=next_page_token, site_id=site_id, extension_type=extension_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->list_gcp_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **site_id** | **str**| Unique identifier of the site. | [optional] 
 **extension_type** | **str**| Type of the assignee. | [optional] 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_gcp_members**
> remove_gcp_members(group_id, extension_id)

Remove members from call pickup group

Use this API to remove member from the [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
extension_id = 'extension_id_example' # str | 

try:
    # Remove members from call pickup group
    api_instance.remove_gcp_members(group_id, extension_id)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->remove_gcp_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **extension_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp**
> update_gcp(group_id, body=body)

Update the group call pickup information

Use this API to update a specific [Group Call Pickup](https://support.zoom.us/hc/en-us/articles/360060107472-Setting-up-and-using-group-call-pickup) object information.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.GroupCallPickupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
body = swagger_client.GroupCallPickupGroupIdBody() # GroupCallPickupGroupIdBody |  (optional)

try:
    # Update the group call pickup information
    api_instance.update_gcp(group_id, body=body)
except ApiException as e:
    print("Exception when calling GroupCallPickupApi->update_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **body** | [**GroupCallPickupGroupIdBody**](GroupCallPickupGroupIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

