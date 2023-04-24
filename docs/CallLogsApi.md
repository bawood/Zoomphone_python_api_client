# swagger_client.CallLogsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_call_logs**](CallLogsApi.md#account_call_logs) | **GET** /phone/call_logs | Get account&#x27;s call logs
[**add_client_code_to_call_log**](CallLogsApi.md#add_client_code_to_call_log) | **PUT** /phone/call_logs/{callLogId}/client_code | Add a client code to a call log
[**delete_call_log**](CallLogsApi.md#delete_call_log) | **DELETE** /phone/users/{userId}/call_logs/{callLogId} | Delete a user&#x27;s call log
[**get_call_log_details**](CallLogsApi.md#get_call_log_details) | **GET** /phone/call_logs/{callLogId} | Get call log details
[**phone_user_call_logs**](CallLogsApi.md#phone_user_call_logs) | **GET** /phone/users/{userId}/call_logs | Get user&#x27;s call logs
[**sync_user_call_logs**](CallLogsApi.md#sync_user_call_logs) | **GET** /phone/users/{userId}/call_logs/sync | Sync user&#x27;s call logs

# **account_call_logs**
> InlineResponse2007 account_call_logs(page_size=page_size, _from=_from, to=to, type=type, next_page_token=next_page_token, path=path, time_type=time_type, site_id=site_id, charged_call_logs=charged_call_logs)

Get account's call logs

Returns an account's [call logs](https://support.zoom.us/hc/en-us/articles/360021114452-Viewing-Call-Logs).  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  * Account owner or a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) with Zoom Phone management  **Scopes:** `phone:read:admin`, `phone_call_log:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits/#zoom-phone-apis):** `Heavy`

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
api_instance = swagger_client.CallLogsApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data. The month defined should fall within the last six months. If unspecified, returns data within the 24 hours. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)
type = 'type_example' # str | The type of the call logs. The value can be either \"all\" or \"missed\". (optional)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
path = 'path_example' # str | Filter the API response by [path](https://support.zoom.us/hc/en-us/articles/360021114452-Viewing-and-identifying-logs#h_646b46c6-0623-4ab1-8b8b-ea5b8bcef679) of the call. The value of this field can be one of the following: `voiceMail`, `message`, `forward`, `extension`, `callQueue`, `ivrMenu`, `companyDirectory`, `autoReceptionist`, `contactCenter`, `disconnected`, `commonAreaPhone`, `pstn`, `transfer`, `sharedLines`, `sharedLineGroup`, `tollFreeBilling`, `meetingService`, `parkPickup`, `parkTimeout`, `monitor`, `takeover`, `sipGroup` (optional)
time_type = 'startTime' # str | Enables you to search call logs by start or end time. Choose `startTime` or `endTime`. (optional) (default to startTime)
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Use this query parameter if you have enabled multiple sites and would like to filter the response of this API call by call logs of a specific phone site. (optional)
charged_call_logs = true # bool | Whether to filter API responses to include call logs that only have a non-zero charge. (optional)

try:
    # Get account's call logs
    api_response = api_instance.account_call_logs(page_size=page_size, _from=_from, to=to, type=type, next_page_token=next_page_token, path=path, time_type=time_type, site_id=site_id, charged_call_logs=charged_call_logs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallLogsApi->account_call_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data. The month defined should fall within the last six months. If unspecified, returns data within the 24 hours. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 
 **type** | **str**| The type of the call logs. The value can be either \&quot;all\&quot; or \&quot;missed\&quot;. | [optional] 
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **path** | **str**| Filter the API response by [path](https://support.zoom.us/hc/en-us/articles/360021114452-Viewing-and-identifying-logs#h_646b46c6-0623-4ab1-8b8b-ea5b8bcef679) of the call. The value of this field can be one of the following: &#x60;voiceMail&#x60;, &#x60;message&#x60;, &#x60;forward&#x60;, &#x60;extension&#x60;, &#x60;callQueue&#x60;, &#x60;ivrMenu&#x60;, &#x60;companyDirectory&#x60;, &#x60;autoReceptionist&#x60;, &#x60;contactCenter&#x60;, &#x60;disconnected&#x60;, &#x60;commonAreaPhone&#x60;, &#x60;pstn&#x60;, &#x60;transfer&#x60;, &#x60;sharedLines&#x60;, &#x60;sharedLineGroup&#x60;, &#x60;tollFreeBilling&#x60;, &#x60;meetingService&#x60;, &#x60;parkPickup&#x60;, &#x60;parkTimeout&#x60;, &#x60;monitor&#x60;, &#x60;takeover&#x60;, &#x60;sipGroup&#x60; | [optional] 
 **time_type** | **str**| Enables you to search call logs by start or end time. Choose &#x60;startTime&#x60; or &#x60;endTime&#x60;. | [optional] [default to startTime]
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Use this query parameter if you have enabled multiple sites and would like to filter the response of this API call by call logs of a specific phone site. | [optional] 
 **charged_call_logs** | **bool**| Whether to filter API responses to include call logs that only have a non-zero charge. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_client_code_to_call_log**
> object add_client_code_to_call_log(call_log_id, body=body)

Add a client code to a call log

Adds a client code to a [call log](https://support.zoom.us/hc/en-us/articles/360040999352-Assigning-client-codes-to-phone-calls). You can track call logs with a client code.   **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits/#zoom-phone-apis):** `Light`

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
api_instance = swagger_client.CallLogsApi(swagger_client.ApiClient(configuration))
call_log_id = 'call_log_id_example' # str | Unique identifier of the call log.
body = swagger_client.CallLogIdClientCodeBody() # CallLogIdClientCodeBody |  (optional)

try:
    # Add a client code to a call log
    api_response = api_instance.add_client_code_to_call_log(call_log_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallLogsApi->add_client_code_to_call_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_log_id** | **str**| Unique identifier of the call log. | 
 **body** | [**CallLogIdClientCodeBody**](CallLogIdClientCodeBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_call_log**
> object delete_call_log(user_id, call_log_id)

Delete a user's call log

Deletes a user's [call log](https://support.zoom.us/hc/en-us/articles/360021114452-Viewing-and-identifying-logs). For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Prerequisites:**  * User must belong to a Business or Enterprise account  * User must have a Zoom Phone license  **Scopes:** `phone:write`, `phone:write:admin`, `phone_call_log:write`, `phone_call_log:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits/#zoom-phone-apis):** `Light`

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
api_instance = swagger_client.CallLogsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user.
call_log_id = 'call_log_id_example' # str | Unique identifier of the call log. The value for this field can be retrieved from [account's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs) or [user's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs).

try:
    # Delete a user's call log
    api_response = api_instance.delete_call_log(user_id, call_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallLogsApi->delete_call_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. | 
 **call_log_id** | **str**| Unique identifier of the call log. The value for this field can be retrieved from [account&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs) or [user&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs). | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_log_details**
> InlineResponse2008 get_call_log_details(call_log_id)

Get call log details

Returns information about a [call log](https://support.zoom.us/hc/en-us/articles/360021114452-Viewing-and-identifying-logs).  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:read:admin`, `phone_call_log:read`, `phone_call_log:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits/#zoom-phone-apis):** `Light`

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
api_instance = swagger_client.CallLogsApi(swagger_client.ApiClient(configuration))
call_log_id = 'call_log_id_example' # str | Unique identifier of the call log. Both `callLogId` and `callId` can be used as path parameters. The value for this field can be retrieved from [account's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs) or the [user's call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs).

try:
    # Get call log details
    api_response = api_instance.get_call_log_details(call_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallLogsApi->get_call_log_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_log_id** | **str**| Unique identifier of the call log. Both &#x60;callLogId&#x60; and &#x60;callId&#x60; can be used as path parameters. The value for this field can be retrieved from [account&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/accountCallLogs) or the [user&#x27;s call logs](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/phoneUserCallLogs). | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_user_call_logs**
> InlineResponse20081 phone_user_call_logs(user_id, page_size=page_size, _from=_from, to=to, type=type, next_page_token=next_page_token, phone_number=phone_number, time_type=time_type)

Get user's call logs

Gets a user's [Zoom phone](https://support.zoom.us/hc/en-us/articles/360001297663-Quickstart-Guide-for-Zoom-Phone-Administrators) call logs. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:read`, `phone:read:admin`, `phone_call_log:read`, `phone_call_log:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits/#zoom-phone-apis):** `Heavy`

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
api_instance = swagger_client.CallLogsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data. The month defined should fall within the last six months. If unspecified, returns data within the 24 hours. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)
type = 'type_example' # str |  (optional)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
phone_number = 'phone_number_example' # str | Filter API responses to include call logs of only the phone number defined in this field. (optional)
time_type = 'startTime' # str | Enables you to sort call logs by start or end time. Choose the sort time value. Values include `startTime` or `endTime`. (optional) (default to startTime)

try:
    # Get user's call logs
    api_response = api_instance.phone_user_call_logs(user_id, page_size=page_size, _from=_from, to=to, type=type, next_page_token=next_page_token, phone_number=phone_number, time_type=time_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallLogsApi->phone_user_call_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data. The month defined should fall within the last six months. If unspecified, returns data within the 24 hours. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 
 **type** | **str**|  | [optional] 
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **phone_number** | **str**| Filter API responses to include call logs of only the phone number defined in this field. | [optional] 
 **time_type** | **str**| Enables you to sort call logs by start or end time. Choose the sort time value. Values include &#x60;startTime&#x60; or &#x60;endTime&#x60;. | [optional] [default to startTime]

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_user_call_logs**
> InlineResponse20082 sync_user_call_logs(user_id, sync_type=sync_type, count=count, sync_token=sync_token)

Sync user's call logs

Syncs a user's [Zoom phone](https://support.zoom.us/hc/en-us/articles/360001297663-Quickstart-Guide-for-Zoom-Phone-Administrators) call logs. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:read`, `phone:read:admin`, `phone_call_log:read`, `phone_call_log:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits/#zoom-phone-apis):** `Medium`

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
api_instance = swagger_client.CallLogsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User ID.
sync_type = 'sync_type_example' # str | Options for synchronizing call log:<br> FSync - Full sync<br> ISync - Increase sync<br> BSync - Backward sync (optional)
count = 56 # int | The number of records returned within a single API call. (optional)
sync_token = 'sync_token_example' # str | The time range for returned records. Used for locating where the next retrieval will begin. (optional)

try:
    # Sync user's call logs
    api_response = api_instance.sync_user_call_logs(user_id, sync_type=sync_type, count=count, sync_token=sync_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallLogsApi->sync_user_call_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. | 
 **sync_type** | **str**| Options for synchronizing call log:&lt;br&gt; FSync - Full sync&lt;br&gt; ISync - Increase sync&lt;br&gt; BSync - Backward sync | [optional] 
 **count** | **int**| The number of records returned within a single API call. | [optional] 
 **sync_token** | **str**| The time range for returned records. Used for locating where the next retrieval will begin. | [optional] 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

