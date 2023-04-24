# swagger_client.PhonePlansApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_calling_plans**](PhonePlansApi.md#list_calling_plans) | **GET** /phone/calling_plans | List calling plans
[**list_phone_plans**](PhonePlansApi.md#list_phone_plans) | **GET** /phone/plans | List plan information

# **list_calling_plans**
> InlineResponse20014 list_calling_plans()

List calling plans

Use this API to return all of an account's Zoom Phone [calling plans](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans).  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Pro or a higher account  * A Zoom Phone license

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
api_instance = swagger_client.PhonePlansApi(swagger_client.ApiClient(configuration))

try:
    # List calling plans
    api_response = api_instance.list_calling_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonePlansApi->list_calling_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_phone_plans**
> InlineResponse20015 list_phone_plans()

List plan information

Use this API to return all of an account's Zoom Phone [plan package](https://marketplace.zoom.us/docs/api-reference/other-references/plans#additional-zoom-phone-plans-and-codes), phone number usage and availability.  **Prerequisites:**  * A Pro or a higher account  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.PhonePlansApi(swagger_client.ApiClient(configuration))

try:
    # List plan information
    api_response = api_instance.list_phone_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonePlansApi->list_phone_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

