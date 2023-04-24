# swagger_client.EmergencyAddressesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_emergency_address**](EmergencyAddressesApi.md#add_emergency_address) | **POST** /phone/emergency_addresses | Add an emergency address
[**delete_emergency_address**](EmergencyAddressesApi.md#delete_emergency_address) | **DELETE** /phone/emergency_addresses/{emergencyAddressId} | Delete an emergency address
[**get_emergency_address**](EmergencyAddressesApi.md#get_emergency_address) | **GET** /phone/emergency_addresses/{emergencyAddressId} | Get emergency address details
[**list_emergency_addresses**](EmergencyAddressesApi.md#list_emergency_addresses) | **GET** /phone/emergency_addresses | List emergency addresses
[**update_emergency_address**](EmergencyAddressesApi.md#update_emergency_address) | **PATCH** /phone/emergency_addresses/{emergencyAddressId} | Update an emergency address

# **add_emergency_address**
> InlineResponse20115 add_emergency_address(body=body)

Add an emergency address

Adds an emergency address. If the address provided is not an exact match, the system generated corrected address will be used.   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyAddressesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneEmergencyAddressesBody() # PhoneEmergencyAddressesBody |  (optional)

try:
    # Add an emergency address
    api_response = api_instance.add_emergency_address(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyAddressesApi->add_emergency_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneEmergencyAddressesBody**](PhoneEmergencyAddressesBody.md)|  | [optional] 

### Return type

[**InlineResponse20115**](InlineResponse20115.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_emergency_address**
> object delete_emergency_address(emergency_address_id)

Delete an emergency address

Removes an emergency address.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyAddressesApi(swagger_client.ApiClient(configuration))
emergency_address_id = 'emergency_address_id_example' # str | The emergency address ID.

try:
    # Delete an emergency address
    api_response = api_instance.delete_emergency_address(emergency_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyAddressesApi->delete_emergency_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emergency_address_id** | **str**| The emergency address ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emergency_address**
> InlineResponse20027 get_emergency_address(emergency_address_id)

Get emergency address details

Gets the emergency address information.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions<br>

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
api_instance = swagger_client.EmergencyAddressesApi(swagger_client.ApiClient(configuration))
emergency_address_id = 'emergency_address_id_example' # str | The emergency address ID.

try:
    # Get emergency address details
    api_response = api_instance.get_emergency_address(emergency_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyAddressesApi->get_emergency_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emergency_address_id** | **str**| The emergency address ID. | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_emergency_addresses**
> InlineResponse20026 list_emergency_addresses(site_id=site_id, user_id=user_id, level=level, status=status, address_keyword=address_keyword, next_page_token=next_page_token, page_size=page_size)

List emergency addresses

Lists the emergency addresses.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyAddressesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The emergency address site ID. (optional)
user_id = 'user_id_example' # str | User ID to which the personal emergency address belongs. (optional)
level = 56 # int | The emergency address owner level:  * `0` - Account/Company-level emergency address.   * `1` - User/Personal-level emergency address.  * `2` - Unknown company/pending emergency address. (optional)
status = 56 # int | The emergency address verification status:  * `1` — Verification not Required.  * `2` — Unverified.  * `3` — Verification requested.  * `4` — Verified.  * `5` — Rejected.  * `6` — Verification failed. (optional)
address_keyword = 'address_keyword_example' # str | Keyword(s) to filter emergency addresses. You can filter by either:  * Address Line 1.  * Address Line 2.  * City.  * State Abbreviation.  * Zip Code. (optional)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # List emergency addresses
    api_response = api_instance.list_emergency_addresses(site_id=site_id, user_id=user_id, level=level, status=status, address_keyword=address_keyword, next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyAddressesApi->list_emergency_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The emergency address site ID. | [optional] 
 **user_id** | **str**| User ID to which the personal emergency address belongs. | [optional] 
 **level** | **int**| The emergency address owner level:  * &#x60;0&#x60; - Account/Company-level emergency address.   * &#x60;1&#x60; - User/Personal-level emergency address.  * &#x60;2&#x60; - Unknown company/pending emergency address. | [optional] 
 **status** | **int**| The emergency address verification status:  * &#x60;1&#x60; — Verification not Required.  * &#x60;2&#x60; — Unverified.  * &#x60;3&#x60; — Verification requested.  * &#x60;4&#x60; — Verified.  * &#x60;5&#x60; — Rejected.  * &#x60;6&#x60; — Verification failed. | [optional] 
 **address_keyword** | **str**| Keyword(s) to filter emergency addresses. You can filter by either:  * Address Line 1.  * Address Line 2.  * City.  * State Abbreviation.  * Zip Code. | [optional] 
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_emergency_address**
> InlineResponse20028 update_emergency_address(emergency_address_id, body=body)

Update an emergency address

Updates an emergency address information. If the address provided is not an exact match, the system generated corrected address will be used.   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyAddressesApi(swagger_client.ApiClient(configuration))
emergency_address_id = 'emergency_address_id_example' # str | The ID of the emergency address.
body = swagger_client.EmergencyAddressesEmergencyAddressIdBody() # EmergencyAddressesEmergencyAddressIdBody |  (optional)

try:
    # Update an emergency address
    api_response = api_instance.update_emergency_address(emergency_address_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyAddressesApi->update_emergency_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emergency_address_id** | **str**| The ID of the emergency address. | 
 **body** | [**EmergencyAddressesEmergencyAddressIdBody**](EmergencyAddressesEmergencyAddressIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

