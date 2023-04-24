# swagger_client.AutoReceptionistsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_auto_receptionist**](AutoReceptionistsApi.md#add_auto_receptionist) | **POST** /phone/auto_receptionists | Add an auto receptionist
[**add_policy**](AutoReceptionistsApi.md#add_policy) | **POST** /phone/auto_receptionists/{autoReceptionistId}/policies/{policyType} | Add a policy setting
[**assign_phone_numbers_auto_receptionist**](AutoReceptionistsApi.md#assign_phone_numbers_auto_receptionist) | **POST** /phone/auto_receptionists/{autoReceptionistId}/phone_numbers | Assign phone numbers
[**delete_auto_receptionist**](AutoReceptionistsApi.md#delete_auto_receptionist) | **DELETE** /phone/auto_receptionists/{autoReceptionistId} | Delete a non-primary auto receptionist
[**delete_policy**](AutoReceptionistsApi.md#delete_policy) | **DELETE** /phone/auto_receptionists/{autoReceptionistId}/policies/{policyType} | Delete a policy setting
[**get_auto_receptionist_detail**](AutoReceptionistsApi.md#get_auto_receptionist_detail) | **GET** /phone/auto_receptionists/{autoReceptionistId} | Get an auto receptionist
[**get_auto_receptionists_policy**](AutoReceptionistsApi.md#get_auto_receptionists_policy) | **GET** /phone/auto_receptionists/{autoReceptionistId}/policies | Get an auto receptionist policy
[**list_auto_receptionists**](AutoReceptionistsApi.md#list_auto_receptionists) | **GET** /phone/auto_receptionists | List auto receptionists
[**unassign_a_phone_num_auto_receptionist**](AutoReceptionistsApi.md#unassign_a_phone_num_auto_receptionist) | **DELETE** /phone/auto_receptionists/{autoReceptionistId}/phone_numbers/{phoneNumberId} | Unassign a phone number
[**unassign_all_phone_nums_auto_receptionist**](AutoReceptionistsApi.md#unassign_all_phone_nums_auto_receptionist) | **DELETE** /phone/auto_receptionists/{autoReceptionistId}/phone_numbers | Unassign all phone numbers
[**update_auto_receptionist**](AutoReceptionistsApi.md#update_auto_receptionist) | **PATCH** /phone/auto_receptionists/{autoReceptionistId} | Update an auto receptionist
[**update_auto_receptionist_policy**](AutoReceptionistsApi.md#update_auto_receptionist_policy) | **PATCH** /phone/auto_receptionists/{autoReceptionistId}/policies | Update an auto receptionist policy
[**update_policy**](AutoReceptionistsApi.md#update_policy) | **PATCH** /phone/auto_receptionists/{autoReceptionistId}/policies/{policyType} | Update a policy setting

# **add_auto_receptionist**
> InlineResponse201 add_auto_receptionist(body=body)

Add an auto receptionist

Auto receptionists answer calls with a personalized recording and routes calls to a phone user, call queue, common area, voicemail or an IVR system. Use this API to add an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-) to a Zoom Phone  **Prerequisites:** * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneAutoReceptionistsBody() # PhoneAutoReceptionistsBody |  (optional)

try:
    # Add an auto receptionist
    api_response = api_instance.add_auto_receptionist(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->add_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneAutoReceptionistsBody**](PhoneAutoReceptionistsBody.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_policy**
> InlineResponse2011 add_policy(auto_receptionist_id, policy_type, body=body)

Add a policy setting

Use this API to add a policy sub-setting according to the policy type for a specific [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-). For example, you can set up shared access members.  **Prerequisites:** * Pro or higher account plan with Zoom Phone license * Account owner or admin permissions  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).
policy_type = 'policy_type_example' # str | Corresponds to the policy item you wish to add. Allowed values: `voice_mail`
body = swagger_client.PoliciesPolicyTypeBody() # PoliciesPolicyTypeBody |  (optional)

try:
    # Add a policy setting
    api_response = api_instance.add_policy(auto_receptionist_id, policy_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->add_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 
 **policy_type** | **str**| Corresponds to the policy item you wish to add. Allowed values: &#x60;voice_mail&#x60; | 
 **body** | [**PoliciesPolicyTypeBody**](PoliciesPolicyTypeBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_numbers_auto_receptionist**
> object assign_phone_numbers_auto_receptionist(auto_receptionist_id, body=body)

Assign phone numbers

Assign available phone numbers to an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-). The available numbers can be retrieved using the List Phone Numbers API with `type` query parameter set to \"unassigned\".  **Prerequisites:** * Pro or higher account plan with Zoom Phone License * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).
body = swagger_client.AutoReceptionistIdPhoneNumbersBody() # AutoReceptionistIdPhoneNumbersBody |  (optional)

try:
    # Assign phone numbers
    api_response = api_instance.assign_phone_numbers_auto_receptionist(auto_receptionist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->assign_phone_numbers_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 
 **body** | [**AutoReceptionistIdPhoneNumbersBody**](AutoReceptionistIdPhoneNumbersBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_receptionist**
> object delete_auto_receptionist(auto_receptionist_id)

Delete a non-primary auto receptionist

An auto receptionist answers calls with a personalized recording and routes calls to a phone user, call queue, common area (phone), or to a voicemail. An auto receptionist can also be set up so that it routes calls to an interactive voice response (IVR) system to allow callers to select the routing options. Use this API to [delete a non-primary auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-#h_1d5ffc56-6ba3-4ce5-9d86-4a1a1ee743f3).  **Prerequisites:** * Pro or higher account with Zoom Phone license.  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).

try:
    # Delete a non-primary auto receptionist
    api_response = api_instance.delete_auto_receptionist(auto_receptionist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->delete_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(auto_receptionist_id, policy_type, shared_ids)

Delete a policy setting

Use this API to remove the policy sub-setting of a [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-). For example, you can remove shared access members.  **Prerequisites:** * Pro or higher account plan with Zoom Phone license * Account owner or admin permissions  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).
policy_type = 'policy_type_example' # str | Corresponds to the policy item you wish to remove. Allowed values: `voice_mail`
shared_ids = ['shared_ids_example'] # list[str] | Unique identifier of the voicemail that the user can access. Required only for `voice_mail` policy type.

try:
    # Delete a policy setting
    api_instance.delete_policy(auto_receptionist_id, policy_type, shared_ids)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 
 **policy_type** | **str**| Corresponds to the policy item you wish to remove. Allowed values: &#x60;voice_mail&#x60; | 
 **shared_ids** | [**list[str]**](str.md)| Unique identifier of the voicemail that the user can access. Required only for &#x60;voice_mail&#x60; policy type. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_receptionist_detail**
> InlineResponse2002 get_auto_receptionist_detail(auto_receptionist_id)

Get an auto receptionist

Use this API to get information on a specific auto receptionist.  **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | 

try:
    # Get an auto receptionist
    api_response = api_instance.get_auto_receptionist_detail(auto_receptionist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->get_auto_receptionist_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_receptionists_policy**
> InlineResponse2003 get_auto_receptionists_policy(auto_receptionist_id)

Get an auto receptionist policy

Use this API to get the policy setting of a specific [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-).  **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).

try:
    # Get an auto receptionist policy
    api_response = api_instance.get_auto_receptionists_policy(auto_receptionist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->get_auto_receptionists_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_receptionists**
> InlineResponse2001 list_auto_receptionists(page_size=page_size, next_page_token=next_page_token)

List auto receptionists

Use this API to list auto receptionists.  **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List auto receptionists
    api_response = api_instance.list_auto_receptionists(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->list_auto_receptionists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_a_phone_num_auto_receptionist**
> object unassign_a_phone_num_auto_receptionist(auto_receptionist_id, phone_number_id)

Unassign a phone number

Unassign a specific phone number that was previously assigned to an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-).   **Prerequisites:** * Pro or higher account plan with Zoom Phone License * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).
phone_number_id = 'phone_number_id_example' # str | Unique Identifier of the phone number or provide the actual phone number in e164 format (example: +19995550123).

try:
    # Unassign a phone number
    api_response = api_instance.unassign_a_phone_num_auto_receptionist(auto_receptionist_id, phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->unassign_a_phone_num_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 
 **phone_number_id** | **str**| Unique Identifier of the phone number or provide the actual phone number in e164 format (example: +19995550123). | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_all_phone_nums_auto_receptionist**
> object unassign_all_phone_nums_auto_receptionist(auto_receptionist_id)

Unassign all phone numbers

Unassign all phone numbers that were previously assigned to an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-).   **Prerequisites:** * Pro or higher account plan with Zoom Phone License * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light` 

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | 

try:
    # Unassign all phone numbers
    api_response = api_instance.unassign_all_phone_nums_auto_receptionist(auto_receptionist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->unassign_all_phone_nums_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_receptionist**
> object update_auto_receptionist(auto_receptionist_id, body=body)

Update an auto receptionist

An auto receptionist answers calls with a personalized recording and routes calls to a phone user, call queue, common area, or voicemail. An auto receptionist can also be set up so that it routes calls to an interactive voice response (IVR) system to allow callers to select the routing options. Use this API to [change information](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-#h_1d5ffc56-6ba3-4ce5-9d86-4a1a1ee743f3) such as the display name and extension number assigned to the main auto receptionist.  **Prerequisites:** * Pro or higher account with Zoom Phone license.  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).
body = swagger_client.AutoReceptionistsAutoReceptionistIdBody() # AutoReceptionistsAutoReceptionistIdBody |  (optional)

try:
    # Update an auto receptionist
    api_response = api_instance.update_auto_receptionist(auto_receptionist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->update_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 
 **body** | [**AutoReceptionistsAutoReceptionistIdBody**](AutoReceptionistsAutoReceptionistIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_receptionist_policy**
> object update_auto_receptionist_policy(auto_receptionist_id, body=body)

Update an auto receptionist policy

Use this API to update the policy setting of a specific [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-).   **Prerequisites:** * Pro or higher account plan with Zoom Phone License * Account owner or admin permissions  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).
body = swagger_client.AutoReceptionistIdPoliciesBody() # AutoReceptionistIdPoliciesBody |  (optional)

try:
    # Update an auto receptionist policy
    api_response = api_instance.update_auto_receptionist_policy(auto_receptionist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->update_auto_receptionist_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 
 **body** | [**AutoReceptionistIdPoliciesBody**](AutoReceptionistIdPoliciesBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> object update_policy(auto_receptionist_id, policy_type, body=body)

Update a policy setting

Use this API to update the policy sub-setting of a specific [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-) according to the policy type. For example, you can update shared access members.  **Prerequisites:** * Pro or higher account plan with Zoom Phone license * Account owner or admin permissions  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists).
policy_type = 'policy_type_example' # str | Corresponds to the policy item you wish to modify. Allowed values: `voice_mail`
body = swagger_client.PoliciesPolicyTypeBody1() # PoliciesPolicyTypeBody1 |  (optional)

try:
    # Update a policy setting
    api_response = api_instance.update_policy(auto_receptionist_id, policy_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoReceptionistsApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List auto receptionists API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listAutoReceptionists). | 
 **policy_type** | **str**| Corresponds to the policy item you wish to modify. Allowed values: &#x60;voice_mail&#x60; | 
 **body** | [**PoliciesPolicyTypeBody1**](PoliciesPolicyTypeBody1.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

