# swagger_client.MonitoringGroupsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members**](MonitoringGroupsApi.md#add_members) | **POST** /phone/monitoring_groups/{monitoringGroupId}/monitor_members | Add members to a monitoring group
[**create_monitoring_group**](MonitoringGroupsApi.md#create_monitoring_group) | **POST** /phone/monitoring_groups | Create a monitoring group
[**delete_monitoring_group**](MonitoringGroupsApi.md#delete_monitoring_group) | **DELETE** /phone/monitoring_groups/{monitoringGroupId} | Delete a monitoring group
[**get_monitoring_group_by_id**](MonitoringGroupsApi.md#get_monitoring_group_by_id) | **GET** /phone/monitoring_groups/{monitoringGroupId} | Get monitoring group by ID
[**list_members**](MonitoringGroupsApi.md#list_members) | **GET** /phone/monitoring_groups/{monitoringGroupId}/monitor_members | Get members of a monitoring group
[**list_monitoring_group**](MonitoringGroupsApi.md#list_monitoring_group) | **GET** /phone/monitoring_groups | Get a list of monitoring groups on an account
[**remove_member**](MonitoringGroupsApi.md#remove_member) | **DELETE** /phone/monitoring_groups/{monitoringGroupId}/monitor_members/{memberExtensionId} | Remove a member from a monitoring group
[**remove_members**](MonitoringGroupsApi.md#remove_members) | **DELETE** /phone/monitoring_groups/{monitoringGroupId}/monitor_members | Remove all monitors or monitored members from a monitoring group
[**update_monitoring_group**](MonitoringGroupsApi.md#update_monitoring_group) | **PATCH** /phone/monitoring_groups/{monitoringGroupId} | Update a monitoring group

# **add_members**
> object add_members(member_type, monitoring_group_id, body=body)

Add members to a monitoring group

Use this API to add members to a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
member_type = 'member_type_example' # str | Member type
monitoring_group_id = 'monitoring_group_id_example' # str | Monitoring group ID.
body = ['body_example'] # list[str] |  (optional)

try:
    # Add members to a monitoring group
    api_response = api_instance.add_members(member_type, monitoring_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->add_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_type** | **str**| Member type | 
 **monitoring_group_id** | **str**| Monitoring group ID. | 
 **body** | [**list[str]**](str.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_monitoring_group**
> InlineResponse20119 create_monitoring_group(body=body)

Create a monitoring group

Use this API to create a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneMonitoringGroupsBody() # PhoneMonitoringGroupsBody |  (optional)

try:
    # Create a monitoring group
    api_response = api_instance.create_monitoring_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->create_monitoring_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneMonitoringGroupsBody**](PhoneMonitoringGroupsBody.md)|  | [optional] 

### Return type

[**InlineResponse20119**](InlineResponse20119.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitoring_group**
> object delete_monitoring_group(monitoring_group_id)

Delete a monitoring group

Use this API to delete a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
monitoring_group_id = 'monitoring_group_id_example' # str | Monitoring group ID.

try:
    # Delete a monitoring group
    api_response = api_instance.delete_monitoring_group(monitoring_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->delete_monitoring_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_group_id** | **str**| Monitoring group ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_group_by_id**
> InlineResponse20041 get_monitoring_group_by_id(monitoring_group_id)

Get monitoring group by ID

Use this API to return a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711) for the specified ID.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
monitoring_group_id = 'monitoring_group_id_example' # str | Monitoring group ID.

try:
    # Get monitoring group by ID
    api_response = api_instance.get_monitoring_group_by_id(monitoring_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->get_monitoring_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_group_id** | **str**| Monitoring group ID. | 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> InlineResponse20042 list_members(monitoring_group_id, member_type, page_size=page_size, next_page_token=next_page_token)

Get members of a monitoring group

Use this API to return members list of a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711).  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
monitoring_group_id = 'monitoring_group_id_example' # str | Monitoring group ID.
member_type = 'member_type_example' # str | Member type
page_size = 56 # int | The size of the page. (optional)
next_page_token = 'next_page_token_example' # str | The current page number of returned records. (optional)

try:
    # Get members of a monitoring group
    api_response = api_instance.list_members(monitoring_group_id, member_type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->list_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_group_id** | **str**| Monitoring group ID. | 
 **member_type** | **str**| Member type | 
 **page_size** | **int**| The size of the page. | [optional] 
 **next_page_token** | **str**| The current page number of returned records. | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monitoring_group**
> InlineResponse20040 list_monitoring_group(type=type, site_id=site_id, page_size=page_size, next_page_token=next_page_token)

Get a list of monitoring groups on an account

Use this API to return an account's [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711) list.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
type = 56 # int | Monitoring group's type. (optional)
site_id = 'site_id_example' # str | Unique identifier of the monitoring group's site. (optional)
page_size = 56 # int | The size of the page. (optional)
next_page_token = 'next_page_token_example' # str | The current page number of returned records. (optional)

try:
    # Get a list of monitoring groups on an account
    api_response = api_instance.list_monitoring_group(type=type, site_id=site_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->list_monitoring_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| Monitoring group&#x27;s type. | [optional] 
 **site_id** | **str**| Unique identifier of the monitoring group&#x27;s site. | [optional] 
 **page_size** | **int**| The size of the page. | [optional] 
 **next_page_token** | **str**| The current page number of returned records. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member**
> object remove_member(monitoring_group_id, member_extension_id, member_type=member_type)

Remove a member from a monitoring group

Use this API to remove a member from a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
monitoring_group_id = 'monitoring_group_id_example' # str | Monitoring group ID.
member_extension_id = 'member_extension_id_example' # str | Member's extension ID.
member_type = 'member_type_example' # str | Member type (optional)

try:
    # Remove a member from a monitoring group
    api_response = api_instance.remove_member(monitoring_group_id, member_extension_id, member_type=member_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->remove_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_group_id** | **str**| Monitoring group ID. | 
 **member_extension_id** | **str**| Member&#x27;s extension ID. | 
 **member_type** | **str**| Member type | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members**
> object remove_members(monitoring_group_id, member_type)

Remove all monitors or monitored members from a monitoring group

Use this API to remove all monitor or monitored members from a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
monitoring_group_id = 'monitoring_group_id_example' # str | Monitoring group ID.
member_type = 'member_type_example' # str | Member type

try:
    # Remove all monitors or monitored members from a monitoring group
    api_response = api_instance.remove_members(monitoring_group_id, member_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->remove_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_group_id** | **str**| Monitoring group ID. | 
 **member_type** | **str**| Member type | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monitoring_group**
> object update_monitoring_group(monitoring_group_id, body=body)

Update a monitoring group

Use this API to update a [Monitoring Group](https://support.zoom.us/hc/en-us/articles/360044804711).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.MonitoringGroupsApi(swagger_client.ApiClient(configuration))
monitoring_group_id = 'monitoring_group_id_example' # str | Monitoring group ID.
body = swagger_client.MonitoringGroupsMonitoringGroupIdBody() # MonitoringGroupsMonitoringGroupIdBody |  (optional)

try:
    # Update a monitoring group
    api_response = api_instance.update_monitoring_group(monitoring_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringGroupsApi->update_monitoring_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_group_id** | **str**| Monitoring group ID. | 
 **body** | [**MonitoringGroupsMonitoringGroupIdBody**](MonitoringGroupsMonitoringGroupIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

