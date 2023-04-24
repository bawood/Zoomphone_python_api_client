# swagger_client.SMSCampaignApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_campaign_phone_numbers**](SMSCampaignApi.md#assign_campaign_phone_numbers) | **POST** /phone/sms_campaigns/{smsCampaignId}/phone_numbers | Assign a phone number to SMS campaign
[**get_sms_campaign**](SMSCampaignApi.md#get_sms_campaign) | **GET** /phone/sms_campaigns/{smsCampaignId} | Get an SMS campaign
[**list_account_sms_campaigns**](SMSCampaignApi.md#list_account_sms_campaigns) | **GET** /phone/sms_campaigns | List SMS campaigns
[**unassign_campaign_phone_number**](SMSCampaignApi.md#unassign_campaign_phone_number) | **DELETE** /phone/sms_campaigns/{smsCampaignId}/phone_numbers/{phoneNumberId} | Unassign a phone number

# **assign_campaign_phone_numbers**
> InlineResponse20131 assign_campaign_phone_numbers(sms_campaign_id, body=body)

Assign a phone number to SMS campaign

Use this API to [assign a phone number to the SMS campaign](https://support.zoom.us/hc/en-us/articles/5016496738445-SMS-MMS-10DLC-Compliance-for-Zoom-Phone-and-Zoom-Contact-Center#h_01FYVVQM1WMW5JD48YNY3J581B).  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SMSCampaignApi(swagger_client.ApiClient(configuration))
sms_campaign_id = 'sms_campaign_id_example' # str | 
body = swagger_client.SmsCampaignIdPhoneNumbersBody() # SmsCampaignIdPhoneNumbersBody | Provide either the phone number ID or the phone number in the request body. (optional)

try:
    # Assign a phone number to SMS campaign
    api_response = api_instance.assign_campaign_phone_numbers(sms_campaign_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignApi->assign_campaign_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_campaign_id** | **str**|  | 
 **body** | [**SmsCampaignIdPhoneNumbersBody**](SmsCampaignIdPhoneNumbersBody.md)| Provide either the phone number ID or the phone number in the request body. | [optional] 

### Return type

[**InlineResponse20131**](InlineResponse20131.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sms_campaign**
> InlineResponse200108 get_sms_campaign(sms_campaign_id)

Get an SMS campaign

Use this API to get a specific SMS campaign.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SMSCampaignApi(swagger_client.ApiClient(configuration))
sms_campaign_id = 'sms_campaign_id_example' # str | 

try:
    # Get an SMS campaign
    api_response = api_instance.get_sms_campaign(sms_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignApi->get_sms_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_campaign_id** | **str**|  | 

### Return type

[**InlineResponse200108**](InlineResponse200108.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_sms_campaigns**
> InlineResponse200107 list_account_sms_campaigns(page_size=page_size, next_page_token=next_page_token)

List SMS campaigns

Use this API to list all SMS campaigns in a Zoom account.  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.SMSCampaignApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List SMS campaigns
    api_response = api_instance.list_account_sms_campaigns(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignApi->list_account_sms_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse200107**](InlineResponse200107.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_campaign_phone_number**
> object unassign_campaign_phone_number(sms_campaign_id, phone_number_id)

Unassign a phone number

Use this API to [unassign a phone number from the SMS campaign](https://support.zoom.us/hc/en-us/articles/5016496738445-SMS-MMS-10DLC-Compliance-for-Zoom-Phone-and-Zoom-Contact-Center#h_01FYVVSPVM8MZN4Y9EW5690QHH). Remove the assigned phone number from the campaign.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  * The campaign must have been previously assigned a Zoom Phone number  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.SMSCampaignApi(swagger_client.ApiClient(configuration))
sms_campaign_id = 'sms_campaign_id_example' # str | 
phone_number_id = 'phone_number_id_example' # str | Provide either phone number (in E164 format) or phoneNumberId of the campaign. 

try:
    # Unassign a phone number
    api_response = api_instance.unassign_campaign_phone_number(sms_campaign_id, phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignApi->unassign_campaign_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_campaign_id** | **str**|  | 
 **phone_number_id** | **str**| Provide either phone number (in E164 format) or phoneNumberId of the campaign.  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

