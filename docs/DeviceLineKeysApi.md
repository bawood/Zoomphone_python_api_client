# swagger_client.DeviceLineKeysApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update_device_line_key_setting**](DeviceLineKeysApi.md#batch_update_device_line_key_setting) | **PATCH** /phone/devices/{deviceId}/line_keys | Batch update device line key position
[**list_device_line_key_setting**](DeviceLineKeysApi.md#list_device_line_key_setting) | **GET** /phone/devices/{deviceId}/line_keys | Get device line keys information

# **batch_update_device_line_key_setting**
> object batch_update_device_line_key_setting(device_id, body=body)

Batch update device line key position

Use this API to batch update the Zoom Phone device [line key position](https://support.zoom.us/hc/en-us/articles/4402415568397-Customizing-keys-for-devices-with-multiple-users) information.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:write:admin` or `phone:write`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`

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
api_instance = swagger_client.DeviceLineKeysApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | The device ID.
body = swagger_client.DeviceIdLineKeysBody() # DeviceIdLineKeysBody |  (optional)

try:
    # Batch update device line key position
    api_response = api_instance.batch_update_device_line_key_setting(device_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceLineKeysApi->batch_update_device_line_key_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The device ID. | 
 **body** | [**DeviceIdLineKeysBody**](DeviceIdLineKeysBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_device_line_key_setting**
> InlineResponse20025 list_device_line_key_setting(device_id)

Get device line keys information

Use this API to get information on the Zoom Phone device [line keys](https://support.zoom.us/hc/en-us/articles/4402415568397-Customizing-keys-for-devices-with-multiple-users) settings and position.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:read:admin` or `phone:read`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`

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
api_instance = swagger_client.DeviceLineKeysApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | The device ID.

try:
    # Get device line keys information
    api_response = api_instance.list_device_line_key_setting(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceLineKeysApi->list_device_line_key_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The device ID. | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

