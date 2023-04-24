# swagger_client.DirectoryBackupRoutingRulesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_routing_rule**](DirectoryBackupRoutingRulesApi.md#add_routing_rule) | **POST** /phone/routing_rules | Add directory backup routing rule
[**delete_routing_rule**](DirectoryBackupRoutingRulesApi.md#delete_routing_rule) | **DELETE** /phone/routing_rules/{routingRuleId} | Delete directory backup routing rule
[**get_routing_rule**](DirectoryBackupRoutingRulesApi.md#get_routing_rule) | **GET** /phone/routing_rules/{routingRuleId} | Get directory backup routing rule
[**list_routing_rule**](DirectoryBackupRoutingRulesApi.md#list_routing_rule) | **GET** /phone/routing_rules | List directory backup routing rules
[**update_routing_rule**](DirectoryBackupRoutingRulesApi.md#update_routing_rule) | **PATCH** /phone/routing_rules/{routingRuleId} | Update directory backup routing rule

# **add_routing_rule**
> InlineResponse20121 add_routing_rule(body=body)

Add directory backup routing rule

Use this API to create a directory backup routing rule. The directory backup routing rules are a series of predefined Regular Expressions. These rules are used to route outgoing calls. If a dialed number does not match a Zoom Phone user, and does not match a defined External Contact, these rules are tested next. If a dialed number does not match any rules, the call will be routed via the PSTN.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.DirectoryBackupRoutingRulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneRoutingRulesBody() # PhoneRoutingRulesBody |  (optional)

try:
    # Add directory backup routing rule
    api_response = api_instance.add_routing_rule(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryBackupRoutingRulesApi->add_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneRoutingRulesBody**](PhoneRoutingRulesBody.md)|  | [optional] 

### Return type

[**InlineResponse20121**](InlineResponse20121.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_routing_rule**
> object delete_routing_rule(routing_rule_id)

Delete directory backup routing rule

Use this API to delete directory backup routing rule. The directory backup routing rules are a series of predefined Regular Expressions. These rules are used to route outgoing calls. If a dialed number does not match a Zoom Phone user, and does not match a defined External Contact, these rules are tested next. If a dialed number does not match any rules, the call will be routed via the PSTN.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.DirectoryBackupRoutingRulesApi(swagger_client.ApiClient(configuration))
routing_rule_id = 'routing_rule_id_example' # str | Unique identifier of the routing rule.

try:
    # Delete directory backup routing rule
    api_response = api_instance.delete_routing_rule(routing_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryBackupRoutingRulesApi->delete_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_rule_id** | **str**| Unique identifier of the routing rule. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_rule**
> InlineResponse20059 get_routing_rule(routing_rule_id)

Get directory backup routing rule

Use this API to get directory backup routing rule. The directory backup routing rules are a series of predefined Regular Expressions. These rules are used to route outgoing calls. If a dialed number does not match a Zoom Phone user, and does not match a defined External Contact, these rules are tested next. If a dialed number does not match any rules, the call will be routed via the PSTN.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.DirectoryBackupRoutingRulesApi(swagger_client.ApiClient(configuration))
routing_rule_id = 'routing_rule_id_example' # str | Unique identifier of the routing rule.

try:
    # Get directory backup routing rule
    api_response = api_instance.get_routing_rule(routing_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryBackupRoutingRulesApi->get_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_rule_id** | **str**| Unique identifier of the routing rule. | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_routing_rule**
> list[InlineResponse20058] list_routing_rule(site_id=site_id)

List directory backup routing rules

Use this API to return a list of directory backup routing rules. The directory backup routing rules are a series of predefined Regular Expressions. These rules are used to route outgoing calls. If a dialed number does not match a Zoom Phone user, and does not match a defined External Contact, these rules are tested next. If a dialed number does not match any rules, the call will be routed via the PSTN.   **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.DirectoryBackupRoutingRulesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the site. (optional)

try:
    # List directory backup routing rules
    api_response = api_instance.list_routing_rule(site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryBackupRoutingRulesApi->list_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the site. | [optional] 

### Return type

[**list[InlineResponse20058]**](InlineResponse20058.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_routing_rule**
> object update_routing_rule(routing_rule_id, body=body)

Update directory backup routing rule

Use this API to update directory backup routing rule. The directory backup routing rules are a series of predefined Regular Expressions. These rules are used to route outgoing calls. If a dialed number does not match a Zoom Phone user, and does not match a defined External Contact, these rules are tested next. If a dialed number does not match any rules, the call will be routed via the PSTN.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.DirectoryBackupRoutingRulesApi(swagger_client.ApiClient(configuration))
routing_rule_id = 'routing_rule_id_example' # str | Unique identifier of the routing rule.
body = swagger_client.RoutingRulesRoutingRuleIdBody() # RoutingRulesRoutingRuleIdBody |  (optional)

try:
    # Update directory backup routing rule
    api_response = api_instance.update_routing_rule(routing_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryBackupRoutingRulesApi->update_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_rule_id** | **str**| Unique identifier of the routing rule. | 
 **body** | [**RoutingRulesRoutingRuleIdBody**](RoutingRulesRoutingRuleIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

