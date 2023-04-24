# swagger_client.ProvisionTemplatesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_provision_template**](ProvisionTemplatesApi.md#add_provision_template) | **POST** /phone/provision_templates | Add a provision template
[**delete_provision_template**](ProvisionTemplatesApi.md#delete_provision_template) | **DELETE** /phone/provision_templates/{templateId} | Delete a provision template
[**get_provision_template**](ProvisionTemplatesApi.md#get_provision_template) | **GET** /phone/provision_templates/{templateId} | Get a provision template
[**list_account_provision_template**](ProvisionTemplatesApi.md#list_account_provision_template) | **GET** /phone/provision_templates | List provision templates
[**update_provision_template**](ProvisionTemplatesApi.md#update_provision_template) | **PATCH** /phone/provision_templates/{templateId} | Update a provision template

# **add_provision_template**
> InlineResponse20132 add_provision_template(body=body)

Add a provision template

Use this API to [create a provision template](https://support.zoom.us/hc/en-us/articles/360035817952#h_8266cb40-58fc-4c1a-8da2-885d72167234) in a Zoom account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.ProvisionTemplatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneProvisionTemplatesBody() # PhoneProvisionTemplatesBody |  (optional)

try:
    # Add a provision template
    api_response = api_instance.add_provision_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionTemplatesApi->add_provision_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneProvisionTemplatesBody**](PhoneProvisionTemplatesBody.md)|  | [optional] 

### Return type

[**InlineResponse20132**](InlineResponse20132.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provision_template**
> delete_provision_template(template_id)

Delete a provision template

Use this API to [delete a provision template](https://support.zoom.us/hc/en-us/articles/360035817952#h_7b34cd1d-5ae6-4a23-bd04-454a6ad8cb3e) in a Zoom account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.ProvisionTemplatesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | The template ID.

try:
    # Delete a provision template
    api_instance.delete_provision_template(template_id)
except ApiException as e:
    print("Exception when calling ProvisionTemplatesApi->delete_provision_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provision_template**
> InlineResponse200110 get_provision_template(template_id)

Get a provision template

Use this API to get a specific [provision template](https://support.zoom.us/hc/en-us/articles/360035817952).  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.ProvisionTemplatesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | The template ID.

try:
    # Get a provision template
    api_response = api_instance.get_provision_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionTemplatesApi->get_provision_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template ID. | 

### Return type

[**InlineResponse200110**](InlineResponse200110.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_provision_template**
> InlineResponse200109 list_account_provision_template(page_size=page_size, next_page_token=next_page_token)

List provision templates

Use this API to list all [provision templates](https://support.zoom.us/hc/en-us/articles/360035817952) in a Zoom account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.ProvisionTemplatesApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List provision templates
    api_response = api_instance.list_account_provision_template(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionTemplatesApi->list_account_provision_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse200109**](InlineResponse200109.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provision_template**
> update_provision_template(template_id, body=body)

Update a provision template

Use this API to update a [provision template](https://support.zoom.us/hc/en-us/articles/360035817952#h_7b34cd1d-5ae6-4a23-bd04-454a6ad8cb3e) in a Zoom account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.ProvisionTemplatesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 
body = swagger_client.ProvisionTemplatesTemplateIdBody() # ProvisionTemplatesTemplateIdBody |  (optional)

try:
    # Update a provision template
    api_instance.update_provision_template(template_id, body=body)
except ApiException as e:
    print("Exception when calling ProvisionTemplatesApi->update_provision_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **body** | [**ProvisionTemplatesTemplateIdBody**](ProvisionTemplatesTemplateIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

