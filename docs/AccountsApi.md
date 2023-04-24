# swagger_client.AccountsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_outbound_caller_numbers**](AccountsApi.md#add_outbound_caller_numbers) | **POST** /phone/outbound_caller_id/customized_numbers | Add phone numbers for an account&#x27;s customized outbound caller ID
[**delete_outbound_caller_numbers**](AccountsApi.md#delete_outbound_caller_numbers) | **DELETE** /phone/outbound_caller_id/customized_numbers | Delete phone numbers for an account&#x27;s customized outbound caller ID
[**list_customize_outbound_caller_numbers**](AccountsApi.md#list_customize_outbound_caller_numbers) | **GET** /phone/outbound_caller_id/customized_numbers | List an account&#x27;s customized outbound caller ID phone numbers
[**list_zoom_phone_account_settings**](AccountsApi.md#list_zoom_phone_account_settings) | **GET** /phone/account_settings | List an account&#x27;s zoom phone settings

# **add_outbound_caller_numbers**
> object add_outbound_caller_numbers(body=body)

Add phone numbers for an account's customized outbound caller ID

Adds the `account-level` customized outbound caller ID phone numbers. Note that when multiple sites policy is enabled, users cannot manage the `account-level` configuration. The system will throw an exception.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OutboundCallerIdCustomizedNumbersBody() # OutboundCallerIdCustomizedNumbersBody |  (optional)

try:
    # Add phone numbers for an account's customized outbound caller ID
    api_response = api_instance.add_outbound_caller_numbers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->add_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OutboundCallerIdCustomizedNumbersBody**](OutboundCallerIdCustomizedNumbersBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_caller_numbers**
> object delete_outbound_caller_numbers(customize_ids=customize_ids)

Delete phone numbers for an account's customized outbound caller ID

Deletes the `account-level` customized outbound caller ID phone numbers. Note that when multiple sites policy is enabled, users cannot manage the `account-level` configuration. The system will throw an exception.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:write:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
customize_ids = ['customize_ids_example'] # list[str] | The customization IDs. (optional)

try:
    # Delete phone numbers for an account's customized outbound caller ID
    api_response = api_instance.delete_outbound_caller_numbers(customize_ids=customize_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customize_ids** | [**list[str]**](str.md)| The customization IDs. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customize_outbound_caller_numbers**
> InlineResponse20043 list_customize_outbound_caller_numbers(selected=selected, site_id=site_id, extension_type=extension_type, keyword=keyword, page_size=page_size, next_page_token=next_page_token)

List an account's customized outbound caller ID phone numbers

Retrieves phone numbers that can be used as the `account-level` customized outbound caller ID. Note that when multiple sites policy is enabled, users cannot manage the `account-level` configuration. The system will throw an exception.   **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license.  **Scope:** `phone:read:admin`    **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
selected = true # bool | The status of the phone numbers.<br> `true`- Numbers already added to the custom list. <br> `false`- Numbers not yet added to the custom list (optional)
site_id = 'site_id_example' # str | This field filters phone numbers that belong to the site. (optional)
extension_type = 'extension_type_example' # str | The type of extension to which the phone number belongs. (optional)
keyword = 'keyword_example' # str | A search keyword for phone or extension numbers. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List an account's customized outbound caller ID phone numbers
    api_response = api_instance.list_customize_outbound_caller_numbers(selected=selected, site_id=site_id, extension_type=extension_type, keyword=keyword, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_customize_outbound_caller_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected** | **bool**| The status of the phone numbers.&lt;br&gt; &#x60;true&#x60;- Numbers already added to the custom list. &lt;br&gt; &#x60;false&#x60;- Numbers not yet added to the custom list | [optional] 
 **site_id** | **str**| This field filters phone numbers that belong to the site. | [optional] 
 **extension_type** | **str**| The type of extension to which the phone number belongs. | [optional] 
 **keyword** | **str**| A search keyword for phone or extension numbers. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zoom_phone_account_settings**
> InlineResponse20044 list_zoom_phone_account_settings(setting_types=setting_types)

List an account's zoom phone settings

Returns an account's Zoom phone settings.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:** * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
setting_types = 'setting_types_example' # str | Comma separated list of the setting items you want to fetch. Allowed values: `call_live_transcription`,`local_survivability_mode`,`external_calling_on_zoom_room_common_area`, `select_outbound_caller_id`, `personal_audio_library`, `voicemail`, `voicemail_transcription`, `voicemail_notification_by_email`, `shared_voicemail_notification_by_email`, `restricted_call_hours`, `allowed_call_locations`, `check_voicemails_over_phone`, `auto_call_recording`, `ad_hoc_call_recording`, `international_calling`, `outbound_calling`, `outbound_sms`, `sms`, `sms_etiquette_tool`, `zoom_phone_on_mobile`, `zoom_phone_on_pwa`, `e2e_encryption`, `call_handling_forwarding_to_other_users`, `call_overflow`, `call_transferring`, `elevate_to_meeting`, `call_park`, `hand_off_to_room`, `mobile_switch_to_carrier`, `delegation`, `audio_intercom`, `block_calls_without_caller_id`, `block_external_calls`,`call_queue_opt_out_reason`,`auto_delete_data_after_retention_duration`,`auto_call_from_third_party_apps`, `override_default_port`,`peer_to_peer_media`,`advanced_encryption`,`display_call_feedback_survey`. (optional)

try:
    # List an account's zoom phone settings
    api_response = api_instance.list_zoom_phone_account_settings(setting_types=setting_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_zoom_phone_account_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_types** | **str**| Comma separated list of the setting items you want to fetch. Allowed values: &#x60;call_live_transcription&#x60;,&#x60;local_survivability_mode&#x60;,&#x60;external_calling_on_zoom_room_common_area&#x60;, &#x60;select_outbound_caller_id&#x60;, &#x60;personal_audio_library&#x60;, &#x60;voicemail&#x60;, &#x60;voicemail_transcription&#x60;, &#x60;voicemail_notification_by_email&#x60;, &#x60;shared_voicemail_notification_by_email&#x60;, &#x60;restricted_call_hours&#x60;, &#x60;allowed_call_locations&#x60;, &#x60;check_voicemails_over_phone&#x60;, &#x60;auto_call_recording&#x60;, &#x60;ad_hoc_call_recording&#x60;, &#x60;international_calling&#x60;, &#x60;outbound_calling&#x60;, &#x60;outbound_sms&#x60;, &#x60;sms&#x60;, &#x60;sms_etiquette_tool&#x60;, &#x60;zoom_phone_on_mobile&#x60;, &#x60;zoom_phone_on_pwa&#x60;, &#x60;e2e_encryption&#x60;, &#x60;call_handling_forwarding_to_other_users&#x60;, &#x60;call_overflow&#x60;, &#x60;call_transferring&#x60;, &#x60;elevate_to_meeting&#x60;, &#x60;call_park&#x60;, &#x60;hand_off_to_room&#x60;, &#x60;mobile_switch_to_carrier&#x60;, &#x60;delegation&#x60;, &#x60;audio_intercom&#x60;, &#x60;block_calls_without_caller_id&#x60;, &#x60;block_external_calls&#x60;,&#x60;call_queue_opt_out_reason&#x60;,&#x60;auto_delete_data_after_retention_duration&#x60;,&#x60;auto_call_from_third_party_apps&#x60;, &#x60;override_default_port&#x60;,&#x60;peer_to_peer_media&#x60;,&#x60;advanced_encryption&#x60;,&#x60;display_call_feedback_survey&#x60;. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

