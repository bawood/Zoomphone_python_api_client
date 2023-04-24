# swagger_client.BillingAccountApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_a_billing_account**](BillingAccountApi.md#get_a_billing_account) | **GET** /phone/billing_accounts/{billingAccountId} | Get billing account details
[**list_billing_account**](BillingAccountApi.md#list_billing_account) | **GET** /phone/billing_accounts | List billing accounts

# **get_a_billing_account**
> InlineResponse200106 get_a_billing_account(billing_account_id)

Get billing account details

A Zoom account owner or a user with admin privilege can use this API to get information about a billing account.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.BillingAccountApi(swagger_client.ApiClient(configuration))
billing_account_id = 'billing_account_id_example' # str | The billing account ID.

try:
    # Get billing account details
    api_response = api_instance.get_a_billing_account(billing_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAccountApi->get_a_billing_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_id** | **str**| The billing account ID. | 

### Return type

[**InlineResponse200106**](InlineResponse200106.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_account**
> InlineResponse200105 list_billing_account()

List billing accounts

A Zoom account owner or a user with admin privileges can use this API to retrieve a list of billing accounts.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.BillingAccountApi(swagger_client.ApiClient(configuration))

try:
    # List billing accounts
    api_response = api_instance.list_billing_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAccountApi->list_billing_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200105**](InlineResponse200105.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

