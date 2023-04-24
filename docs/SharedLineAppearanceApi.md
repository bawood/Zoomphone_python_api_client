# swagger_client.SharedLineAppearanceApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_shared_line_appearances**](SharedLineAppearanceApi.md#list_shared_line_appearances) | **GET** /phone/shared_line_appearances | List shared line appearances

# **list_shared_line_appearances**
> InlineResponse20063 list_shared_line_appearances(page_size=page_size, next_page_token=next_page_token)

List shared line appearances

Use this API to list [shared line appearance](https://support.zoom.us/hc/en-us/articles/4406753208461-Enabling-or-disabling-shared-lines-privacy-mode) instances.  **Prerequisites:**  * Pro or higher account with Zoom Phone license  * Account owner or admin privileges    **Scopes:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.SharedLineAppearanceApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List shared line appearances
    api_response = api_instance.list_shared_line_appearances(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLineAppearanceApi->list_shared_line_appearances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

