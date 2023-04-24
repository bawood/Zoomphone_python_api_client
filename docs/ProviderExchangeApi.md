# swagger_client.ProviderExchangeApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_peering_phone_numbers**](ProviderExchangeApi.md#add_peering_phone_numbers) | **POST** /phone/peering/numbers | Add peering phone numbers
[**delete_peering_phone_numbers**](ProviderExchangeApi.md#delete_peering_phone_numbers) | **DELETE** /phone/peering/numbers | Remove peering phone numbers
[**list_carrier_peering_phone_numbers**](ProviderExchangeApi.md#list_carrier_peering_phone_numbers) | **GET** /phone/carrier_peering/numbers | List carrier peering phone numbers.
[**list_peering_phone_numbers**](ProviderExchangeApi.md#list_peering_phone_numbers) | **GET** /phone/peering/numbers | List peering phone numbers
[**update_peering_phone_numbers**](ProviderExchangeApi.md#update_peering_phone_numbers) | **PATCH** /phone/peering/numbers | Update peering phone numbers

# **add_peering_phone_numbers**
> InlineResponse20120 add_peering_phone_numbers(body=body)

Add peering phone numbers

Adds phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ProviderExchangeApi(swagger_client.ApiClient(configuration))
body = swagger_client.PeeringNumbersBody() # PeeringNumbersBody |  (optional)

try:
    # Add peering phone numbers
    api_response = api_instance.add_peering_phone_numbers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderExchangeApi->add_peering_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PeeringNumbersBody**](PeeringNumbersBody.md)|  | [optional] 

### Return type

[**InlineResponse20120**](InlineResponse20120.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_peering_phone_numbers**
> InlineResponse20048 delete_peering_phone_numbers(body=body)

Remove peering phone numbers

Removes phone numbers added to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes**: `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ProviderExchangeApi(swagger_client.ApiClient(configuration))
body = swagger_client.PeeringNumbersBody1() # PeeringNumbersBody1 |  (optional)

try:
    # Remove peering phone numbers
    api_response = api_instance.delete_peering_phone_numbers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderExchangeApi->delete_peering_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PeeringNumbersBody1**](PeeringNumbersBody1.md)|  | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_carrier_peering_phone_numbers**
> InlineResponse20050 list_carrier_peering_phone_numbers(page_size=page_size, next_page_token=next_page_token, phone_number=phone_number)

List carrier peering phone numbers.

Returns phone numbers pushed by the carrier to different customers. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:read:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ProviderExchangeApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
phone_number = 'phone_number_example' # str | To filter results by the given phone number. (optional)

try:
    # List carrier peering phone numbers.
    api_response = api_instance.list_carrier_peering_phone_numbers(page_size=page_size, next_page_token=next_page_token, phone_number=phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderExchangeApi->list_carrier_peering_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **phone_number** | **str**| To filter results by the given phone number. | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_peering_phone_numbers**
> InlineResponse20047 list_peering_phone_numbers(page_size=page_size, next_page_token=next_page_token, phone_number=phone_number, carrier_code=carrier_code)

List peering phone numbers

Returns phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners who have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:read:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ProviderExchangeApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
phone_number = 'phone_number_example' # str | The sender's or receiver's phone number that limits the list of SMS sessions. (optional)
carrier_code = 56 # int | The carrier's code. The `clientId` that maps to a carrier peered with Zoom.  This parameter is required if you do **not** use an OAuth token or the OAuth token does not contain the `clientId`. (optional)

try:
    # List peering phone numbers
    api_response = api_instance.list_peering_phone_numbers(page_size=page_size, next_page_token=next_page_token, phone_number=phone_number, carrier_code=carrier_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderExchangeApi->list_peering_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **phone_number** | **str**| The sender&#x27;s or receiver&#x27;s phone number that limits the list of SMS sessions. | [optional] 
 **carrier_code** | **int**| The carrier&#x27;s code. The &#x60;clientId&#x60; that maps to a carrier peered with Zoom.  This parameter is required if you do **not** use an OAuth token or the OAuth token does not contain the &#x60;clientId&#x60;. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_peering_phone_numbers**
> InlineResponse20049 update_peering_phone_numbers(body=body)

Update peering phone numbers

Updates phone numbers to Zoom through the Provider Exchange.  **Note**: Phone peering API and events are for partners that have completed the MoU to peer with Zoom. To become a peering provider/ carrier, submit your [request](https://docs.google.com/forms/d/e/1FAIpQLSewkY6ixVyKVNkWC-vgmejC16gigxsJWXji3dWzE3XlWtjsgg/viewform).  **Scopes:** `phone_peering:write:admin`, `phone_peering:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ProviderExchangeApi(swagger_client.ApiClient(configuration))
body = swagger_client.PeeringNumbersBody2() # PeeringNumbersBody2 |  (optional)

try:
    # Update peering phone numbers
    api_response = api_instance.update_peering_phone_numbers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderExchangeApi->update_peering_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PeeringNumbersBody2**](PeeringNumbersBody2.md)|  | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

