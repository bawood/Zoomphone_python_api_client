# swagger_client.VoicemailsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_voice_mails**](VoicemailsApi.md#account_voice_mails) | **GET** /phone/voice_mails | Get account voicemails
[**delete_voicemail**](VoicemailsApi.md#delete_voicemail) | **DELETE** /phone/voice_mails/{voicemailId} | Delete a voicemail
[**get_phone_user_voice_mails**](VoicemailsApi.md#get_phone_user_voice_mails) | **GET** /phone/users/{userId}/voice_mails/sync | List user&#x27;s voicemails in descending order
[**get_voicemail_details**](VoicemailsApi.md#get_voicemail_details) | **GET** /phone/voice_mails/{voicemailId} | Get voicemail details
[**get_voicemail_details_by_call_id_or_call_log_id**](VoicemailsApi.md#get_voicemail_details_by_call_id_or_call_log_id) | **GET** /phone/users/{userId}/call_logs/{id}/voice_mail | Get user voicemail details from a call log
[**phone_user_voice_mails**](VoicemailsApi.md#phone_user_voice_mails) | **GET** /phone/users/{userId}/voice_mails | Get user&#x27;s voicemails

# **account_voice_mails**
> InlineResponse20092 account_voice_mails(page_size=page_size, status=status, site_id=site_id, owner_type=owner_type, voicemail_type=voicemail_type, next_page_token=next_page_token, _from=_from, to=to)

Get account voicemails

Use this API to get a user's Zoom Phone voicemails.   **Scopes:** `phone_voicemail:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.VoicemailsApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
status = 'all' # str | Status of the voice mail (optional) (default to all)
site_id = 'site_id_example' # str | The site ID. (optional)
owner_type = 'owner_type_example' # str | The owner type. (optional)
voicemail_type = 'voicemail_type_example' # str | The voicemail type. (optional)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. The month defined should fall within the last six months. If unspecified, returns data from the past 30 days. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)

try:
    # Get account voicemails
    api_response = api_instance.account_voice_mails(page_size=page_size, status=status, site_id=site_id, owner_type=owner_type, voicemail_type=voicemail_type, next_page_token=next_page_token, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailsApi->account_voice_mails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **status** | **str**| Status of the voice mail | [optional] [default to all]
 **site_id** | **str**| The site ID. | [optional] 
 **owner_type** | **str**| The owner type. | [optional] 
 **voicemail_type** | **str**| The voicemail type. | [optional] 
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. The month defined should fall within the last six months. If unspecified, returns data from the past 30 days. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voicemail**
> object delete_voicemail(voicemail_id)

Delete a voicemail

Use this API to delete an account's [voicemail message](https://support.zoom.us/hc/en-us/articles/360021400211-Managing-voicemail-messages).  **Scopes:** `phone:write:admin`, `phone:write`, `phone_voicemail:write`, `phone_voicemail:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Zoom Phone license

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
api_instance = swagger_client.VoicemailsApi(swagger_client.ApiClient(configuration))
voicemail_id = 'voicemail_id_example' # str | Unique identifier of the voicemail. Retrieve the value for this field by calling the [Get voicemails](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserVoiceMails) API.

try:
    # Delete a voicemail
    api_response = api_instance.delete_voicemail(voicemail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailsApi->delete_voicemail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voicemail_id** | **str**| Unique identifier of the voicemail. Retrieve the value for this field by calling the [Get voicemails](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserVoiceMails) API. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_user_voice_mails**
> InlineResponse20091 get_phone_user_voice_mails(user_id, sync_type, sync_token=sync_token, count=count)

List user's voicemails in descending order

Use this API to retrieve a user's Zoom Phone voicemails in descending order. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:read`, `phone:read:admin`, `phone_voicemail:read`, `phone_voicemail:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.VoicemailsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
sync_type = 'FSync' # str | FSync: Full sync  BSync: Backward sync  ISync: Forward sync (default to FSync)
sync_token = 'sync_token_example' # str | Sync token. Use if requesting a backward (`BSync`) or forward (`ISync`) sync. (optional)
count = 56 # int | Record count of each query. (optional)

try:
    # List user's voicemails in descending order
    api_response = api_instance.get_phone_user_voice_mails(user_id, sync_type, sync_token=sync_token, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailsApi->get_phone_user_voice_mails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **sync_type** | **str**| FSync: Full sync  BSync: Backward sync  ISync: Forward sync | [default to FSync]
 **sync_token** | **str**| Sync token. Use if requesting a backward (&#x60;BSync&#x60;) or forward (&#x60;ISync&#x60;) sync. | [optional] 
 **count** | **int**| Record count of each query. | [optional] 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voicemail_details**
> InlineResponse20093 get_voicemail_details(voicemail_id)

Get voicemail details

Use this API to return information about a [voicemail message](https://support.zoom.us/hc/en-us/articles/360021400211-Managing-voicemail-messages).  **Scopes:** `phone:read:admin`, `phone:read`, `phone_voicemail:read`, `phone_voicemail:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Zoom Phone license

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
api_instance = swagger_client.VoicemailsApi(swagger_client.ApiClient(configuration))
voicemail_id = 'voicemail_id_example' # str | The unique identifier of the voicemail. It retrieves the value for this field by calling the [Get voicemails](https://marketplace.zoom.us/docs/api-reference/phone/methods/#operation/phoneUserVoiceMails) API.

try:
    # Get voicemail details
    api_response = api_instance.get_voicemail_details(voicemail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailsApi->get_voicemail_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voicemail_id** | **str**| The unique identifier of the voicemail. It retrieves the value for this field by calling the [Get voicemails](https://marketplace.zoom.us/docs/api-reference/phone/methods/#operation/phoneUserVoiceMails) API. | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voicemail_details_by_call_id_or_call_log_id**
> InlineResponse20083 get_voicemail_details_by_call_id_or_call_log_id(user_id, id)

Get user voicemail details from a call log

Use this API to return detailed information on a voicemail associated with a call log ID. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:read`, `phone:read:admin`, `phone_voicemail:read`, `phone_voicemail:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * User must belong to a Business or Enterprise account  * User must have a Zoom Phone license

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
api_instance = swagger_client.VoicemailsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user.
id = 'id_example' # str | Gets the unique ID of the call log. You can use `callLogId` or `callId` as path parameters.  You can find the value for this field with in **[Get account's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs)** API or **[Get user's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs)** API.

try:
    # Get user voicemail details from a call log
    api_response = api_instance.get_voicemail_details_by_call_id_or_call_log_id(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailsApi->get_voicemail_details_by_call_id_or_call_log_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. | 
 **id** | **str**| Gets the unique ID of the call log. You can use &#x60;callLogId&#x60; or &#x60;callId&#x60; as path parameters.  You can find the value for this field with in **[Get account&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs)** API or **[Get user&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs)** API. | 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_user_voice_mails**
> InlineResponse20090 phone_user_voice_mails(user_id, page_size=page_size, status=status, next_page_token=next_page_token, _from=_from, to=to)

Get user's voicemails

Use this API to get a user's Zoom Phone voicemails. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:read`, `phone:read:admin`, `phone_voicemail:read`, `phone_voicemail:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.VoicemailsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
status = 'all' # str | Status of the voice mail (optional) (default to all)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. The month defined should fall within the last six months. If unspecified, returns data from the past 30 days. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)

try:
    # Get user's voicemails
    api_response = api_instance.phone_user_voice_mails(user_id, page_size=page_size, status=status, next_page_token=next_page_token, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailsApi->phone_user_voice_mails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **status** | **str**| Status of the voice mail | [optional] [default to all]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. The month defined should fall within the last six months. If unspecified, returns data from the past 30 days. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

