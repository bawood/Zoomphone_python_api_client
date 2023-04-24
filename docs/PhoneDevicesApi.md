# swagger_client.PhoneDevicesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_extensions_to_a_device**](PhoneDevicesApi.md#add_extensions_to_a_device) | **POST** /phone/devices/{deviceId}/extensions | Assign an entity to a device
[**add_phone_device**](PhoneDevicesApi.md#add_phone_device) | **POST** /phone/devices | Add a device
[**delete_a_device**](PhoneDevicesApi.md#delete_a_device) | **DELETE** /phone/devices/{deviceId} | Delete a device
[**delete_extension_from_a_device**](PhoneDevicesApi.md#delete_extension_from_a_device) | **DELETE** /phone/devices/{deviceId}/extensions/{extensionId} | Unassign an entity from the device
[**get_a_device**](PhoneDevicesApi.md#get_a_device) | **GET** /phone/devices/{deviceId} | Get device details
[**list_phone_devices**](PhoneDevicesApi.md#list_phone_devices) | **GET** /phone/devices | List devices
[**reboot_phone_device**](PhoneDevicesApi.md#reboot_phone_device) | **POST** /phone/devices/{deviceId}/reboot | Reboot a desk phone
[**sync_phone_device**](PhoneDevicesApi.md#sync_phone_device) | **POST** /phone/devices/sync | Sync deskphones
[**update_a_device**](PhoneDevicesApi.md#update_a_device) | **PATCH** /phone/devices/{deviceId} | Update a device
[**update_provision_template_to_device**](PhoneDevicesApi.md#update_provision_template_to_device) | **PUT** /phone/devices/{deviceId}/provision_templates | Update provision template of a device

# **add_extensions_to_a_device**
> object add_extensions_to_a_device(device_id, body=body)

Assign an entity to a device

By default, all Zoom Phone users can make and receive calls using the Zoom desktop and mobile applications. Additionally, if a desk phone is required, use this API to [add a desk phone and assign it to a user](https://support.zoom.us/hc/en-us/articles/360021119092#h_5ca07504-68a8-4c3d-ad0e-c1d3594436da).  **Prerequisites:** * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique identifier of the device.
body = swagger_client.DeviceIdExtensionsBody() # DeviceIdExtensionsBody |  (optional)

try:
    # Assign an entity to a device
    api_response = api_instance.add_extensions_to_a_device(device_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->add_extensions_to_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique identifier of the device. | 
 **body** | [**DeviceIdExtensionsBody**](DeviceIdExtensionsBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_phone_device**
> InlineResponse20114 add_phone_device(body=body)

Add a device

By default, all Zoom Phone users can make and receive calls using the Zoom desktop and mobile applications. Additionally, if a desk phone is required, use this API to [add a desk phone and assign it](https://support.zoom.us/hc/en-us/articles/360021119092#h_5ca07504-68a8-4c3d-ad0e-c1d3594436da) to a user.  **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)  **Scopes:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneDevicesBody() # PhoneDevicesBody |  (optional)

try:
    # Add a device
    api_response = api_instance.add_phone_device(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->add_phone_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneDevicesBody**](PhoneDevicesBody.md)|  | [optional] 

### Return type

[**InlineResponse20114**](InlineResponse20114.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_device**
> object delete_a_device(device_id)

Delete a device

Remove a [desk phone device or ATA (Analog Telephone Adapter)](https://support.zoom.us/hc/en-us/articles/360021119092) from the Zoom Phone System Management.  **Prerequisites:** * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * Device must not have been assigned to a user.  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique identifier of the device.

try:
    # Delete a device
    api_response = api_instance.delete_a_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->delete_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique identifier of the device. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extension_from_a_device**
> delete_extension_from_a_device(device_id, extension_id)

Unassign an entity from the device

Use this API to unassign a specific assignee from the device.  **Prerequisites:** * Pro or a higher account with Zoom Phone license * Account owner or admin permissions.   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique identifier of the device from which to unassign an assignee.
extension_id = 'extension_id_example' # str | Extension ID of the assignee (`user` or `common area`)

try:
    # Unassign an entity from the device
    api_instance.delete_extension_from_a_device(device_id, extension_id)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->delete_extension_from_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique identifier of the device from which to unassign an assignee. | 
 **extension_id** | **str**| Extension ID of the assignee (&#x60;user&#x60; or &#x60;common area&#x60;) | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_device**
> InlineResponse20024 get_a_device(device_id)

Get device details

Gets detailed information about a specific [desk phone device](https://support.zoom.us/hc/en-us/articles/360021119092).  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:** * Pro or a higher account with Zoom Phone license * Account owner or admin permissions

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique Identifier of the device.

try:
    # Get device details
    api_response = api_instance.get_a_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->get_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique Identifier of the device. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_phone_devices**
> InlineResponse20023 list_phone_devices(type, assignee_type=assignee_type, device_source=device_source, location_status=location_status, site_id=site_id, device_type=device_type, next_page_token=next_page_token, page_size=page_size)

List devices

List all the [desk phone devices](https://support.zoom.us/hc/en-us/articles/360021119092) that are configured with Zoom Phone on an account.  **Scopes:** `phone:read:admin`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Device status: `assigned` or `unassigned` to list device status in Zoom account.
assignee_type = 'assignee_type_example' # str | Type of the assignee. Available if `type = assigned`. Unavailable if the account has not enabled the common area feature. Returns devices of the specified `assignee_type`. If unspecified, returns all assigned devices. (optional)
device_source = 'device_source_example' # str | Device source. `hotDesking` only available when `type = assigned`. (optional)
location_status = 'location_status_example' # str | The status of device location. Available if `type = assigned`. (optional)
site_id = 'site_id_example' # str | The site of the assignee. (optional)
device_type = 'device_type_example' # str | The manufacturer name or device type. (optional)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # List devices
    api_response = api_instance.list_phone_devices(type, assignee_type=assignee_type, device_source=device_source, location_status=location_status, site_id=site_id, device_type=device_type, next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->list_phone_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Device status: &#x60;assigned&#x60; or &#x60;unassigned&#x60; to list device status in Zoom account. | 
 **assignee_type** | **str**| Type of the assignee. Available if &#x60;type &#x3D; assigned&#x60;. Unavailable if the account has not enabled the common area feature. Returns devices of the specified &#x60;assignee_type&#x60;. If unspecified, returns all assigned devices. | [optional] 
 **device_source** | **str**| Device source. &#x60;hotDesking&#x60; only available when &#x60;type &#x3D; assigned&#x60;. | [optional] 
 **location_status** | **str**| The status of device location. Available if &#x60;type &#x3D; assigned&#x60;. | [optional] 
 **site_id** | **str**| The site of the assignee. | [optional] 
 **device_type** | **str**| The manufacturer name or device type. | [optional] 
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_phone_device**
> object reboot_phone_device(device_id)

Reboot a desk phone

Use this API to reboot an online zero-touch or assisted-provisioning device. You can only send one request every second.  **Prerequisites:** * Pro or a higher account with Zoom Phone license * Account owner or admin permissions.   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique identifier of the device.

try:
    # Reboot a desk phone
    api_response = api_instance.reboot_phone_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->reboot_phone_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique identifier of the device. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_phone_device**
> object sync_phone_device(body=body)

Sync deskphones

Use this API to resync all online zero-touch or assisted-provisioning devices in an account or a site. Only allows sending one request every 15 minutes.  **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DevicesSyncBody() # DevicesSyncBody |  (optional)

try:
    # Sync deskphones
    api_response = api_instance.sync_phone_device(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->sync_phone_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesSyncBody**](DevicesSyncBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_device**
> object update_a_device(device_id, body=body)

Update a device

Update information of a [desk phone device](https://support.zoom.us/hc/en-us/articles/360021119092).   **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions  **Scopes:** `phone:write:admin`      **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique identifier of the Device.
body = swagger_client.DevicesDeviceIdBody() # DevicesDeviceIdBody |  (optional)

try:
    # Update a device
    api_response = api_instance.update_a_device(device_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->update_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique identifier of the Device. | 
 **body** | [**DevicesDeviceIdBody**](DevicesDeviceIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provision_template_to_device**
> object update_provision_template_to_device(device_id, body=body)

Update provision template of a device

Use this API to [assign a provision template to a device](https://support.zoom.us/hc/en-us/articles/360035817952#h_6b52ef26-d070-40ed-a3fa-520571944afc) or [remove a provision template from the device](https://support.zoom.us/hc/en-us/articles/360035817952#h_7b34cd1d-5ae6-4a23-bd04-454a6ad8cb3e) by leaving `templateId` empty.  **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * [Supported device](https://support.zoom.us/hc/en-us/articles/360029698771#note)<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | The device ID.
body = swagger_client.DeviceIdProvisionTemplatesBody() # DeviceIdProvisionTemplatesBody |  (optional)

try:
    # Update provision template of a device
    api_response = api_instance.update_provision_template_to_device(device_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->update_provision_template_to_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The device ID. | 
 **body** | [**DeviceIdProvisionTemplatesBody**](DeviceIdProvisionTemplatesBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

