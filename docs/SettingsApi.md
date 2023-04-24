# swagger_client.SettingsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_main_company_number**](SettingsApi.md#change_main_company_number) | **PUT** /phone/company_number | Change main company number
[**get_ported_numbers_details**](SettingsApi.md#get_ported_numbers_details) | **GET** /phone/ported_numbers/orders/{orderId} | Get ported number details
[**list_byocsip_trunk**](SettingsApi.md#list_byocsip_trunk) | **GET** /phone/sip_trunk/trunks | List BYOC SIP trunks
[**list_ported_numbers**](SettingsApi.md#list_ported_numbers) | **GET** /phone/ported_numbers/orders | List ported numbers
[**list_sip_groups**](SettingsApi.md#list_sip_groups) | **GET** /phone/sip_groups | List SIP groups
[**phone_setting**](SettingsApi.md#phone_setting) | **GET** /phone/settings | Get phone account settings
[**update_phone_settings**](SettingsApi.md#update_phone_settings) | **PATCH** /phone/settings | Update phone account settings

# **change_main_company_number**
> object change_main_company_number(body=body)

Change main company number

Use this API to [change an account's main company number](https://support.zoom.us/hc/en-us/articles/360028553691#h_82414c34-9df2-428a-85a4-efcf7f9e0d72).  External users can use the [main company number](https://support.zoom.us/hc/en-us/articles/360028553691) to reach your Zoom Phone users by dialing the main company number and the user's extension. It can also be used by your account's Zoom Phone users as their caller ID when making calls.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * Account owner or admin permissions

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneCompanyNumberBody() # PhoneCompanyNumberBody |  (optional)

try:
    # Change main company number
    api_response = api_instance.change_main_company_number(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->change_main_company_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneCompanyNumberBody**](PhoneCompanyNumberBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ported_numbers_details**
> InlineResponse20052 get_ported_numbers_details(order_id)

Get ported number details

Use this API to get details on the ported numbers by specifying `order_id`.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom phone license

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
order_id = 'order_id_example' # str | Order ID of the ported numbers. This can be retrieved from the List Ported Numbers API.

try:
    # Get ported number details
    api_response = api_instance.get_ported_numbers_details(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_ported_numbers_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID of the ported numbers. This can be retrieved from the List Ported Numbers API. | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_byocsip_trunk**
> InlineResponse20067 list_byocsip_trunk(next_page_token=next_page_token, page_size=page_size)

List BYOC SIP trunks

Use this API to return a list of an account's assigned [BYOC (Bring Your Own Carrier) SIP (Session Initiation Protocol) trunks](https://zoom.us/docs/doc/Zoom-Bring%20Your%20Own%20Carrier.pdf).  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # List BYOC SIP trunks
    api_response = api_instance.list_byocsip_trunk(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->list_byocsip_trunk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ported_numbers**
> InlineResponse20051 list_ported_numbers(next_page_token=next_page_token, page_size=page_size)

List ported numbers

Use this API to list ported numbers in a Zoom account.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # List ported numbers
    api_response = api_instance.list_ported_numbers(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->list_ported_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_groups**
> InlineResponse20066 list_sip_groups(next_page_token=next_page_token, page_size=page_size)

List SIP groups

Use this API to list SIP (Session Initiation Protocol) groups.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # List SIP groups
    api_response = api_instance.list_sip_groups(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->list_sip_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_setting**
> InlineResponse20062 phone_setting()

Get phone account settings

Use this API to return an account's settings.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:** * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))

try:
    # Get phone account settings
    api_response = api_instance.phone_setting()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->phone_setting: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_settings**
> object update_phone_settings(account_id, body=body)

Update phone account settings

Account owners can use this API to update Zoom Phone [account settings](https://support.zoom.us/hc/en-us/articles/360025846692).  **Scopes:** `phone:write:admin`  **Prerequisites:**  * A Business or Enterprise account

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The sub account ID.
body = swagger_client.PhoneSettingsBody() # PhoneSettingsBody |  (optional)

try:
    # Update phone account settings
    api_response = api_instance.update_phone_settings(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->update_phone_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The sub account ID. | 
 **body** | [**PhoneSettingsBody**](PhoneSettingsBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

