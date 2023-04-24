# swagger_client.RecordingsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_call_recording**](RecordingsApi.md#delete_call_recording) | **DELETE** /phone/recordings/{recordingId} | Delete a call recording
[**get_phone_recordings**](RecordingsApi.md#get_phone_recordings) | **GET** /phone/recordings | Get call recordings
[**get_phone_recordings_by_call_id_or_call_log_id**](RecordingsApi.md#get_phone_recordings_by_call_id_or_call_log_id) | **GET** /phone/call_logs/{id}/recordings | Get recording by call ID
[**phone_download_recording_transcript**](RecordingsApi.md#phone_download_recording_transcript) | **GET** /phone/recording_transcript/download/{recordingId} | Download a phone recording transcript
[**phone_user_recordings**](RecordingsApi.md#phone_user_recordings) | **GET** /phone/users/{userId}/recordings | Get user&#x27;s recordings

# **delete_call_recording**
> object delete_call_recording(recording_id)

Delete a call recording

Deletes a call recording.  **Scopes:** `phone:write`, `phone:write:admin`, `phone_recording:write`, `phone_recording:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * User must belong to a Business or Enterprise account  * User must have a Zoom Phone license

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
api_instance = swagger_client.RecordingsApi(swagger_client.ApiClient(configuration))
recording_id = 'recording_id_example' # str | The unique identifier of the recording.

try:
    # Delete a call recording
    api_response = api_instance.delete_call_recording(recording_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingsApi->delete_call_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| The unique identifier of the recording. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_recordings**
> InlineResponse20053 get_phone_recordings(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, owner_type=owner_type, recording_type=recording_type, site_id=site_id, query_date_type=query_date_type)

Get call recordings

Lists an account's [call recordings](https://support.zoom.us/hc/en-us/articles/360038521091-Accessing-and-sharing-call-recordings).  **Prerequisites:** * A Pro or higher account plan  * A Zoom Phone license  * Account owner or admin privileges**Scopes:** `phone:read:admin`, `phone_recording:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium` 

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
api_instance = swagger_client.RecordingsApi(swagger_client.ApiClient(configuration))
page_size = 56 # int | The number of records returned within a single API call. The default is **30**, and the maximum is **300**. (optional)
next_page_token = 'next_page_token_example' # str | The current page number of returned records. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. If unspecified, returns data from the past 30 days. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)
owner_type = 'all' # str | The owner type. The allowed values are null, `user`, or `callQueue`. The default is null. If null, returns all owner types.  (optional) (default to all)
recording_type = 'recording_type_example' # str | The recording type. The allowed values are null, `OnDemand`, or `Automatic`. The default is null. If null, returns all recording types.  (optional)
site_id = 'All sites' # str | The site ID. The default is `All sites`. (optional) (default to All sites)
query_date_type = 'start_time' # str | The query date type, `start_time` or the `end_time`, default `start_time` (optional) (default to start_time)

try:
    # Get call recordings
    api_response = api_instance.get_phone_recordings(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, owner_type=owner_type, recording_type=recording_type, site_id=site_id, query_date_type=query_date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingsApi->get_phone_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. The default is **30**, and the maximum is **300**. | [optional] 
 **next_page_token** | **str**| The current page number of returned records. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. If unspecified, returns data from the past 30 days. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 
 **owner_type** | **str**| The owner type. The allowed values are null, &#x60;user&#x60;, or &#x60;callQueue&#x60;. The default is null. If null, returns all owner types.  | [optional] [default to all]
 **recording_type** | **str**| The recording type. The allowed values are null, &#x60;OnDemand&#x60;, or &#x60;Automatic&#x60;. The default is null. If null, returns all recording types.  | [optional] 
 **site_id** | **str**| The site ID. The default is &#x60;All sites&#x60;. | [optional] [default to All sites]
 **query_date_type** | **str**| The query date type, &#x60;start_time&#x60; or the &#x60;end_time&#x60;, default &#x60;start_time&#x60; | [optional] [default to start_time]

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_recordings_by_call_id_or_call_log_id**
> InlineResponse2009 get_phone_recordings_by_call_id_or_call_log_id(id)

Get recording by call ID

Gets an account's call recording(https://support.zoom.us/hc/en-us/articles/360038521091-Accessing-and-sharing-call-recordings) by the recording's `callId` or `callLogId` ID.  **Prerequisites:**  * A Pro or higher account with Zoom Phone license.  * Account owner or admin privileges  **Scopes:** `phone:read:admin`<br> **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.RecordingsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique ID of the call log. You can use `callLogId` and `callId` as path parameters.  You can find the value for this field with the **[Get account's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs)** API or the **[Get user's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs)** API.

try:
    # Get recording by call ID
    api_response = api_instance.get_phone_recordings_by_call_id_or_call_log_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingsApi->get_phone_recordings_by_call_id_or_call_log_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the call log. You can use &#x60;callLogId&#x60; and &#x60;callId&#x60; as path parameters.  You can find the value for this field with the **[Get account&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs)** API or the **[Get user&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs)** API. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_download_recording_transcript**
> phone_download_recording_transcript(recording_id)

Download a phone recording transcript

Downloads the phone recording transcript.   **Prerequisites:**  * A Business or Enterprise account * A Zoom Phone license  **Scopes:** `phone:read`, `phone:read:admin`, `phone_recording:read`, `phone_recording:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`    

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
api_instance = swagger_client.RecordingsApi(swagger_client.ApiClient(configuration))
recording_id = 'recording_id_example' # str | The phone recording ID.

try:
    # Download a phone recording transcript
    api_instance.phone_download_recording_transcript(recording_id)
except ApiException as e:
    print("Exception when calling RecordingsApi->phone_download_recording_transcript: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| The phone recording ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_user_recordings**
> InlineResponse20085 phone_user_recordings(user_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)

Get user's recordings

Gets a user's [Zoom Phone recordings](https://support.zoom.us/hc/en-us/articles/360021336671-Viewing-Call-History-and-Recordings). For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Scopes:** `phone:read`, `phone:read:admin`, `phone_recording:read`, `phone_recording:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.RecordingsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. The month defined should fall within the last six months. If unspecified, returns data from the past 30 days. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)

try:
    # Get user's recordings
    api_response = api_instance.phone_user_recordings(user_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingsApi->phone_user_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. The month defined should fall within the last six months. If unspecified, returns data from the past 30 days. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

