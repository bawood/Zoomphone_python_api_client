# swagger_client.IVRApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auto_receptionist_ivr**](IVRApi.md#get_auto_receptionist_ivr) | **GET** /phone/auto_receptionists/{autoReceptionistId}/ivr | Get auto receptionist IVR
[**update_auto_receptionist_ivr**](IVRApi.md#update_auto_receptionist_ivr) | **PATCH** /phone/auto_receptionists/{autoReceptionistId}/ivr | Update auto receptionist IVR

# **get_auto_receptionist_ivr**
> InlineResponse2004 get_auto_receptionist_ivr(auto_receptionist_id, hours_type=hours_type, holiday_id=holiday_id)

Get auto receptionist IVR

Gets an [interactive voice response (IVR) system](https://support.zoom.us/hc/en-us/articles/360038601971) of the specified auto receptionist.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.IVRApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The unique identifier of the auto receptionist. It can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API.
hours_type = 'business_hours' # str | The query hours type: `business_hours` or `closed_hours`, default `business_hours`. (optional) (default to business_hours)
holiday_id = 'holiday_id_example' # str | The auto receptionist holiday hours ID. If both `holiday_id` and `hours_type` are passed, `holiday_id` has a high priority and `hours_type` is invalid. (optional)

try:
    # Get auto receptionist IVR
    api_response = api_instance.get_auto_receptionist_ivr(auto_receptionist_id, hours_type=hours_type, holiday_id=holiday_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->get_auto_receptionist_ivr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The unique identifier of the auto receptionist. It can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. | 
 **hours_type** | **str**| The query hours type: &#x60;business_hours&#x60; or &#x60;closed_hours&#x60;, default &#x60;business_hours&#x60;. | [optional] [default to business_hours]
 **holiday_id** | **str**| The auto receptionist holiday hours ID. If both &#x60;holiday_id&#x60; and &#x60;hours_type&#x60; are passed, &#x60;holiday_id&#x60; has a high priority and &#x60;hours_type&#x60; is invalid. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_receptionist_ivr**
> object update_auto_receptionist_ivr(auto_receptionist_id, body=body)

Update auto receptionist IVR

Updates the [interactive voice response (IVR) system](https://support.zoom.us/hc/en-us/articles/360038601971) of the specified auto receptionist.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.IVRApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | The auto receptionist id.
body = swagger_client.AutoReceptionistIdIvrBody() # AutoReceptionistIdIvrBody |  (optional)

try:
    # Update auto receptionist IVR
    api_response = api_instance.update_auto_receptionist_ivr(auto_receptionist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->update_auto_receptionist_ivr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| The auto receptionist id. | 
 **body** | [**AutoReceptionistIdIvrBody**](AutoReceptionistIdIvrBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

