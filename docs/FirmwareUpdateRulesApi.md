# swagger_client.FirmwareUpdateRulesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_firmware_rule**](FirmwareUpdateRulesApi.md#add_firmware_rule) | **POST** /phone/firmware_update_rules | Add a firmware update rule
[**delete_firmware_update_rule**](FirmwareUpdateRulesApi.md#delete_firmware_update_rule) | **DELETE** /phone/firmware_update_rules/{ruleId} | Delete firmware update rule
[**get_firmware_rule_detail**](FirmwareUpdateRulesApi.md#get_firmware_rule_detail) | **GET** /phone/firmware_update_rules/{ruleId} | Get firmware update rule information
[**list_firmware_rules**](FirmwareUpdateRulesApi.md#list_firmware_rules) | **GET** /phone/firmware_update_rules | List firmware update rules
[**list_firmwares**](FirmwareUpdateRulesApi.md#list_firmwares) | **GET** /phone/firmwares | List updatable firmwares
[**update_firmware_rule**](FirmwareUpdateRulesApi.md#update_firmware_rule) | **PATCH** /phone/firmware_update_rules/{ruleId} | Update firmware update rule

# **add_firmware_rule**
> InlineResponse20130 add_firmware_rule(body=body)

Add a firmware update rule

Use this API to add a [firmware update rule](https://support.zoom.us/hc/en-us/articles/360054198852-Setting-up-firmware-update-rules).  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.FirmwareUpdateRulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneFirmwareUpdateRulesBody() # PhoneFirmwareUpdateRulesBody |  (optional)

try:
    # Add a firmware update rule
    api_response = api_instance.add_firmware_rule(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwareUpdateRulesApi->add_firmware_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneFirmwareUpdateRulesBody**](PhoneFirmwareUpdateRulesBody.md)|  | [optional] 

### Return type

[**InlineResponse20130**](InlineResponse20130.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firmware_update_rule**
> delete_firmware_update_rule(rule_id, restart_type=restart_type)

Delete firmware update rule

Use this API to delete the [firmware update rule](https://support.zoom.us/hc/en-us/articles/360054198852-Setting-up-firmware-update-rules).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.FirmwareUpdateRulesApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | Unique identifier of the firmware update rule.
restart_type = 1 # int | Restart type: `1` - Restart the devices immediately. `2` - Restart with the next resync or auto pull. (optional) (default to 1)

try:
    # Delete firmware update rule
    api_instance.delete_firmware_update_rule(rule_id, restart_type=restart_type)
except ApiException as e:
    print("Exception when calling FirmwareUpdateRulesApi->delete_firmware_update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Unique identifier of the firmware update rule. | 
 **restart_type** | **int**| Restart type: &#x60;1&#x60; - Restart the devices immediately. &#x60;2&#x60; - Restart with the next resync or auto pull. | [optional] [default to 1]

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_rule_detail**
> InlineResponse200104 get_firmware_rule_detail(rule_id)

Get firmware update rule information

Use this API to get the [firmware update rule](https://support.zoom.us/hc/en-us/articles/360054198852-Setting-up-firmware-update-rules) information.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.FirmwareUpdateRulesApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | Unique identifier of the firmware update rule.

try:
    # Get firmware update rule information
    api_response = api_instance.get_firmware_rule_detail(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwareUpdateRulesApi->get_firmware_rule_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Unique identifier of the firmware update rule. | 

### Return type

[**InlineResponse200104**](InlineResponse200104.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firmware_rules**
> InlineResponse200103 list_firmware_rules(site_id=site_id, page_size=page_size, next_page_token=next_page_token)

List firmware update rules

Use this API to get [firmware update rules](https://support.zoom.us/hc/en-us/articles/360054198852-Setting-up-firmware-update-rules).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.FirmwareUpdateRulesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Required if multiple sites are enabled. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List firmware update rules
    api_response = api_instance.list_firmware_rules(site_id=site_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwareUpdateRulesApi->list_firmware_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Required if multiple sites are enabled. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse200103**](InlineResponse200103.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firmwares**
> InlineResponse200102 list_firmwares(is_update=is_update, site_id=site_id)

List updatable firmwares

Use this API to get updatable [firmwares](https://support.zoom.us/hc/en-us/articles/360054198852-Setting-up-firmware-update-rules).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.FirmwareUpdateRulesApi(swagger_client.ApiClient(configuration))
is_update = true # bool | Firmware update rule enabled.   `true` - Get all firmwares that can have firmware update rules added   `false` - Get all firmwares whether or not you can add firmware update rules to it (optional) (default to true)
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Required if multiple sites are enabled. (optional)

try:
    # List updatable firmwares
    api_response = api_instance.list_firmwares(is_update=is_update, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwareUpdateRulesApi->list_firmwares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_update** | **bool**| Firmware update rule enabled.   &#x60;true&#x60; - Get all firmwares that can have firmware update rules added   &#x60;false&#x60; - Get all firmwares whether or not you can add firmware update rules to it | [optional] [default to true]
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Required if multiple sites are enabled. | [optional] 

### Return type

[**InlineResponse200102**](InlineResponse200102.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firmware_rule**
> update_firmware_rule(rule_id, body=body)

Update firmware update rule

Use this API to update a specific [firmware update rule](https://support.zoom.us/hc/en-us/articles/360054198852-Setting-up-firmware-update-rules).  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.FirmwareUpdateRulesApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | Unique identifier of the firmware update rule.
body = swagger_client.FirmwareUpdateRulesRuleIdBody() # FirmwareUpdateRulesRuleIdBody |  (optional)

try:
    # Update firmware update rule
    api_instance.update_firmware_rule(rule_id, body=body)
except ApiException as e:
    print("Exception when calling FirmwareUpdateRulesApi->update_firmware_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Unique identifier of the firmware update rule. | 
 **body** | [**FirmwareUpdateRulesRuleIdBody**](FirmwareUpdateRulesRuleIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

