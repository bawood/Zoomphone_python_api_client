# swagger_client.PhoneRolesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role_members**](PhoneRolesApi.md#add_role_members) | **POST** /phone/roles/{roleId}/members | Add members to a role
[**del_role_members**](PhoneRolesApi.md#del_role_members) | **DELETE** /phone/roles/{roleId}/members | Delete members in a role
[**delete_phone_role**](PhoneRolesApi.md#delete_phone_role) | **DELETE** /phone/roles/{roleId} | Delete a phone role
[**duplicate_phone_role**](PhoneRolesApi.md#duplicate_phone_role) | **POST** /phone/roles | Duplicate a phone role
[**get_role_information**](PhoneRolesApi.md#get_role_information) | **GET** /phone/roles/{roleId} | Get role information
[**list_phone_roles**](PhoneRolesApi.md#list_phone_roles) | **GET** /phone/roles | List phone roles
[**list_role_members**](PhoneRolesApi.md#list_role_members) | **GET** /phone/roles/{roleId}/members | List members in a role
[**update_phone_role**](PhoneRolesApi.md#update_phone_role) | **PATCH** /phone/roles/{roleId} | Update a phone role

# **add_role_members**
> add_role_members(role_id, body=body)

Add members to a role

Use this API to add member(s) to a role.  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user.
body = swagger_client.RoleIdMembersBody() # RoleIdMembersBody |  (optional)

try:
    # Add members to a role
    api_instance.add_role_members(role_id, body=body)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->add_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user. | 
 **body** | [**RoleIdMembersBody**](RoleIdMembersBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_role_members**
> del_role_members(role_id, user_ids)

Delete members in a role

Use this API to delete member(s) in a role.  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user.
user_ids = ['user_ids_example'] # list[str] | The user IDs.

try:
    # Delete members in a role
    api_instance.del_role_members(role_id, user_ids)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->del_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user. | 
 **user_ids** | [**list[str]**](str.md)| The user IDs. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_phone_role**
> delete_phone_role(role_id)

Delete a phone role

Use this API to delete a phone [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management).  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user.

try:
    # Delete a phone role
    api_instance.delete_phone_role(role_id)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->delete_phone_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_phone_role**
> InlineResponse20129 duplicate_phone_role(body=body)

Duplicate a phone role

Use this API to duplicate a phone role.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light` 

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneRolesBody() # PhoneRolesBody |  (optional)

try:
    # Duplicate a phone role
    api_response = api_instance.duplicate_phone_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->duplicate_phone_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneRolesBody**](PhoneRolesBody.md)|  | [optional] 

### Return type

[**InlineResponse20129**](InlineResponse20129.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_information**
> InlineResponse200100 get_role_information(role_id)

Get role information

Use this API to get information on a phone [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management).  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Medium`

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | The role ID.

try:
    # Get role information
    api_response = api_instance.get_role_information(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->get_role_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The role ID. | 

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_phone_roles**
> InlineResponse20099 list_phone_roles()

List phone roles

Use this API to get phone roles.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Medium`

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))

try:
    # List phone roles
    api_response = api_instance.list_phone_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->list_phone_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_members**
> InlineResponse200101 list_role_members(role_id, in_role=in_role)

List members in a role

Use this API to get members (not) in a [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Medium`

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user.
in_role = false # bool | Whether the user belongs to the role: default is `false`. (optional) (default to false)

try:
    # List members in a role
    api_response = api_instance.list_role_members(role_id, in_role=in_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->list_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user. | 
 **in_role** | **bool**| Whether the user belongs to the role: default is &#x60;false&#x60;. | [optional] [default to false]

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_role**
> update_phone_role(role_id, body=body)

Update a phone role

Use this API to update a role.  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.PhoneRolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user.
body = swagger_client.RolesRoleIdBody() # RolesRoleIdBody |  (optional)

try:
    # Update a phone role
    api_instance.update_phone_role(role_id, body=body)
except ApiException as e:
    print("Exception when calling PhoneRolesApi->update_phone_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user. | 
 **body** | [**RolesRoleIdBody**](RolesRoleIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

