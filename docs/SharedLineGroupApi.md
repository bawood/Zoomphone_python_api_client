# swagger_client.SharedLineGroupApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_to_shared_line_group**](SharedLineGroupApi.md#add_members_to_shared_line_group) | **POST** /phone/shared_line_groups/{sharedLineGroupId}/members | Add members to a shared line group
[**add_slg_policy_sub_setting**](SharedLineGroupApi.md#add_slg_policy_sub_setting) | **POST** /phone/shared_line_groups/{sharedLineGroupId}/policy/{policyType} | Add a policy setting to a shared line group
[**assign_phone_numbers_slg**](SharedLineGroupApi.md#assign_phone_numbers_slg) | **POST** /phone/shared_line_groups/{sharedLineGroupId}/phone_numbers | Assign phone numbers
[**create_a_shared_line_group**](SharedLineGroupApi.md#create_a_shared_line_group) | **POST** /phone/shared_line_groups | Create a shared line group
[**delete_a_member_slg**](SharedLineGroupApi.md#delete_a_member_slg) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/members/{memberId} | Unassign a member from a shared line group
[**delete_a_phone_number_slg**](SharedLineGroupApi.md#delete_a_phone_number_slg) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/phone_numbers/{phoneNumberId} | Unassign a phone number
[**delete_a_shared_line_group**](SharedLineGroupApi.md#delete_a_shared_line_group) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId} | Delete a shared line group
[**delete_members_of_slg**](SharedLineGroupApi.md#delete_members_of_slg) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/members | Unassign members from a shared line group
[**delete_phone_numbers_slg**](SharedLineGroupApi.md#delete_phone_numbers_slg) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/phone_numbers | Unassign all phone numbers
[**get_a_shared_line_group**](SharedLineGroupApi.md#get_a_shared_line_group) | **GET** /phone/shared_line_groups/{sharedLineGroupId} | Get a shared line group
[**list_shared_line_groups**](SharedLineGroupApi.md#list_shared_line_groups) | **GET** /phone/shared_line_groups | List shared line groups
[**remove_slg_policy_sub_setting**](SharedLineGroupApi.md#remove_slg_policy_sub_setting) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/policy/{policyType} | Delete an SLG policy setting
[**update_a_shared_line_group**](SharedLineGroupApi.md#update_a_shared_line_group) | **PATCH** /phone/shared_line_groups/{sharedLineGroupId} | Update a shared line group
[**update_slg_policy_sub_setting**](SharedLineGroupApi.md#update_slg_policy_sub_setting) | **PATCH** /phone/shared_line_groups/{sharedLineGroupId}/policy/{policyType} | Update an SLG policy setting

# **add_members_to_shared_line_group**
> object add_members_to_shared_line_group(shared_line_group_id, body=body)

Add members to a shared line group

[Adds members](https://support.zoom.us/hc/en-us/articles/360038850792-Setting-up-shared-line-groups#h_7cb42370-48f6-4a8f-84f4-c6eee4d9f0ca) to a shared line group. A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common areas. This gives members of the shared line group access to the group's direct phone number and voicemail.  Note that a member can only be added to one shared line group.   **Prerequisites:** <br> * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges   **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the shared line group.
body = swagger_client.SharedLineGroupIdMembersBody() # SharedLineGroupIdMembersBody |  (optional)

try:
    # Add members to a shared line group
    api_response = api_instance.add_members_to_shared_line_group(shared_line_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->add_members_to_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the shared line group. | 
 **body** | [**SharedLineGroupIdMembersBody**](SharedLineGroupIdMembersBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_slg_policy_sub_setting**
> InlineResponse20123 add_slg_policy_sub_setting(shared_line_group_id, policy_type, body=body)

Add a policy setting to a shared line group

Adds the policy sub-setting for a specific [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) according to the `policyType`. For example, you can use this API to set up shared access members.   **Prerequisites:**  * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The shared line group ID.
policy_type = 'policy_type_example' # str | This field corresponds to the policy item you wish to add. Allowed values: `voice_mail`.
body = swagger_client.PolicyPolicyTypeBody() # PolicyPolicyTypeBody |  (optional)

try:
    # Add a policy setting to a shared line group
    api_response = api_instance.add_slg_policy_sub_setting(shared_line_group_id, policy_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->add_slg_policy_sub_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The shared line group ID. | 
 **policy_type** | **str**| This field corresponds to the policy item you wish to add. Allowed values: &#x60;voice_mail&#x60;. | 
 **body** | [**PolicyPolicyTypeBody**](PolicyPolicyTypeBody.md)|  | [optional] 

### Return type

[**InlineResponse20123**](InlineResponse20123.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_numbers_slg**
> assign_phone_numbers_slg(shared_line_group_id, body=body)

Assign phone numbers

Assigns phone numbers to a shared line groups. These direct phone numbers will be shared among members of the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792-Setting-up-shared-line-groups).  **Prerequisites:**   * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the shared line group.
body = swagger_client.SharedLineGroupIdPhoneNumbersBody() # SharedLineGroupIdPhoneNumbersBody |  (optional)

try:
    # Assign phone numbers
    api_instance.assign_phone_numbers_slg(shared_line_group_id, body=body)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->assign_phone_numbers_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the shared line group. | 
 **body** | [**SharedLineGroupIdPhoneNumbersBody**](SharedLineGroupIdPhoneNumbersBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_a_shared_line_group**
> object create_a_shared_line_group(body=body)

Create a shared line group

Creates a shared line group. A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common areas. This gives members of the shared line group access to the group's direct phone number and voicemail.   **Prerequisites:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneSharedLineGroupsBody() # PhoneSharedLineGroupsBody |  (optional)

try:
    # Create a shared line group
    api_response = api_instance.create_a_shared_line_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->create_a_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneSharedLineGroupsBody**](PhoneSharedLineGroupsBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_member_slg**
> delete_a_member_slg(shared_line_group_id, member_id)

Unassign a member from a shared line group

Unassigns **a specific member** from a shared line group. Members of the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) have access to the group's phone number and voicemail.   **Prerequisites:**   * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the shared line group from which you would like to remove a member.
member_id = 'member_id_example' # str | The unique identifier of the member who is to be removed.

try:
    # Unassign a member from a shared line group
    api_instance.delete_a_member_slg(shared_line_group_id, member_id)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->delete_a_member_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the shared line group from which you would like to remove a member. | 
 **member_id** | **str**| The unique identifier of the member who is to be removed. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_phone_number_slg**
> delete_a_phone_number_slg(shared_line_group_id, phone_number_id)

Unassign a phone number

Unassigns a specific phone number that was assigned to the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792-Setting-up-shared-line-groups). **Prerequisites:**   * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the shared line group from which you would like to unassign a phone number.
phone_number_id = 'phone_number_id_example' # str | The unique identifier of the phone number which is to be unassigned. This can be retrieved from Get a Shared Line Group API.

try:
    # Unassign a phone number
    api_instance.delete_a_phone_number_slg(shared_line_group_id, phone_number_id)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->delete_a_phone_number_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the shared line group from which you would like to unassign a phone number. | 
 **phone_number_id** | **str**| The unique identifier of the phone number which is to be unassigned. This can be retrieved from Get a Shared Line Group API. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_shared_line_group**
> object delete_a_shared_line_group(shared_line_group_id)

Delete a shared line group

Deletes a shared line group. A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common areas.  **Prerequisites:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the shared line group that you would like to delete.

try:
    # Delete a shared line group
    api_response = api_instance.delete_a_shared_line_group(shared_line_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->delete_a_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the shared line group that you would like to delete. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_members_of_slg**
> object delete_members_of_slg(shared_line_group_id)

Unassign members from a shared line group

Unassigns **all** existing members from a Shared Line Group.Members of the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) have access to the group's phone number and voicemail.   **Prerequisites:**   * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the shared line group that you would like to delete.

try:
    # Unassign members from a shared line group
    api_response = api_instance.delete_members_of_slg(shared_line_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->delete_members_of_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the shared line group that you would like to delete. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_phone_numbers_slg**
> delete_phone_numbers_slg(shared_line_group_id)

Unassign all phone numbers

Unassigns all the phone numbers that have been assigned to the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792-Setting-up-shared-line-groups).  **Prerequisites:**   * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the Shared Line Group.

try:
    # Unassign all phone numbers
    api_instance.delete_phone_numbers_slg(shared_line_group_id)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->delete_phone_numbers_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the Shared Line Group. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_shared_line_group**
> InlineResponse20065 get_a_shared_line_group(shared_line_group_id)

Get a shared line group

 Lists all the shared line groups. A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common areas. This gives members of the shared line group access to the group's direct phone number and voicemail.   **Prerequisites:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the Shared Line Group.

try:
    # Get a shared line group
    api_response = api_instance.get_a_shared_line_group(shared_line_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->get_a_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the Shared Line Group. | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_line_groups**
> InlineResponse20064 list_shared_line_groups(page_size=page_size, next_page_token=next_page_token)

List shared line groups

Lists all the shared line groups. A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common areas. This capability gives members of the shared line group access to the group's direct phone number and voicemail.   **Prerequisites:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges  <br>  **Scopes:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List shared line groups
    api_response = api_instance.list_shared_line_groups(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->list_shared_line_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_slg_policy_sub_setting**
> object remove_slg_policy_sub_setting(shared_line_group_id, policy_type, shared_ids)

Delete an SLG policy setting

Removes the policy sub-setting for a specific [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) according to the `policyType`. For example, you can use this API to remove shared access members.   **Prerequisites:**  * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The shared line group ID.
policy_type = 'policy_type_example' # str | This field corresponds to the policy item you wish to remove. Allowed values: `voice_mail`.
shared_ids = ['shared_ids_example'] # list[str] | This field is a comma separated list of shared IDs to remove. The number is limited to the minimum value of 10 or the number of allowed access members account setting.

try:
    # Delete an SLG policy setting
    api_response = api_instance.remove_slg_policy_sub_setting(shared_line_group_id, policy_type, shared_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->remove_slg_policy_sub_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The shared line group ID. | 
 **policy_type** | **str**| This field corresponds to the policy item you wish to remove. Allowed values: &#x60;voice_mail&#x60;. | 
 **shared_ids** | [**list[str]**](str.md)| This field is a comma separated list of shared IDs to remove. The number is limited to the minimum value of 10 or the number of allowed access members account setting. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_shared_line_group**
> object update_a_shared_line_group(shared_line_group_id, body=body)

Update a shared line group

 Updates information of a shared line group. A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common areas. This gives members of the shared line group access to the group's direct phone number and voicemail.  **Prerequisites:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The unique identifier of the shared line group that is to be updated.
body = swagger_client.SharedLineGroupsSharedLineGroupIdBody() # SharedLineGroupsSharedLineGroupIdBody |  (optional)

try:
    # Update a shared line group
    api_response = api_instance.update_a_shared_line_group(shared_line_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->update_a_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The unique identifier of the shared line group that is to be updated. | 
 **body** | [**SharedLineGroupsSharedLineGroupIdBody**](SharedLineGroupsSharedLineGroupIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_slg_policy_sub_setting**
> object update_slg_policy_sub_setting(shared_line_group_id, policy_type, body=body)

Update an SLG policy setting

Updates the policy sub-setting for a specific [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) according to the `policyType`. For example, you can use this API to update shared access members.   **Prerequisites:**  * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SharedLineGroupApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | The shared line group ID.
policy_type = 'policy_type_example' # str | This field corresponds to the policy item you wish to update. Allowed values: `voice_mail`.
body = swagger_client.PolicyPolicyTypeBody1() # PolicyPolicyTypeBody1 |  (optional)

try:
    # Update an SLG policy setting
    api_response = api_instance.update_slg_policy_sub_setting(shared_line_group_id, policy_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineGroupApi->update_slg_policy_sub_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| The shared line group ID. | 
 **policy_type** | **str**| This field corresponds to the policy item you wish to update. Allowed values: &#x60;voice_mail&#x60;. | 
 **body** | [**PolicyPolicyTypeBody1**](PolicyPolicyTypeBody1.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

