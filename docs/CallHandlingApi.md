# swagger_client.CallHandlingApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_call_handling**](CallHandlingApi.md#add_call_handling) | **POST** /phone/extension/{extensionId}/call_handling/settings/{settingType} | Add a call handling setting
[**delete_call_handling**](CallHandlingApi.md#delete_call_handling) | **DELETE** /phone/extension/{extensionId}/call_handling/settings/{settingType} | Delete a call handling setting
[**get_call_handling**](CallHandlingApi.md#get_call_handling) | **GET** /phone/extension/{extensionId}/call_handling/settings | Get call handling settings
[**update_call_handling**](CallHandlingApi.md#update_call_handling) | **PATCH** /phone/extension/{extensionId}/call_handling/settings/{settingType} | Update a call handling setting

# **add_call_handling**
> InlineResponse20116 add_call_handling(extension_id, setting_type, body=body)

Add a call handling setting

Adds Zoom Phone call handling subsettings for your phone system. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or a higher account with Zoom Phone enabled

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
api_instance = swagger_client.CallHandlingApi(swagger_client.ApiClient(configuration))
extension_id = 'extension_id_example' # str | The extension ID.
setting_type = 'setting_type_example' # str | The call handling setting type:  * `business_hours`  * `closed_hours`  * `holiday_hours`
body = swagger_client.SettingsSettingTypeBody2() # SettingsSettingTypeBody2 |  (optional)

try:
    # Add a call handling setting
    api_response = api_instance.add_call_handling(extension_id, setting_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallHandlingApi->add_call_handling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension ID. | 
 **setting_type** | **str**| The call handling setting type:  * &#x60;business_hours&#x60;  * &#x60;closed_hours&#x60;  * &#x60;holiday_hours&#x60; | 
 **body** | [**SettingsSettingTypeBody2**](SettingsSettingTypeBody2.md)|  | [optional] 

### Return type

[**InlineResponse20116**](InlineResponse20116.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_call_handling**
> delete_call_handling(extension_id, setting_type, call_forwarding_id=call_forwarding_id, holiday_id=holiday_id)

Delete a call handling setting

Deletes a Zoom Phone's call handling settings. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled

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
api_instance = swagger_client.CallHandlingApi(swagger_client.ApiClient(configuration))
extension_id = 'extension_id_example' # str | The extension ID.
setting_type = 'setting_type_example' # str | The type of call handling setting:  * `business_hours`  * `closed_hours`  * `holiday_hours`
call_forwarding_id = 'call_forwarding_id_example' # str | The call forwarding's ID. Use this parameter if you pass the `call_forwarding_id` value for the `settingType` parameter. (optional)
holiday_id = 'holiday_id_example' # str | The holiday's ID. Use this parameter if you pass the `holiday_id` value for the `settingType` parameter. (optional)

try:
    # Delete a call handling setting
    api_instance.delete_call_handling(extension_id, setting_type, call_forwarding_id=call_forwarding_id, holiday_id=holiday_id)
except ApiException as e:
    print("Exception when calling CallHandlingApi->delete_call_handling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension ID. | 
 **setting_type** | **str**| The type of call handling setting:  * &#x60;business_hours&#x60;  * &#x60;closed_hours&#x60;  * &#x60;holiday_hours&#x60; | 
 **call_forwarding_id** | **str**| The call forwarding&#x27;s ID. Use this parameter if you pass the &#x60;call_forwarding_id&#x60; value for the &#x60;settingType&#x60; parameter. | [optional] 
 **holiday_id** | **str**| The holiday&#x27;s ID. Use this parameter if you pass the &#x60;holiday_id&#x60; value for the &#x60;settingType&#x60; parameter. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_handling**
> InlineResponse20030 get_call_handling(extension_id)

Get call handling settings

Gets information about a Zoom Phone's call handling settings. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled

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
api_instance = swagger_client.CallHandlingApi(swagger_client.ApiClient(configuration))
extension_id = 'extension_id_example' # str | The extension ID.

try:
    # Get call handling settings
    api_response = api_instance.get_call_handling(extension_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallHandlingApi->get_call_handling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension ID. | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_handling**
> update_call_handling(extension_id, setting_type, body=body)

Update a call handling setting

Updates a Zoom Phone's call handling setting. Call handling settings let you control how your system routes calls during business, closed, or holiday hours. For more information, read our [API guide](https://marketplace.zoom.us/docs/guides/zoom-phone/call-handling/) or Zoom support article [Customizing call handling settings](https://support.zoom.us/hc/en-us/articles/360059966372-Customizing-call-handling-settings).  **Applicable to user, call queue, or auto receptionist call handling at this time.**   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone enabled

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
api_instance = swagger_client.CallHandlingApi(swagger_client.ApiClient(configuration))
extension_id = 'extension_id_example' # str | The extension ID.
setting_type = 'setting_type_example' # str | The call handling setting type:  * `business_hours`  * `closed_hours`  * `holiday_hours`
body = swagger_client.SettingsSettingTypeBody3() # SettingsSettingTypeBody3 |  (optional)

try:
    # Update a call handling setting
    api_instance.update_call_handling(extension_id, setting_type, body=body)
except ApiException as e:
    print("Exception when calling CallHandlingApi->update_call_handling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension ID. | 
 **setting_type** | **str**| The call handling setting type:  * &#x60;business_hours&#x60;  * &#x60;closed_hours&#x60;  * &#x60;holiday_hours&#x60; | 
 **body** | [**SettingsSettingTypeBody3**](SettingsSettingTypeBody3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

