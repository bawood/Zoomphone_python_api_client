# swagger_client.UsersApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_outbound_caller_numbers**](UsersApi.md#add_user_outbound_caller_numbers) | **POST** /phone/users/{userId}/outbound_caller_id/customized_numbers | Add phone numbers for users&#x27; customized outbound caller ID
[**add_user_setting**](UsersApi.md#add_user_setting) | **POST** /phone/users/{userId}/settings/{settingType} | Add a user&#x27;s shared access setting
[**assign_calling_plan**](UsersApi.md#assign_calling_plan) | **POST** /phone/users/{userId}/calling_plans | Assign calling plan to a user
[**batch_add_users**](UsersApi.md#batch_add_users) | **POST** /phone/users/batch | Batch add users
[**delete_user_outbound_caller_numbers**](UsersApi.md#delete_user_outbound_caller_numbers) | **DELETE** /phone/users/{userId}/outbound_caller_id/customized_numbers | Remove users&#x27; customized outbound caller ID phone numbers
[**delete_user_setting**](UsersApi.md#delete_user_setting) | **DELETE** /phone/users/{userId}/settings/{settingType} | Delete a user&#x27;s shared access setting
[**get_user_policy_details**](UsersApi.md#get_user_policy_details) | **GET** /phone/users/{userId}/policies/{policyType} | Get user policy details
[**list_phone_users**](UsersApi.md#list_phone_users) | **GET** /phone/users | List phone users
[**list_user_customize_outbound_caller_numbers**](UsersApi.md#list_user_customize_outbound_caller_numbers) | **GET** /phone/users/{userId}/outbound_caller_id/customized_numbers | List users&#x27; phone numbers for a customized outbound caller ID
[**phone_user**](UsersApi.md#phone_user) | **GET** /phone/users/{userId} | Get a user&#x27;s profile
[**phone_user_settings**](UsersApi.md#phone_user_settings) | **GET** /phone/users/{userId}/settings | Get a user&#x27;s profile settings
[**unassign_calling_plan**](UsersApi.md#unassign_calling_plan) | **DELETE** /phone/users/{userId}/calling_plans/{type} | Unassign user&#x27;s calling plan
[**update_calling_plan**](UsersApi.md#update_calling_plan) | **PUT** /phone/users/{userId}/calling_plans | Update user&#x27;s calling plan
[**update_user_policy**](UsersApi.md#update_user_policy) | **PATCH** /phone/users/{userId}/policies/{policyType} | Update user policy
[**update_user_profile**](UsersApi.md#update_user_profile) | **PATCH** /phone/users/{userId} | Update a user&#x27;s profile
[**update_user_setting**](UsersApi.md#update_user_setting) | **PATCH** /phone/users/{userId}/settings/{settingType} | Update a user&#x27;s shared access setting
[**update_user_settings**](UsersApi.md#update_user_settings) | **PATCH** /phone/users/{userId}/settings | Update a user&#x27;s profile settings
[**update_users_properties_in_batch**](UsersApi.md#update_users_properties_in_batch) | **PUT** /phone/users/batch | Update multiple users&#x27; properties in batch

# **add_user_outbound_caller_numbers**
> object add_user_outbound_caller_numbers(user_id, body=body)

Add phone numbers for users' customized outbound caller ID

Adds users' customized outbound caller ID phone numbers.   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The unique identifier of the user.
body = swagger_client.OutboundCallerIdCustomizedNumbersBody2() # OutboundCallerIdCustomizedNumbersBody2 |  (optional)

try:
    # Add phone numbers for users' customized outbound caller ID
    api_response = api_instance.add_user_outbound_caller_numbers(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_user_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **body** | [**OutboundCallerIdCustomizedNumbersBody2**](OutboundCallerIdCustomizedNumbersBody2.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_setting**
> InlineResponse20127 add_user_setting(user_id, setting_type, body=body)

Add a user's shared access setting

Adds the user setting according to the setting type, specifically for delegation, intercom and shared access for voicemail, and call recordings. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  To see the shared access settings in the Zoom web portal, go to **Admin > Phone System Management > Users & Rooms** . Click **Users** and select **User Policy**. Go to **Voicemail, Automatic Call Recording and Ad Hoc Call Recording**.   To view the delegation and intercom setting in your Zoom web portal, navigate to **Admin > Phone System Management > Users & Rooms**. Click the **Users** tab and select **User Settings**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The unique identifier of the user.
setting_type = 'setting_type_example' # str | Corresponds to the setting item you wish to modify. Allowed values: `voice_mail`, `delegation`, `desk_phone`, `intercom`, `auto_call_recording`,`ad_hoc_call_recording`
body = swagger_client.SettingsSettingTypeBody6() # SettingsSettingTypeBody6 |  (optional)

try:
    # Add a user's shared access setting
    api_response = api_instance.add_user_setting(user_id, setting_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **setting_type** | **str**| Corresponds to the setting item you wish to modify. Allowed values: &#x60;voice_mail&#x60;, &#x60;delegation&#x60;, &#x60;desk_phone&#x60;, &#x60;intercom&#x60;, &#x60;auto_call_recording&#x60;,&#x60;ad_hoc_call_recording&#x60; | 
 **body** | [**SettingsSettingTypeBody6**](SettingsSettingTypeBody6.md)|  | [optional] 

### Return type

[**InlineResponse20127**](InlineResponse20127.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_calling_plan**
> object assign_calling_plan(user_id, body=body)

Assign calling plan to a user

Assigns a [calling plan](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) to a [Zoom Phone](https://support.zoom.us/hc/en-us/categories/360001370051-Zoom-Phone) user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:write`, `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = swagger_client.UserIdCallingPlansBody1() # UserIdCallingPlansBody1 |  (optional)

try:
    # Assign calling plan to a user
    api_response = api_instance.assign_calling_plan(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->assign_calling_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**UserIdCallingPlansBody1**](UserIdCallingPlansBody1.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_add_users**
> list[InlineResponse20125] batch_add_users(body=body)

Batch add users

Adds phone users in batch. You can add up to 10 users at a time.  **Prerequisites:** * The users must be active in your [Zoom account](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods#tag/Users/operation/users).  * Pro or higher account plan with Zoom phone license * Account owner or admin permissions  **Scope:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersBatchBody1() # UsersBatchBody1 |  (optional)

try:
    # Batch add users
    api_response = api_instance.batch_add_users(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->batch_add_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersBatchBody1**](UsersBatchBody1.md)|  | [optional] 

### Return type

[**list[InlineResponse20125]**](InlineResponse20125.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_outbound_caller_numbers**
> object delete_user_outbound_caller_numbers(user_id, customize_ids=customize_ids)

Remove users' customized outbound caller ID phone numbers

Removes the users' customized outbound caller ID phone numbers.   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The unique identifier of the user.
customize_ids = ['customize_ids_example'] # list[str] | The customization IDs. (optional)

try:
    # Remove users' customized outbound caller ID phone numbers
    api_response = api_instance.delete_user_outbound_caller_numbers(user_id, customize_ids=customize_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **customize_ids** | [**list[str]**](str.md)| The customization IDs. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_setting**
> object delete_user_setting(user_id, setting_type, shared_id=shared_id, assistant_extension_id=assistant_extension_id, device_id=device_id, intercom_extension_id=intercom_extension_id)

Delete a user's shared access setting

Removes the user setting according to the setting type, specifically for delegation, intercom and shared access for voicemail and call recordings. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  To see the shared access settings in the Zoom web portal, go to **Admin > Phone System Management > Users & Rooms** . Click **Users** and select **User Policy**. Go to **Voicemail, Automatic Call Recording and Ad Hoc Call Recording**.   To view the delegation and intercom setting in your Zoom web portal, navigate to **Admin > Phone System Management > Users & Rooms**. Click the **Users** tab and select **User Settings**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The unique identifier of the user.
setting_type = 'setting_type_example' # str | Corresponds to the setting item you wish to remove. Allowed values: `voice_mail`, `delegation`, `desk_phone`, `intercom`, `auto_call_recording`,`ad_hoc_call_recording`
shared_id = 'shared_id_example' # str | This field is required only for voicemail, auto_call_recording, and ad_hoc_call_recording setting type. (optional)
assistant_extension_id = 'assistant_extension_id_example' # str | This field deletes the delegation assistant, used for delegation setting type. (optional)
device_id = 'device_id_example' # str | This field deletes the assigned device, used for `desk_phone` setting type. (optional)
intercom_extension_id = 'intercom_extension_id_example' # str | This field deletes the intercom connection for the `intercom` setting type. (optional)

try:
    # Delete a user's shared access setting
    api_response = api_instance.delete_user_setting(user_id, setting_type, shared_id=shared_id, assistant_extension_id=assistant_extension_id, device_id=device_id, intercom_extension_id=intercom_extension_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **setting_type** | **str**| Corresponds to the setting item you wish to remove. Allowed values: &#x60;voice_mail&#x60;, &#x60;delegation&#x60;, &#x60;desk_phone&#x60;, &#x60;intercom&#x60;, &#x60;auto_call_recording&#x60;,&#x60;ad_hoc_call_recording&#x60; | 
 **shared_id** | **str**| This field is required only for voicemail, auto_call_recording, and ad_hoc_call_recording setting type. | [optional] 
 **assistant_extension_id** | **str**| This field deletes the delegation assistant, used for delegation setting type. | [optional] 
 **device_id** | **str**| This field deletes the assigned device, used for &#x60;desk_phone&#x60; setting type. | [optional] 
 **intercom_extension_id** | **str**| This field deletes the intercom connection for the &#x60;intercom&#x60; setting type. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_policy_details**
> InlineResponse20079 get_user_policy_details(user_id, policy_type, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)

Get user policy details

Gets the user policy details.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID.
policy_type = 'policy_type_example' # str | The user policy type: `restricted_call_hours`, `allowed_call_locations`.
sub_policy_type = 'sub_policy_type_example' # str | The sub policy type: `restricted_holiday_hours`, `allowed_call_locations_places`. The `restricted_holiday_hours` sub policy type is for policy type `restricted_call_hours`. The `allowed_call_locations_places` sub policy type is for policy type `allowed_call_locations`. (optional)
holiday_hours_site_id = 'holiday_hours_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `restricted_holiday_hours`. (optional)
locations_site_id = 'locations_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `allowed_call_locations_places`. (optional)

try:
    # Get user policy details
    api_response = api_instance.get_user_policy_details(user_id, policy_type, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_policy_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID. | 
 **policy_type** | **str**| The user policy type: &#x60;restricted_call_hours&#x60;, &#x60;allowed_call_locations&#x60;. | 
 **sub_policy_type** | **str**| The sub policy type: &#x60;restricted_holiday_hours&#x60;, &#x60;allowed_call_locations_places&#x60;. The &#x60;restricted_holiday_hours&#x60; sub policy type is for policy type &#x60;restricted_call_hours&#x60;. The &#x60;allowed_call_locations_places&#x60; sub policy type is for policy type &#x60;allowed_call_locations&#x60;. | [optional] 
 **holiday_hours_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;restricted_holiday_hours&#x60;. | [optional] 
 **locations_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;allowed_call_locations_places&#x60;. | [optional] 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_phone_users**
> InlineResponse20077 list_phone_users(page_size=page_size, next_page_token=next_page_token, site_id=site_id, calling_type=calling_type, status=status, department=department, cost_center=cost_center, keyword=keyword)

List phone users

Returns a list of all of an account's users who are assigned a Zoom Phone license.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
site_id = 'site_id_example' # str | The unique identifier of the site from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. (optional)
calling_type = 56 # int | The [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) of the calling plan. (optional)
status = 'status_example' # str | The status of the Zoom Phone user. (optional)
department = 'department_example' # str | The department of which the user belongs. (optional)
cost_center = 'cost_center_example' # str | The cost center of which the user belongs. (optional)
keyword = 'keyword_example' # str | The partial string of user's name, extension number or phone number. (optional)

try:
    # List phone users
    api_response = api_instance.list_phone_users(page_size=page_size, next_page_token=next_page_token, site_id=site_id, calling_type=calling_type, status=status, department=department, cost_center=cost_center, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_phone_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **site_id** | **str**| The unique identifier of the site from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. | [optional] 
 **calling_type** | **int**| The [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) of the calling plan. | [optional] 
 **status** | **str**| The status of the Zoom Phone user. | [optional] 
 **department** | **str**| The department of which the user belongs. | [optional] 
 **cost_center** | **str**| The cost center of which the user belongs. | [optional] 
 **keyword** | **str**| The partial string of user&#x27;s name, extension number or phone number. | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_customize_outbound_caller_numbers**
> InlineResponse20087 list_user_customize_outbound_caller_numbers(user_id, selected=selected, site_id=site_id, extension_type=extension_type, keyword=keyword, page_size=page_size, next_page_token=next_page_token)

List users' phone numbers for a customized outbound caller ID

Retrieves phone numbers that can be the `user-level` customized outbound caller ID.   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The unique identifier of the user.
selected = true # bool | The status of the phone numbers.<br>`true`- Numbers already added to the custom list. <br>`false`- Numbers not yet added to the custom list (optional)
site_id = 'site_id_example' # str | This field filters phone numbers that belong to the site. (optional)
extension_type = 'extension_type_example' # str | The type of extension to which the phone number belongs. (optional)
keyword = 'keyword_example' # str | A search keyword for phone or extension numbers. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List users' phone numbers for a customized outbound caller ID
    api_response = api_instance.list_user_customize_outbound_caller_numbers(user_id, selected=selected, site_id=site_id, extension_type=extension_type, keyword=keyword, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_user_customize_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique identifier of the user. | 
 **selected** | **bool**| The status of the phone numbers.&lt;br&gt;&#x60;true&#x60;- Numbers already added to the custom list. &lt;br&gt;&#x60;false&#x60;- Numbers not yet added to the custom list | [optional] 
 **site_id** | **str**| This field filters phone numbers that belong to the site. | [optional] 
 **extension_type** | **str**| The type of extension to which the phone number belongs. | [optional] 
 **keyword** | **str**| A search keyword for phone or extension numbers. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_user**
> InlineResponse20078 phone_user(user_id)

Get a user's profile

Returns a user's [Zoom phone](https://support.zoom.us/hc/en-us/articles/360001297663-Quickstart-Guide-for-Zoom-Phone-Administrators) profile. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:read`, `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Get a user's profile
    api_response = api_instance.phone_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->phone_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_user_settings**
> InlineResponse20086 phone_user_settings(user_id)

Get a user's profile settings

Gets the Zoom Phone [profile settings](https://support.zoom.us/hc/en-us/articles/360021325712-Configuring-Settings) of a user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:read`, `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Get a user's profile settings
    api_response = api_instance.phone_user_settings(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->phone_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_calling_plan**
> object unassign_calling_plan(user_id, type, billing_account_id=billing_account_id)

Unassign user's calling plan

Unassigns a a [Zoom Phone](https://support.zoom.us/hc/en-us/categories/360001370051) user's [calling plan](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans). For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:write`, `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
type = 'type_example' # str | The [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) of the calling plan that was assigned to user. (e.g: The value of type would be \"200\" for Unlimited US/Canada calling plan.) 
billing_account_id = 'billing_account_id_example' # str | The billing account ID. If the user is located in India, the parameter is required. (optional)

try:
    # Unassign user's calling plan
    api_response = api_instance.unassign_calling_plan(user_id, type, billing_account_id=billing_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->unassign_calling_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **type** | **str**| The [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) of the calling plan that was assigned to user. (e.g: The value of type would be \&quot;200\&quot; for Unlimited US/Canada calling plan.)  | 
 **billing_account_id** | **str**| The billing account ID. If the user is located in India, the parameter is required. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_calling_plan**
> object update_calling_plan(user_id, body=body)

Update user's calling plan

Switches [calling plans](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) of a [Zoom Phone](https://support.zoom.us/hc/en-us/categories/360001370051-Zoom-Phone) user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = swagger_client.UserIdCallingPlansBody() # UserIdCallingPlansBody |  (optional)

try:
    # Update user's calling plan
    api_response = api_instance.update_calling_plan(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_calling_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**UserIdCallingPlansBody**](UserIdCallingPlansBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_policy**
> object update_user_policy(user_id, policy_type, body=body, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)

Update user policy

Updates a user's [Zoom Phone](https://support.zoom.us/hc/en-us/categories/360001370051-Zoom-Phone) policy.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID.
policy_type = 'policy_type_example' # str | The user policy type: `restricted_call_hours`, `allowed_call_locations`.
body = swagger_client.PoliciesPolicyTypeBody6() # PoliciesPolicyTypeBody6 |  (optional)
sub_policy_type = 'sub_policy_type_example' # str | The sub policy type: `restricted_holiday_hours`, `allowed_call_locations_places`. The `restricted_holiday_hours` sub policy type is for policy type `restricted_call_hours`. The `allowed_call_locations_places` sub policy type is for policy type `allowed_call_locations`. (optional)
holiday_hours_site_id = 'holiday_hours_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `restricted_holiday_hours`. (optional)
locations_site_id = 'locations_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `allowed_call_locations_places`. (optional)

try:
    # Update user policy
    api_response = api_instance.update_user_policy(user_id, policy_type, body=body, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID. | 
 **policy_type** | **str**| The user policy type: &#x60;restricted_call_hours&#x60;, &#x60;allowed_call_locations&#x60;. | 
 **body** | [**PoliciesPolicyTypeBody6**](PoliciesPolicyTypeBody6.md)|  | [optional] 
 **sub_policy_type** | **str**| The sub policy type: &#x60;restricted_holiday_hours&#x60;, &#x60;allowed_call_locations_places&#x60;. The &#x60;restricted_holiday_hours&#x60; sub policy type is for policy type &#x60;restricted_call_hours&#x60;. The &#x60;allowed_call_locations_places&#x60; sub policy type is for policy type &#x60;allowed_call_locations&#x60;. | [optional] 
 **holiday_hours_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;restricted_holiday_hours&#x60;. | [optional] 
 **locations_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;allowed_call_locations_places&#x60;. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> object update_user_profile(user_id, body=body)

Update a user's profile

Updates a user's [Zoom Phone](https://support.zoom.us/hc/en-us/categories/360001370051-Zoom-Phone) profile. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  To add, update or remove the shared access members for voicemail and call recordings, use the [Add](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Users/operation/addUserSetting)/[Update](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Users/operation/updateUserSetting)/[Delete](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Users/operation/deleteUserSetting) a user's shared access setting API.   **Scopes:** `phone:write`, `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
body = swagger_client.UsersUserIdBody() # UsersUserIdBody |  (optional)

try:
    # Update a user's profile
    api_response = api_instance.update_user_profile(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **body** | [**UsersUserIdBody**](UsersUserIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_setting**
> object update_user_setting(setting_type, user_id, body=body)

Update a user's shared access setting

Updates the user setting according to the setting type, specifically for delegation, intercom and shared access for voicemail and call recordings. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  To see the shared access settings in the Zoom web portal, go to **Admin > Phone System Management > Users & Rooms** . Click **Users** and select **User Policy**. Go to **Voicemail, Automatic Call Recording and Ad Hoc Call Recording**.   To view the delegation and intercom setting in your Zoom web portal, navigate to **Admin > Phone System Management > Users & Rooms**. Click the **Users** tab and select **User Settings**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
setting_type = 'setting_type_example' # str | Corresponds to the setting item you wish to modify. Allowed values: `voice_mail`, `delegation`, `desk_phone`, `intercom`, `auto_call_recording`,`ad_hoc_call_recording`
user_id = 'user_id_example' # str | The unique identifier of the user.
body = swagger_client.SettingsSettingTypeBody7() # SettingsSettingTypeBody7 |  (optional)

try:
    # Update a user's shared access setting
    api_response = api_instance.update_user_setting(setting_type, user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| Corresponds to the setting item you wish to modify. Allowed values: &#x60;voice_mail&#x60;, &#x60;delegation&#x60;, &#x60;desk_phone&#x60;, &#x60;intercom&#x60;, &#x60;auto_call_recording&#x60;,&#x60;ad_hoc_call_recording&#x60; | 
 **user_id** | **str**| The unique identifier of the user. | 
 **body** | [**SettingsSettingTypeBody7**](SettingsSettingTypeBody7.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_settings**
> object update_user_settings(user_id, body=body)

Update a user's profile settings

Updates the Zoom Phone [profile settings](https://support.zoom.us/hc/en-us/articles/360021325712-Configuring-Settings) of a user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:write`, `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
body = swagger_client.UserIdSettingsBody() # UserIdSettingsBody |  (optional)

try:
    # Update a user's profile settings
    api_response = api_instance.update_user_settings(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **body** | [**UserIdSettingsBody**](UserIdSettingsBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users_properties_in_batch**
> object update_users_properties_in_batch(body=body)

Update multiple users' properties in batch

Updates multiple users' properties in batch. For example, the users' [site](https://support.zoom.us/hc/en-us/articles/360020809672) can be updated when `batchType` is equal to `move_site`. You can update 10 users at a time.   **Prerequisites:** * Business, or Education account * Zoom Phone license     **Scopes:** `phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersBatchBody() # UsersBatchBody |  (optional)

try:
    # Update multiple users' properties in batch
    api_response = api_instance.update_users_properties_in_batch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_users_properties_in_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersBatchBody**](UsersBatchBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

