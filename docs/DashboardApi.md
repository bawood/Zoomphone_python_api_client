# swagger_client.DashboardApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_call_log_metrics_details**](DashboardApi.md#get_call_log_metrics_details) | **GET** /phone/metrics/call_logs/{call_id} | Get call details from call log
[**get_call_qo_s**](DashboardApi.md#get_call_qo_s) | **GET** /phone/metrics/call_logs/{callId}/qos | Get call QoS
[**list_call_logs_metrics**](DashboardApi.md#list_call_logs_metrics) | **GET** /phone/metrics/call_logs | List call logs
[**list_tracked_locations**](DashboardApi.md#list_tracked_locations) | **GET** /phone/metrics/location_tracking | List tracked locations

# **get_call_log_metrics_details**
> InlineResponse20038 get_call_log_metrics_details(call_id)

Get call details from call log

Lists call log details of a specific call. The call logs provide a record of all incoming and outgoing calls over Zoom Phone in an account.   **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light

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
api_instance = swagger_client.DashboardApi(swagger_client.ApiClient(configuration))
call_id = 'call_id_example' # str | The unique identifier of the phone call. The value of this field can be retrieved from [List Call Logs]() API.

try:
    # Get call details from call log
    api_response = api_instance.get_call_log_metrics_details(call_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_call_log_metrics_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**| The unique identifier of the phone call. The value of this field can be retrieved from [List Call Logs]() API. | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_qo_s**
> InlineResponse20037 get_call_qo_s(call_id)

Get call QoS

Gets the call quality of service (QoS) data for a call made or received by a Zoom phone user in the account.   **Prerequisites:** * Business, or Education account * Zoom Phone license <br><br> **Scopes:** `phone:read:admin`<br> **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.DashboardApi(swagger_client.ApiClient(configuration))
call_id = 'call_id_example' # str | The unique identifier of the call.

try:
    # Get call QoS
    api_response = api_instance.get_call_qo_s(call_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_call_qo_s: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**| The unique identifier of the call. | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_logs_metrics**
> InlineResponse20036 list_call_logs_metrics(_from=_from, to=to, site_id=site_id, quality_type=quality_type, page_size=page_size, next_page_token=next_page_token)

List call logs

 Lists the monthly call logs metrics. You can use query parameters to filter the response by date, site and MOS(Mean Opinion Score) of the call.The call logs that provide a record of all incoming and outgoing calls over Zoom Phone in an account.   **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`

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
api_instance = swagger_client.DashboardApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | The start date in **yyyy-mm-dd** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. If unspecified, returns data from the past 1 day. (optional)
to = '2013-10-20' # date | This setting is **required** only when the `from` parameter is specified. The end date is in **yyyy-mm-dd** format, which is the same format as the `from` parameter. (optional)
site_id = 'site_id_example' # str | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Use this query parameter if you have enabled multiple sites and would like to filter the response of this API call by call logs of a specific phone site. (optional)
quality_type = 'quality_type_example' # str | This setting filters call logs by voice quality. Zoom uses MOS of 3.5 as a general baseline to categorize calls by call quality. A MOS greater than or equal to 3.5 means good quality, while below 3.5 means poor quality. <br><br>The value of this field can be one of the following:<br> * `good`: Retrieve call logs of the call(s) with good quality of voice.<br> * `bad`: Retrieve call logs of the call(s) with good quality of voice.<br> * `all`: Retrieve all call logs without filtering by voice quality.      (optional)
page_size = 30 # int | The number of records returned within a single call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List call logs
    api_response = api_instance.list_call_logs_metrics(_from=_from, to=to, site_id=site_id, quality_type=quality_type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->list_call_logs_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The start date in **yyyy-mm-dd** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. If unspecified, returns data from the past 1 day. | [optional] 
 **to** | **date**| This setting is **required** only when the &#x60;from&#x60; parameter is specified. The end date is in **yyyy-mm-dd** format, which is the same format as the &#x60;from&#x60; parameter. | [optional] 
 **site_id** | **str**| The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). Use this query parameter if you have enabled multiple sites and would like to filter the response of this API call by call logs of a specific phone site. | [optional] 
 **quality_type** | **str**| This setting filters call logs by voice quality. Zoom uses MOS of 3.5 as a general baseline to categorize calls by call quality. A MOS greater than or equal to 3.5 means good quality, while below 3.5 means poor quality. &lt;br&gt;&lt;br&gt;The value of this field can be one of the following:&lt;br&gt; * &#x60;good&#x60;: Retrieve call logs of the call(s) with good quality of voice.&lt;br&gt; * &#x60;bad&#x60;: Retrieve call logs of the call(s) with good quality of voice.&lt;br&gt; * &#x60;all&#x60;: Retrieve all call logs without filtering by voice quality.      | [optional] 
 **page_size** | **int**| The number of records returned within a single call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tracked_locations**
> InlineResponse20039 list_tracked_locations(type=type, site_id=site_id, location_type=location_type, keyword=keyword)

List tracked locations

Lists the tracked locations.   **Prerequisites:** * Pro or higher account plan with Zoom phone license * Account owner or admin permissions  **Scope:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.DashboardApi(swagger_client.ApiClient(configuration))
type = 56 # int | The type of response data. Supports  only six responses at this time. `1`: Nomadic Emergency Services. `2`: Users Permission for Location Sharing. `3`: Default Emergency Address. `4`: Detectable Personal Location. `5`: Real-time Location for Users. `6`: Real-time Location for IP Phones. (optional)
site_id = 'site_id_example' # str | The site's ID. (optional)
location_type = 'location_type_example' # str | The location's type. 'Company' is the default value. (optional)
keyword = 'keyword_example' # str | The device name or device MAC address. (optional)

try:
    # List tracked locations
    api_response = api_instance.list_tracked_locations(type=type, site_id=site_id, location_type=location_type, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->list_tracked_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| The type of response data. Supports  only six responses at this time. &#x60;1&#x60;: Nomadic Emergency Services. &#x60;2&#x60;: Users Permission for Location Sharing. &#x60;3&#x60;: Default Emergency Address. &#x60;4&#x60;: Detectable Personal Location. &#x60;5&#x60;: Real-time Location for Users. &#x60;6&#x60;: Real-time Location for IP Phones. | [optional] 
 **site_id** | **str**| The site&#x27;s ID. | [optional] 
 **location_type** | **str**| The location&#x27;s type. &#x27;Company&#x27; is the default value. | [optional] 
 **keyword** | **str**| The device name or device MAC address. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

