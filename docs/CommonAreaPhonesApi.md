# swagger_client.CommonAreaPhonesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_common_area_phone**](CommonAreaPhonesApi.md#add_common_area_phone) | **POST** /phone/common_area_phones | Add a common area phone
[**assign_calling_plans_to_common_area_phone**](CommonAreaPhonesApi.md#assign_calling_plans_to_common_area_phone) | **POST** /phone/common_area_phones/{commonAreaPhoneId}/calling_plans | Assign calling plans to common area phone
[**assign_phone_numbers_to_common_area_phone**](CommonAreaPhonesApi.md#assign_phone_numbers_to_common_area_phone) | **POST** /phone/common_area_phones/{commonAreaPhoneId}/phone_numbers | Assign phone numbers to common area phone
[**delete_common_area_phone**](CommonAreaPhonesApi.md#delete_common_area_phone) | **DELETE** /phone/common_area_phones/{commonAreaPhoneId} | Delete a common area phone
[**get_a_common_area_phone**](CommonAreaPhonesApi.md#get_a_common_area_phone) | **GET** /phone/common_area_phones/{commonAreaPhoneId} | Get common area phone details
[**list_common_area_phones**](CommonAreaPhonesApi.md#list_common_area_phones) | **GET** /phone/common_area_phones | List common area phones
[**unassign_calling_plans_from_common_area_phone**](CommonAreaPhonesApi.md#unassign_calling_plans_from_common_area_phone) | **DELETE** /phone/common_area_phones/{commonAreaPhoneId}/calling_plans/{type} | Unassign calling plan from a common area phone
[**unassign_phone_numbers_from_common_area_phone**](CommonAreaPhonesApi.md#unassign_phone_numbers_from_common_area_phone) | **DELETE** /phone/common_area_phones/{commonAreaPhoneId}/phone_numbers/{phoneNumberId} | Unassign phone numbers from a common area phone
[**update_common_area_phone**](CommonAreaPhonesApi.md#update_common_area_phone) | **PATCH** /phone/common_area_phones/{commonAreaPhoneId} | Update common area phone

# **add_common_area_phone**
> InlineResponse2017 add_common_area_phone(body=body)

Add a common area phone

Use this API to [add a common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones#h_2d0da347-c35a-4993-9771-e21aaa568deb).  A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.  **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * A [supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)  **Scopes:**  `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneCommonAreaPhonesBody() # PhoneCommonAreaPhonesBody |  (optional)

try:
    # Add a common area phone
    api_response = api_instance.add_common_area_phone(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->add_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneCommonAreaPhonesBody**](PhoneCommonAreaPhonesBody.md)|  | [optional] 

### Return type

[**InlineResponse2017**](InlineResponse2017.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_calling_plans_to_common_area_phone**
> InlineResponse2018 assign_calling_plans_to_common_area_phone(common_area_phone_id, body=body)

Assign calling plans to common area phone

Assign calling plans to common area phone.    **Prerequisites:**  * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scopes:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | 
body = swagger_client.CommonAreaPhoneIdCallingPlansBody() # CommonAreaPhoneIdCallingPlansBody |  (optional)

try:
    # Assign calling plans to common area phone
    api_response = api_instance.assign_calling_plans_to_common_area_phone(common_area_phone_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->assign_calling_plans_to_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**|  | 
 **body** | [**CommonAreaPhoneIdCallingPlansBody**](CommonAreaPhoneIdCallingPlansBody.md)|  | [optional] 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_numbers_to_common_area_phone**
> InlineResponse2019 assign_phone_numbers_to_common_area_phone(common_area_phone_id, body=body)

Assign phone numbers to common area phone

Assign phone numbers to common area phone.    **Prerequisites:**  * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. **Scope:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | 
body = swagger_client.CommonAreaPhoneIdPhoneNumbersBody() # CommonAreaPhoneIdPhoneNumbersBody |  (optional)

try:
    # Assign phone numbers to common area phone
    api_response = api_instance.assign_phone_numbers_to_common_area_phone(common_area_phone_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->assign_phone_numbers_to_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**|  | 
 **body** | [**CommonAreaPhoneIdPhoneNumbersBody**](CommonAreaPhoneIdPhoneNumbersBody.md)|  | [optional] 

### Return type

[**InlineResponse2019**](InlineResponse2019.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_common_area_phone**
> object delete_common_area_phone(common_area_phone_id)

Delete a common area phone

A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.  Use this API to remove the [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) from Zoom Phone System in an account.  **Prerequisites:**  * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)  **Scopes:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | Unique identifier of the common area phone.

try:
    # Delete a common area phone
    api_response = api_instance.delete_common_area_phone(common_area_phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->delete_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**| Unique identifier of the common area phone. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_common_area_phone**
> InlineResponse20018 get_a_common_area_phone(common_area_phone_id)

Get common area phone details

Use this API to get details on a specific [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) in an account.  A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.     **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * A [supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)  **Scopes:**  `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | Unique identifier of the Common Area Phone. Use the unique identifier or the Mac address of the common area phone. The Mac address can be in hyphenated (`00-04-f2-5e-ec-3c`) or not hyphenated (`0004f25eec3c`) format. You can get this value from the [List Common Area Phones API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listCommonAreaPhones).

try:
    # Get common area phone details
    api_response = api_instance.get_a_common_area_phone(common_area_phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->get_a_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**| Unique identifier of the Common Area Phone. Use the unique identifier or the Mac address of the common area phone. The Mac address can be in hyphenated (&#x60;00-04-f2-5e-ec-3c&#x60;) or not hyphenated (&#x60;0004f25eec3c&#x60;) format. You can get this value from the [List Common Area Phones API](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listCommonAreaPhones). | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_common_area_phones**
> InlineResponse20017 list_common_area_phones(page_size=page_size, next_page_token=next_page_token)

List common area phones

Use this API to list all of an account's [common area phones](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones).  A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. * A [supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List common area phones
    api_response = api_instance.list_common_area_phones(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->list_common_area_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_calling_plans_from_common_area_phone**
> unassign_calling_plans_from_common_area_phone(common_area_phone_id, type, billing_account_id=billing_account_id)

Unassign calling plan from a common area phone

Use this API to unassign a calling plan from a common area phone.  **Prerequisites:**  * A Pro or higher account with a Zoom Phone license  * An account owner or admin permissions  **Scopes:**   `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | The common area phone's unique ID.
type = 'type_example' # str | The [calling plan](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) to remove.
billing_account_id = 'billing_account_id_example' # str | Billing account ID. If the common area phone is in India, the parameter is required. (optional)

try:
    # Unassign calling plan from a common area phone
    api_instance.unassign_calling_plans_from_common_area_phone(common_area_phone_id, type, billing_account_id=billing_account_id)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->unassign_calling_plans_from_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**| The common area phone&#x27;s unique ID. | 
 **type** | **str**| The [calling plan](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) to remove. | 
 **billing_account_id** | **str**| Billing account ID. If the common area phone is in India, the parameter is required. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_phone_numbers_from_common_area_phone**
> unassign_phone_numbers_from_common_area_phone(common_area_phone_id, phone_number_id)

Unassign phone numbers from a common area phone

Use this API to unassign a phone number from a common Area phone.  **Prerequisites:**  * A Pro or a higher account with a Zoom Phone license * An account owner or admin permissions  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | The common area phone's unique ID.
phone_number_id = 'phone_number_id_example' # str | The phone number or the phone number's unique ID.

try:
    # Unassign phone numbers from a common area phone
    api_instance.unassign_phone_numbers_from_common_area_phone(common_area_phone_id, phone_number_id)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->unassign_phone_numbers_from_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**| The common area phone&#x27;s unique ID. | 
 **phone_number_id** | **str**| The phone number or the phone number&#x27;s unique ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_area_phone**
> object update_common_area_phone(common_area_phone_id, body=body)

Update common area phone

Use this API to update details on a specific [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) in an account.  A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * A [supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | 
body = swagger_client.CommonAreaPhonesCommonAreaPhoneIdBody() # CommonAreaPhonesCommonAreaPhoneIdBody |  (optional)

try:
    # Update common area phone
    api_response = api_instance.update_common_area_phone(common_area_phone_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->update_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**|  | 
 **body** | [**CommonAreaPhonesCommonAreaPhoneIdBody**](CommonAreaPhonesCommonAreaPhoneIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

