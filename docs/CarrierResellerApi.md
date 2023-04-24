# swagger_client.CarrierResellerApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_cr_phone_numbers**](CarrierResellerApi.md#active_cr_phone_numbers) | **PATCH** /phone/carrier_reseller/numbers | Activate phone numbers
[**create_cr_phone_numbers**](CarrierResellerApi.md#create_cr_phone_numbers) | **POST** /phone/carrier_reseller/numbers | Create phone numbers
[**delete_cr_phone_number**](CarrierResellerApi.md#delete_cr_phone_number) | **DELETE** /phone/carrier_reseller/numbers/{number} | Delete a phone number
[**list_cr_phone_numbers**](CarrierResellerApi.md#list_cr_phone_numbers) | **GET** /phone/carrier_reseller/numbers | List phone numbers

# **active_cr_phone_numbers**
> active_cr_phone_numbers(body=body)

Activate phone numbers

Use this API to change phone number status to 'active' in a carrier reseller's master account. Up to 200 numbers at a time.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.CarrierResellerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] |  (optional)

try:
    # Activate phone numbers
    api_instance.active_cr_phone_numbers(body=body)
except ApiException as e:
    print("Exception when calling CarrierResellerApi->active_cr_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cr_phone_numbers**
> create_cr_phone_numbers(body=body)

Create phone numbers

Use this API to add phone numbers to a carrier reseller (master) account. Up to 200 numbers at a time. If this API is called in MA mode, it also has functions of distribution.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.CarrierResellerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.CarrierResellerNumbersBody()] # list[CarrierResellerNumbersBody] |  (optional)

try:
    # Create phone numbers
    api_instance.create_cr_phone_numbers(body=body)
except ApiException as e:
    print("Exception when calling CarrierResellerApi->create_cr_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CarrierResellerNumbersBody]**](CarrierResellerNumbersBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cr_phone_number**
> delete_cr_phone_number(number)

Delete a phone number

Use this API to delete or unassign a phone number from a carrier reseller account.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.CarrierResellerApi(swagger_client.ApiClient(configuration))
number = 'number_example' # str | Phone number in E164 format.

try:
    # Delete a phone number
    api_instance.delete_cr_phone_number(number)
except ApiException as e:
    print("Exception when calling CarrierResellerApi->delete_cr_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Phone number in E164 format. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cr_phone_numbers**
> InlineResponse20016 list_cr_phone_numbers(page_size=page_size, next_page_token=next_page_token, assigned_status=assigned_status, sub_account_id=sub_account_id, keyword=keyword)

List phone numbers

Use this API to list phone numbers in a carrier reseller (master) account that can be pushed to its subaccounts.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.CarrierResellerApi(swagger_client.ApiClient(configuration))
page_size = 56 # int | The size of the page. (optional)
next_page_token = 'next_page_token_example' # str | The current page number of returned records. (optional)
assigned_status = 'assigned_status_example' # str | Number assignment status. (optional)
sub_account_id = 'sub_account_id_example' # str | Partner account ID from sub-account. (optional)
keyword = 'keyword_example' # str | Partial string of the phone number. (optional)

try:
    # List phone numbers
    api_response = api_instance.list_cr_phone_numbers(page_size=page_size, next_page_token=next_page_token, assigned_status=assigned_status, sub_account_id=sub_account_id, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierResellerApi->list_cr_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The size of the page. | [optional] 
 **next_page_token** | **str**| The current page number of returned records. | [optional] 
 **assigned_status** | **str**| Number assignment status. | [optional] 
 **sub_account_id** | **str**| Partner account ID from sub-account. | [optional] 
 **keyword** | **str**| Partial string of the phone number. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

