# swagger_client.ReportsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ps_operation_logs**](ReportsApi.md#get_ps_operation_logs) | **GET** /phone/reports/operationlogs | Get operation logs report

# **get_ps_operation_logs**
> InlineResponse20054 get_ps_operation_logs(_from=_from, to=to, category_type=category_type, page_size=page_size, next_page_token=next_page_token)

Get operation logs report

The **Phone System operation logs report** allows account owners and admins to view monthly Zoom phone related admin operation details.   Use this API to retrieve the **Phone System Operation Logs Report**. Account owners and admins can also access this information by logging into their Zoom accounts and navigating to [Phone System Operation Logs](https://zoom.us/pbx/page/report/operations#/report/operation-logs).<br><br> **Scopes:** `phone:read:admin`<br> **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`<br> <br> **Prerequisites:** <br> * Account must be enrollled in Pro or a higher plan * Account must be enrolled in a [Zoom Phone](https://zoom.us/pricing/zoom-phone) plan  

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format. The date range defined by the `from` and `to` parameters should be a month as the response only includes one month's worth of data at once. If unspecified, returns data within the 24 hours. (optional)
to = '2013-10-20' # date | **Required** only when the `from` parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd'T'HH:mm:ss'Z'** format, the same format as the `from` parameter. (optional)
category_type = 'all' # str | Filter the response by the category of the action performed. By default, the value of this field is \"all\" and thus, the response will include log of all operations for the defined period.<br><br>To only include response for a specific category type, provide a value for `category_type` from this [table](https://marketplace.zoom.us/docs/api-reference/other-references/phone-operation-categories). (optional) (default to all)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get operation logs report
    api_response = api_instance.get_ps_operation_logs(_from=_from, to=to, category_type=category_type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_ps_operation_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The start time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format. The date range defined by the &#x60;from&#x60; and &#x60;to&#x60; parameters should be a month as the response only includes one month&#x27;s worth of data at once. If unspecified, returns data within the 24 hours. | [optional] 
 **to** | **date**| **Required** only when the &#x60;from&#x60; parameter is specified. End time and date in **yyyy-mm-dd** or **yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;** format, the same format as the &#x60;from&#x60; parameter. | [optional] 
 **category_type** | **str**| Filter the response by the category of the action performed. By default, the value of this field is \&quot;all\&quot; and thus, the response will include log of all operations for the defined period.&lt;br&gt;&lt;br&gt;To only include response for a specific category type, provide a value for &#x60;category_type&#x60; from this [table](https://marketplace.zoom.us/docs/api-reference/other-references/phone-operation-categories). | [optional] [default to all]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

