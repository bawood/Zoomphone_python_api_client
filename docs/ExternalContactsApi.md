# swagger_client.ExternalContactsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_external_contact**](ExternalContactsApi.md#add_external_contact) | **POST** /phone/external_contacts | Add an external contact
[**delete_a_external_contact**](ExternalContactsApi.md#delete_a_external_contact) | **DELETE** /phone/external_contacts/{externalContactId} | Delete an external contact
[**get_a_external_contact**](ExternalContactsApi.md#get_a_external_contact) | **GET** /phone/external_contacts/{externalContactId} | Get external contact details
[**list_external_contacts**](ExternalContactsApi.md#list_external_contacts) | **GET** /phone/external_contacts | List external contacts
[**update_external_contact**](ExternalContactsApi.md#update_external_contact) | **PATCH** /phone/external_contacts/{externalContactId} | Update external contact

# **add_external_contact**
> InlineResponse20117 add_external_contact(body=body)

Add an external contact

Adds an external contact.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.ExternalContactsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneExternalContactsBody() # PhoneExternalContactsBody |  (optional)

try:
    # Add an external contact
    api_response = api_instance.add_external_contact(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->add_external_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneExternalContactsBody**](PhoneExternalContactsBody.md)|  | [optional] 

### Return type

[**InlineResponse20117**](InlineResponse20117.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_external_contact**
> object delete_a_external_contact(external_contact_id)

Delete an external contact

Removes an external contact.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.ExternalContactsApi(swagger_client.ApiClient(configuration))
external_contact_id = 'external_contact_id_example' # str | The external contact's ID.

try:
    # Delete an external contact
    api_response = api_instance.delete_a_external_contact(external_contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_a_external_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_contact_id** | **str**| The external contact&#x27;s ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_external_contact**
> InlineResponse20033 get_a_external_contact(external_contact_id)

Get external contact details

Gets an external contact's information.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions<br>

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
api_instance = swagger_client.ExternalContactsApi(swagger_client.ApiClient(configuration))
external_contact_id = 'external_contact_id_example' # str | The external contact's ID.

try:
    # Get external contact details
    api_response = api_instance.get_a_external_contact(external_contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_a_external_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_contact_id** | **str**| The external contact&#x27;s ID. | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_contacts**
> InlineResponse20032 list_external_contacts(next_page_token=next_page_token, page_size=page_size)

List external contacts

Lists the external contacts.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.ExternalContactsApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # List external contacts
    api_response = api_instance.list_external_contacts(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->list_external_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_contact**
> object update_external_contact(external_contact_id, body=body)

Update external contact

Updates an external contact's information.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.ExternalContactsApi(swagger_client.ApiClient(configuration))
external_contact_id = 'external_contact_id_example' # str | The external contact ID.
body = swagger_client.ExternalContactsExternalContactIdBody() # ExternalContactsExternalContactIdBody |  (optional)

try:
    # Update external contact
    api_response = api_instance.update_external_contact(external_contact_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->update_external_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_contact_id** | **str**| The external contact ID. | 
 **body** | [**ExternalContactsExternalContactIdBody**](ExternalContactsExternalContactIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

