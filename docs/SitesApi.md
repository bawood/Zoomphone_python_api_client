# swagger_client.SitesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_site_outbound_caller_numbers**](SitesApi.md#add_site_outbound_caller_numbers) | **POST** /phone/sites/{siteId}/outbound_caller_id/customized_numbers | Add customized outbound caller ID phone numbers
[**add_site_setting**](SitesApi.md#add_site_setting) | **POST** /phone/sites/{siteId}/settings/{settingType} | Add a site setting
[**create_phone_site**](SitesApi.md#create_phone_site) | **POST** /phone/sites | Create a phone site
[**delete_phone_site**](SitesApi.md#delete_phone_site) | **DELETE** /phone/sites/{siteId} | Delete a phone site
[**delete_site_outbound_caller_numbers**](SitesApi.md#delete_site_outbound_caller_numbers) | **DELETE** /phone/sites/{siteId}/outbound_caller_id/customized_numbers | Remove customized outbound caller ID phone numbers
[**delete_site_setting**](SitesApi.md#delete_site_setting) | **DELETE** /phone/sites/{siteId}/settings/{settingType} | Delete a site setting
[**get_a_site**](SitesApi.md#get_a_site) | **GET** /phone/sites/{siteId} | Get phone site details
[**get_site_policy_details**](SitesApi.md#get_site_policy_details) | **GET** /phone/sites/{siteId}/policies/{policyType} | Get site policy details
[**get_site_setting_for_type**](SitesApi.md#get_site_setting_for_type) | **GET** /phone/sites/{siteId}/settings/{settingType} | Get a phone site setting
[**list_phone_sites**](SitesApi.md#list_phone_sites) | **GET** /phone/sites | List phone sites
[**list_site_customize_outbound_caller_numbers**](SitesApi.md#list_site_customize_outbound_caller_numbers) | **GET** /phone/sites/{siteId}/outbound_caller_id/customized_numbers | List customized outbound caller ID phone numbers
[**update_site_details**](SitesApi.md#update_site_details) | **PATCH** /phone/sites/{siteId} | Update phone site details
[**update_site_policy**](SitesApi.md#update_site_policy) | **PATCH** /phone/sites/{siteId}/policies/{policyType} | Update site policy
[**update_site_setting**](SitesApi.md#update_site_setting) | **PATCH** /phone/sites/{siteId}/settings/{settingType} | Update the site setting

# **add_site_outbound_caller_numbers**
> object add_site_outbound_caller_numbers(site_id, body=body)

Add customized outbound caller ID phone numbers

Use this API to add the `site-level` customized outbound caller ID phone numbers.  * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
body = swagger_client.OutboundCallerIdCustomizedNumbersBody1() # OutboundCallerIdCustomizedNumbersBody1 |  (optional)

try:
    # Add customized outbound caller ID phone numbers
    api_response = api_instance.add_site_outbound_caller_numbers(site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->add_site_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **body** | [**OutboundCallerIdCustomizedNumbersBody1**](OutboundCallerIdCustomizedNumbersBody1.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_site_setting**
> InlineResponse20124 add_site_setting(site_id, setting_type, body=body)

Add a site setting

Sites allow you to organize Zoom Phone users in your organization. Use this API to add a site setting to a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672) according to the setting type.  **Prerequisites:**  * Account must have a Pro or a higher plan with Zoom Phone license. * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
setting_type = 'setting_type_example' # str | The site setting type:  * `holiday_hours`  * `security`.
body = swagger_client.SettingsSettingTypeBody4() # SettingsSettingTypeBody4 |  (optional)

try:
    # Add a site setting
    api_response = api_instance.add_site_setting(site_id, setting_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->add_site_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **setting_type** | **str**| The site setting type:  * &#x60;holiday_hours&#x60;  * &#x60;security&#x60;. | 
 **body** | [**SettingsSettingTypeBody4**](SettingsSettingTypeBody4.md)|  | [optional] 

### Return type

[**InlineResponse20124**](InlineResponse20124.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phone_site**
> InlineResponse204 create_phone_site(body=body)

Create a phone site

Use this API to create a [site](https://support.zoom.us/hc/en-us/articles/360020809672). It allows you to organize the Zoom Phone users in your organization.  **Prerequisites:** * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).  * Pro or a higher account with Zoom Phone enabled.  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneSitesBody() # PhoneSitesBody |  (optional)

try:
    # Create a phone site
    api_response = api_instance.create_phone_site(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->create_phone_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneSitesBody**](PhoneSitesBody.md)|  | [optional] 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_phone_site**
> object delete_phone_site(site_id, transfer_site_id)

Delete a phone site

 Use this API to delete a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672) in a Zoom account. To delete a site, in the query parameter, you must provide the site ID of another site where the assets of current site (users, numbers and phones) can be transferred to.  You cannot use this API to delete the main site.  **Prerequisites:**   * Account must have a Pro or a higher plan with Zoom Phone license.  * [Multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites) must be enabled.  **Scope:** `phone:write:admin`     **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The unique identifier of the site.
transfer_site_id = 'transfer_site_id_example' # str | The site ID of another site where the assets of the current site (users, numbers and phones) can be transferred.

try:
    # Delete a phone site
    api_response = api_instance.delete_phone_site(site_id, transfer_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->delete_phone_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The unique identifier of the site. | 
 **transfer_site_id** | **str**| The site ID of another site where the assets of the current site (users, numbers and phones) can be transferred. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_outbound_caller_numbers**
> object delete_site_outbound_caller_numbers(site_id, customize_ids=customize_ids)

Remove customized outbound caller ID phone numbers

Use this API to remove the `site-level` customized outbound caller ID phone numbers.  * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
customize_ids = ['customize_ids_example'] # list[str] | The customization IDs. (optional)

try:
    # Remove customized outbound caller ID phone numbers
    api_response = api_instance.delete_site_outbound_caller_numbers(site_id, customize_ids=customize_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->delete_site_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **customize_ids** | [**list[str]**](str.md)| The customization IDs. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_setting**
> object delete_site_setting(site_id, setting_type, device_type=device_type, holiday_id=holiday_id)

Delete a site setting

Sites allow you to organize Zoom Phone users in your organization. Use this API to delete the site setting of a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672).  **Prerequisites:**  * Account must have a Pro or a higher plan with Zoom Phone license. * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
setting_type = 'setting_type_example' # str | The site setting type:  * `holiday_hours`  * `security`.
device_type = 'device_type_example' # str | The device type. Enable SRTP AES-256 encryption on the site for the specified device type. Used for `security` setting type. (optional)
holiday_id = 'holiday_id_example' # str | The holiday hour setting ID.  Used for `holiday_hours` setting type. (optional)

try:
    # Delete a site setting
    api_response = api_instance.delete_site_setting(site_id, setting_type, device_type=device_type, holiday_id=holiday_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->delete_site_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **setting_type** | **str**| The site setting type:  * &#x60;holiday_hours&#x60;  * &#x60;security&#x60;. | 
 **device_type** | **str**| The device type. Enable SRTP AES-256 encryption on the site for the specified device type. Used for &#x60;security&#x60; setting type. | [optional] 
 **holiday_id** | **str**| The holiday hour setting ID.  Used for &#x60;holiday_hours&#x60; setting type. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_site**
> InlineResponse20069 get_a_site(site_id)

Get phone site details

Sites allow you to organize Zoom Phone users in your organization. Use this API to get information on a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672).  **Prerequisites:**  * Account must have a Pro or a higher plan with Zoom Phone license. * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).  **Scope:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The unique identifier of the site.

try:
    # Get phone site details
    api_response = api_instance.get_a_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_a_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The unique identifier of the site. | 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_policy_details**
> InlineResponse20071 get_site_policy_details(site_id, policy_type, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)

Get site policy details

Use this API to get the site policy details.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
policy_type = 'policy_type_example' # str | The site policy type: `restricted_call_hours`, `allowed_call_locations`.
sub_policy_type = 'sub_policy_type_example' # str | The sub policy type: `restricted_holiday_hours`, `allowed_call_locations_places`.  The `restricted_holiday_hours` sub policy type is for policy type `restricted_call_hours`.  The `allowed_call_locations_places` sub policy type is for policy type `allowed_call_locations`. (optional)
holiday_hours_site_id = 'holiday_hours_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `restricted_holiday_hours`. (optional)
locations_site_id = 'locations_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `allowed_call_locations_places`. (optional)

try:
    # Get site policy details
    api_response = api_instance.get_site_policy_details(site_id, policy_type, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_site_policy_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **policy_type** | **str**| The site policy type: &#x60;restricted_call_hours&#x60;, &#x60;allowed_call_locations&#x60;. | 
 **sub_policy_type** | **str**| The sub policy type: &#x60;restricted_holiday_hours&#x60;, &#x60;allowed_call_locations_places&#x60;.  The &#x60;restricted_holiday_hours&#x60; sub policy type is for policy type &#x60;restricted_call_hours&#x60;.  The &#x60;allowed_call_locations_places&#x60; sub policy type is for policy type &#x60;allowed_call_locations&#x60;. | [optional] 
 **holiday_hours_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;restricted_holiday_hours&#x60;. | [optional] 
 **locations_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;allowed_call_locations_places&#x60;. | [optional] 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_setting_for_type**
> InlineResponse20070 get_site_setting_for_type(site_id, setting_type)

Get a phone site setting

Sites allow you to organize Zoom Phone users in your organization. Use this API to get site setting about a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672) according to the setting type.  **Prerequisites:**   * Account must have a Pro or a higher plan with Zoom Phone license. * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).  **Scope:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
setting_type = 'setting_type_example' # str | The site setting type:  * `local_based_routing`  * `business_hours`  * `closed_hours`  * `holiday_hours`  * `security`  * `outbound_caller_id`  * `audio_prompt`  * `desk_phone`  * `dial_by_name`  * `billing_account`

try:
    # Get a phone site setting
    api_response = api_instance.get_site_setting_for_type(site_id, setting_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_site_setting_for_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **setting_type** | **str**| The site setting type:  * &#x60;local_based_routing&#x60;  * &#x60;business_hours&#x60;  * &#x60;closed_hours&#x60;  * &#x60;holiday_hours&#x60;  * &#x60;security&#x60;  * &#x60;outbound_caller_id&#x60;  * &#x60;audio_prompt&#x60;  * &#x60;desk_phone&#x60;  * &#x60;dial_by_name&#x60;  * &#x60;billing_account&#x60; | 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_phone_sites**
> InlineResponse20068 list_phone_sites(page_size=page_size, next_page_token=next_page_token)

List phone sites

Sites allow you to organize Zoom Phone users in your organization. Use this API to list all the [sites](https://support.zoom.us/hc/en-us/articles/360020809672) that have been created for an account.<br> **Prerequisites:**<br> * Multiple Sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15). * Pro or a higher account with Zoom Phone enabled.   **Scope:** `phone:read:admin`<br>   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List phone sites
    api_response = api_instance.list_phone_sites(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->list_phone_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_site_customize_outbound_caller_numbers**
> InlineResponse20072 list_site_customize_outbound_caller_numbers(site_id, selected=selected, site_id=site_id, extension_type=extension_type, keyword=keyword, page_size=page_size, next_page_token=next_page_token)

List customized outbound caller ID phone numbers

Use this API to retrieve phone numbers that can be used as the `site-level` customized outbound caller ID.  * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
selected = true # bool | Status of the phone numbers.<br>`true`- Numbers already added to the custom list. <br>`false`- Numbers not yet added to the custom list (optional)
site_id = 'site_id_example' # str | For filtering phone numbers that belong to the site. (optional)
extension_type = 'extension_type_example' # str | The type of the extension to which the phone number belongs. (optional)
keyword = 'keyword_example' # str | A search keyword for phone or extension numbers. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List customized outbound caller ID phone numbers
    api_response = api_instance.list_site_customize_outbound_caller_numbers(site_id, selected=selected, site_id=site_id, extension_type=extension_type, keyword=keyword, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->list_site_customize_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **selected** | **bool**| Status of the phone numbers.&lt;br&gt;&#x60;true&#x60;- Numbers already added to the custom list. &lt;br&gt;&#x60;false&#x60;- Numbers not yet added to the custom list | [optional] 
 **site_id** | **str**| For filtering phone numbers that belong to the site. | [optional] 
 **extension_type** | **str**| The type of the extension to which the phone number belongs. | [optional] 
 **keyword** | **str**| A search keyword for phone or extension numbers. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_details**
> object update_site_details(site_id, body=body)

Update phone site details

Allows you to organize Zoom Phone users in your organization. Use this API to update information about a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672).   **Prerequisites:**   * Account must have a Pro or a higher plan with Zoom Phone license. * **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the site.
body = swagger_client.SitesSiteIdBody1() # SitesSiteIdBody1 |  (optional)

try:
    # Update phone site details
    api_response = api_instance.update_site_details(site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->update_site_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the site. | 
 **body** | [**SitesSiteIdBody1**](SitesSiteIdBody1.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_policy**
> object update_site_policy(site_id, policy_type, body=body, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)

Update site policy

Use this API to update a site's [Zoom Phone](https://support.zoom.us/hc/en-us/categories/360001370051-Zoom-Phone) policy.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
policy_type = 'policy_type_example' # str | The site policy type: `restricted_call_hours`, `allowed_call_locations`.
body = swagger_client.PoliciesPolicyTypeBody5() # PoliciesPolicyTypeBody5 |  (optional)
sub_policy_type = 'sub_policy_type_example' # str | The sub policy type: `restricted_holiday_hours`, `allowed_call_locations_places`.  The `restricted_holiday_hours` sub policy type is for policy type `restricted_call_hours`.  The `allowed_call_locations_places` sub policy type is for policy type `allowed_call_locations`. (optional)
holiday_hours_site_id = 'holiday_hours_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `restricted_holiday_hours`. (optional)
locations_site_id = 'locations_site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type `allowed_call_locations_places`. (optional)

try:
    # Update site policy
    api_response = api_instance.update_site_policy(site_id, policy_type, body=body, sub_policy_type=sub_policy_type, holiday_hours_site_id=holiday_hours_site_id, locations_site_id=locations_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->update_site_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **policy_type** | **str**| The site policy type: &#x60;restricted_call_hours&#x60;, &#x60;allowed_call_locations&#x60;. | 
 **body** | [**PoliciesPolicyTypeBody5**](PoliciesPolicyTypeBody5.md)|  | [optional] 
 **sub_policy_type** | **str**| The sub policy type: &#x60;restricted_holiday_hours&#x60;, &#x60;allowed_call_locations_places&#x60;.  The &#x60;restricted_holiday_hours&#x60; sub policy type is for policy type &#x60;restricted_call_hours&#x60;.  The &#x60;allowed_call_locations_places&#x60; sub policy type is for policy type &#x60;allowed_call_locations&#x60;. | [optional] 
 **holiday_hours_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;restricted_holiday_hours&#x60;. | [optional] 
 **locations_site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for sub policy type &#x60;allowed_call_locations_places&#x60;. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_setting**
> object update_site_setting(site_id, setting_type, body=body)

Update the site setting

Sites allow you to organize Zoom Phone users in your organization. Use this API to update the site setting of a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672) according to the setting type.  **Prerequisites:**  * Account must have a Pro or a higher plan with Zoom Phone license. * Multiple sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | The site ID.
setting_type = 'setting_type_example' # str | The site setting type:  * `local_based_routing`  * `business_hours`  * `closed_hours`  * `holiday_hours` * `outbound_caller_id`  * `audio_prompt`  * `desk_phone`  * `dial_by_name`  * `billing_account`
body = swagger_client.SettingsSettingTypeBody5() # SettingsSettingTypeBody5 |  (optional)

try:
    # Update the site setting
    api_response = api_instance.update_site_setting(site_id, setting_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->update_site_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site ID. | 
 **setting_type** | **str**| The site setting type:  * &#x60;local_based_routing&#x60;  * &#x60;business_hours&#x60;  * &#x60;closed_hours&#x60;  * &#x60;holiday_hours&#x60; * &#x60;outbound_caller_id&#x60;  * &#x60;audio_prompt&#x60;  * &#x60;desk_phone&#x60;  * &#x60;dial_by_name&#x60;  * &#x60;billing_account&#x60; | 
 **body** | [**SettingsSettingTypeBody5**](SettingsSettingTypeBody5.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

