# swagger_client.LineKeysApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update_line_key_setting**](LineKeysApi.md#batch_update_line_key_setting) | **PATCH** /phone/extension/{extensionId}/line_keys | Batch update line key position and settings information
[**delete_line_key**](LineKeysApi.md#delete_line_key) | **DELETE** /phone/extension/{extensionId}/line_keys/{lineKeyId} | Delete a line key setting.
[**list_line_key_setting**](LineKeysApi.md#list_line_key_setting) | **GET** /phone/extension/{extensionId}/line_keys | Get line key position and settings information

# **batch_update_line_key_setting**
> object batch_update_line_key_setting(extension_id, body=body)

Batch update line key position and settings information

Use this API to batch update the Zoom Phone [line key settings](https://support.zoom.us/hc/en-us/articles/360040587552) information.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:write:admin` or `phone:write`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.LineKeysApi(swagger_client.ApiClient(configuration))
extension_id = 'extension_id_example' # str | The extension ID.
body = swagger_client.ExtensionIdLineKeysBody() # ExtensionIdLineKeysBody |  (optional)

try:
    # Batch update line key position and settings information
    api_response = api_instance.batch_update_line_key_setting(extension_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LineKeysApi->batch_update_line_key_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension ID. | 
 **body** | [**ExtensionIdLineKeysBody**](ExtensionIdLineKeysBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_line_key**
> object delete_line_key(extension_id, line_key_id)

Delete a line key setting.

Use this API to delete the Zoom Phone [line key settings](https://support.zoom.us/hc/en-us/articles/360040587552) information.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:write:admin` or `phone:write`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.LineKeysApi(swagger_client.ApiClient(configuration))
extension_id = 'extension_id_example' # str | The extension ID.
line_key_id = 'line_key_id_example' # str | Line key ID.

try:
    # Delete a line key setting.
    api_response = api_instance.delete_line_key(extension_id, line_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LineKeysApi->delete_line_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension ID. | 
 **line_key_id** | **str**| Line key ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_line_key_setting**
> InlineResponse20031 list_line_key_setting(extension_id)

Get line key position and settings information

Use this API to get the Zoom Phone [line key settings](https://support.zoom.us/hc/en-us/articles/360040587552) information.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:read:admin` or `phone:read`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.LineKeysApi(swagger_client.ApiClient(configuration))
extension_id = 'extension_id_example' # str | The extension ID.

try:
    # Get line key position and settings information
    api_response = api_instance.list_line_key_setting(extension_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LineKeysApi->list_line_key_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension ID. | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

