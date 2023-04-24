# swagger_client.EmergencyServiceLocationsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_location**](EmergencyServiceLocationsApi.md#add_location) | **POST** /phone/locations | Add an emergency service location
[**batch_add_locations**](EmergencyServiceLocationsApi.md#batch_add_locations) | **POST** /phone/batch_locations | Batch add emergency service locations
[**delete_location**](EmergencyServiceLocationsApi.md#delete_location) | **DELETE** /phone/locations/{locationId} | Delete an emergency location
[**get_location**](EmergencyServiceLocationsApi.md#get_location) | **GET** /phone/locations/{locationId} | Get emergency service location details
[**list_locations**](EmergencyServiceLocationsApi.md#list_locations) | **GET** /phone/locations | List emergency service locations
[**update_location**](EmergencyServiceLocationsApi.md#update_location) | **PATCH** /phone/locations/{locationId} | Update emergency service location

# **add_location**
> InlineResponse20118 add_location(body=body)

Add an emergency service location

Adds an emergency service location.  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.EmergencyServiceLocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneLocationsBody() # PhoneLocationsBody |  (optional)

try:
    # Add an emergency service location
    api_response = api_instance.add_location(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyServiceLocationsApi->add_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneLocationsBody**](PhoneLocationsBody.md)|  | [optional] 

### Return type

[**InlineResponse20118**](InlineResponse20118.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_add_locations**
> InlineResponse2012 batch_add_locations(body=body)

Batch add emergency service locations

Batches the add emergency service locations.  **Prerequisites:** * Pro or higher account plan with Zoom phone license * Account owner or admin permissions  **Scope:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.EmergencyServiceLocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneBatchLocationsBody() # PhoneBatchLocationsBody |  (optional)

try:
    # Batch add emergency service locations
    api_response = api_instance.batch_add_locations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyServiceLocationsApi->batch_add_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneBatchLocationsBody**](PhoneBatchLocationsBody.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location**
> object delete_location(location_id)

Delete an emergency location

Removes an emergency location.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyServiceLocationsApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | The emergency service location's ID.

try:
    # Delete an emergency location
    api_response = api_instance.delete_location(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyServiceLocationsApi->delete_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The emergency service location&#x27;s ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location**
> InlineResponse20035 get_location(location_id)

Get emergency service location details

Returns an emergency service location's information.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyServiceLocationsApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | The emergency service location's ID.

try:
    # Get emergency service location details
    api_response = api_instance.get_location(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyServiceLocationsApi->get_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The emergency service location&#x27;s ID. | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_locations**
> InlineResponse20034 list_locations(next_page_token=next_page_token, page_size=page_size, site_id=site_id)

List emergency service locations

Lists the emergency service locations.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyServiceLocationsApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
site_id = 'site_id_example' # str | The unique identifier of the site. It can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. (optional)

try:
    # List emergency service locations
    api_response = api_instance.list_locations(next_page_token=next_page_token, page_size=page_size, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyServiceLocationsApi->list_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **site_id** | **str**| The unique identifier of the site. It can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location**
> object update_location(location_id, body=body)

Update emergency service location

Updates an emergency location's information.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions

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
api_instance = swagger_client.EmergencyServiceLocationsApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | The emergency service location's ID.
body = swagger_client.LocationsLocationIdBody() # LocationsLocationIdBody |  (optional)

try:
    # Update emergency service location
    api_response = api_instance.update_location(location_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmergencyServiceLocationsApi->update_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The emergency service location&#x27;s ID. | 
 **body** | [**LocationsLocationIdBody**](LocationsLocationIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

