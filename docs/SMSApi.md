# swagger_client.SMSApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_sms_session**](SMSApi.md#account_sms_session) | **GET** /phone/sms/sessions | Get account&#x27;s SMS sessions
[**get_sms_sessions**](SMSApi.md#get_sms_sessions) | **GET** /phone/users/{userId}/sms/sessions/sync | List user&#x27;s SMS sessions in descending order
[**sms_by_message_id**](SMSApi.md#sms_by_message_id) | **GET** /phone/sms/sessions/{sessionId}/messages/{messageId} | Get SMS by message ID
[**sms_session_details**](SMSApi.md#sms_session_details) | **GET** /phone/sms/sessions/{sessionId} | Get SMS session details
[**sms_session_sync**](SMSApi.md#sms_session_sync) | **GET** /phone/sms/sessions/{sessionId}/sync | Sync SMS by session ID
[**user_sms_session**](SMSApi.md#user_sms_session) | **GET** /phone/users/{userId}/sms/sessions | Get user&#x27;s SMS sessions

# **account_sms_session**
> InlineResponse20073 account_sms_session(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, phone_number=phone_number)

Get account's SMS sessions

Get details about SMS sessions for an account.  **Scopes:** `phone_sms:read:admin`, `phone_sms:master`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites** * Paid account * User-enabled Zoom phone  

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
api_instance = swagger_client.SMSApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The current page number of returned records. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. If unspecified, returns data from the past 30 days. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)
phone_number = 'phone_number_example' # str | Either the sender's or receiver's phone number, to limit the list of SMS sessions. (optional)

try:
    # Get account's SMS sessions
    api_response = api_instance.account_sms_session(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, phone_number=phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->account_sms_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The current page number of returned records. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. If unspecified, returns data from the past 30 days. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 
 **phone_number** | **str**| Either the sender&#x27;s or receiver&#x27;s phone number, to limit the list of SMS sessions. | [optional] 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sms_sessions**
> InlineResponse20089 get_sms_sessions(user_id, sync_type, sync_token=sync_token, count=count)

List user's SMS sessions in descending order

Use this API to retrieve user's SMS sessions in descending order. Mirrors the ZP client behavior with the most recent on top.  **Prerequisites:** * Paid account  * User-enabled Zoom phone   **Scopes:** `phone_sms:read`, `phone_sms:read:admin`, `phone_sms:master`  **Rate Limit Label:** `Medium`

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
api_instance = swagger_client.SMSApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User ID, user email, or “me” if using OAuth token.
sync_type = 'FSync' # str | FSync: Full sync BSync: Backward sync ISync: Forward sync (default to FSync)
sync_token = 'sync_token_example' # str | Sync token. Use if requesting a backward (`BSync`) or forward (`ISync`) sync. (optional)
count = 56 # int | Record count of each query (optional)

try:
    # List user's SMS sessions in descending order
    api_response = api_instance.get_sms_sessions(user_id, sync_type, sync_token=sync_token, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->get_sms_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID, user email, or “me” if using OAuth token. | 
 **sync_type** | **str**| FSync: Full sync BSync: Backward sync ISync: Forward sync | [default to FSync]
 **sync_token** | **str**| Sync token. Use if requesting a backward (&#x60;BSync&#x60;) or forward (&#x60;ISync&#x60;) sync. | [optional] 
 **count** | **int**| Record count of each query | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_by_message_id**
> InlineResponse20076 sms_by_message_id(session_id, message_id)

Get SMS by message ID

Get details about a specific message in an SMS session.  **Scopes:** `phone_sms:read`, `phone_sms:read:admin`, `phone_sms:master`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`  **Prerequisites** * Paid account * User-enabled Zoom phone  

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
api_instance = swagger_client.SMSApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | The SMS session ID.
message_id = 'message_id_example' # str | The SMS message ID.

try:
    # Get SMS by message ID
    api_response = api_instance.sms_by_message_id(session_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_by_message_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The SMS session ID. | 
 **message_id** | **str**| The SMS message ID. | 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_session_details**
> InlineResponse20074 sms_session_details(session_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, sort=sort)

Get SMS session details

Get details about an SMS session.  **Scopes:** `phone_sms:read`, `phone_sms:read:admin`, `phone_sms:master`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites** * Paid account * User-enabled Zoom phone  

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
api_instance = swagger_client.SMSApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | SMS session ID.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The current page number of returned records. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. If unspecified, returns data from the past 30 days. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)
sort = 56 # int | Order of SMS to return based on creation time. `1`: ascending `2`: descending (optional)

try:
    # Get SMS session details
    api_response = api_instance.sms_session_details(session_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_session_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| SMS session ID. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The current page number of returned records. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. If unspecified, returns data from the past 30 days. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 
 **sort** | **int**| Order of SMS to return based on creation time. &#x60;1&#x60;: ascending &#x60;2&#x60;: descending | [optional] 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_session_sync**
> InlineResponse20075 sms_session_sync(session_id, sync_type=sync_type, count=count, sync_token=sync_token)

Sync SMS by session ID

Use this API to sync SMS messages in a session.   **Scopes:** `phone_sms:read`, `phone_sms:read:admin`, `phone_sms:master`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites** * Paid account * User-enabled Zoom phone  

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
api_instance = swagger_client.SMSApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | SMS session ID.
sync_type = 'sync_type_example' # str | Options for synchronizing sms message:<br> FSync - Full sync<br> ISync - Increase sync<br> BSync - Backward sync (optional)
count = 56 # int | The number of records returned within a single API call. (optional)
sync_token = 'sync_token_example' # str | The time range for returned records. Used for locating where the next retrieval will begin. (optional)

try:
    # Sync SMS by session ID
    api_response = api_instance.sms_session_sync(session_id, sync_type=sync_type, count=count, sync_token=sync_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_session_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| SMS session ID. | 
 **sync_type** | **str**| Options for synchronizing sms message:&lt;br&gt; FSync - Full sync&lt;br&gt; ISync - Increase sync&lt;br&gt; BSync - Backward sync | [optional] 
 **count** | **int**| The number of records returned within a single API call. | [optional] 
 **sync_token** | **str**| The time range for returned records. Used for locating where the next retrieval will begin. | [optional] 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_sms_session**
> InlineResponse20088 user_sms_session(user_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, phone_number=phone_number)

Get user's SMS sessions

Get details about SMS sessions for a user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone_sms:read`, `phone_sms:read:admin`, `phone_sms:master`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`  **Prerequisites:**  * Paid account  * User-enabled Zoom phone

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
api_instance = swagger_client.SMSApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User ID, user email, or “me” if using OAuth token.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The current page number of returned records. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. If unspecified, returns data from the past 30 days. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)
phone_number = 'phone_number_example' # str | Either the sender's or receiver's phone number, to limit the list of SMS sessions. (optional)

try:
    # Get user's SMS sessions
    api_response = api_instance.user_sms_session(user_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, phone_number=phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->user_sms_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID, user email, or “me” if using OAuth token. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The current page number of returned records. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. If unspecified, returns data from the past 30 days. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 
 **phone_number** | **str**| Either the sender&#x27;s or receiver&#x27;s phone number, to limit the list of SMS sessions. | [optional] 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

