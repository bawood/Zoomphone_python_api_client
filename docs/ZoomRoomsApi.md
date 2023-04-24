# swagger_client.ZoomRoomsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_zoom_room**](ZoomRoomsApi.md#add_zoom_room) | **POST** /phone/rooms | Add a Zoom Room to a Zoom Phone
[**assign_calling_plan_to_room**](ZoomRoomsApi.md#assign_calling_plan_to_room) | **POST** /phone/rooms/{roomId}/calling_plans | Assign calling plans to a Zoom Room
[**assign_phone_number_to_zoom_room**](ZoomRoomsApi.md#assign_phone_number_to_zoom_room) | **POST** /phone/rooms/{roomId}/phone_numbers | Assign phone numbers to a Zoom Room
[**get_zoom_room**](ZoomRoomsApi.md#get_zoom_room) | **GET** /phone/rooms/{roomId} | Get a Zoom Room under Zoom Phone license
[**list_unassigned_zoom_rooms**](ZoomRoomsApi.md#list_unassigned_zoom_rooms) | **GET** /phone/rooms/unassigned | List Zoom Rooms without Zoom Phone assignment
[**list_zoom_rooms**](ZoomRoomsApi.md#list_zoom_rooms) | **GET** /phone/rooms | List Zoom Rooms under Zoom Phone license
[**remove_zoom_room**](ZoomRoomsApi.md#remove_zoom_room) | **DELETE** /phone/rooms/{roomId} | Remove a Zoom Room from a ZP account
[**unassign_calling_plan_from_room**](ZoomRoomsApi.md#unassign_calling_plan_from_room) | **DELETE** /phone/rooms/{roomId}/calling_plans/{type} | Remove a calling plan from a Zoom Room
[**unassign_phone_number_from_zoom_room**](ZoomRoomsApi.md#unassign_phone_number_from_zoom_room) | **DELETE** /phone/rooms/{roomId}/phone_numbers/{phoneNumberId} | Remove a phone number from a Zoom Room
[**update_zoom_room**](ZoomRoomsApi.md#update_zoom_room) | **PATCH** /phone/rooms/{roomId} | Update a Zoom Room under Zoom Phone license

# **add_zoom_room**
> object add_zoom_room(body=body)

Add a Zoom Room to a Zoom Phone

Use this API to associate a [Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711#h_70c74c57-50d6-406b-a4fa-2f33d4bebdbc) with a Zoom Phone license.   **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneRoomsBody() # PhoneRoomsBody |  (optional)

try:
    # Add a Zoom Room to a Zoom Phone
    api_response = api_instance.add_zoom_room(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->add_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneRoomsBody**](PhoneRoomsBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_calling_plan_to_room**
> object assign_calling_plan_to_room(room_id, body=body)

Assign calling plans to a Zoom Room

Use this API to assign [calling plans](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) to a [Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711#h_70c74c57-50d6-406b-a4fa-2f33d4bebdbc). Up to 200 numbers at a time.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
room_id = 'room_id_example' # str | 
body = swagger_client.RoomIdCallingPlansBody() # RoomIdCallingPlansBody |  (optional)

try:
    # Assign calling plans to a Zoom Room
    api_response = api_instance.assign_calling_plan_to_room(room_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->assign_calling_plan_to_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**|  | 
 **body** | [**RoomIdCallingPlansBody**](RoomIdCallingPlansBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_number_to_zoom_room**
> object assign_phone_number_to_zoom_room(room_id, body=body)

Assign phone numbers to a Zoom Room

Use this API to [assign phone numbers to a Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711). Up to 200 numbers at a time.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
room_id = 'room_id_example' # str | 
body = swagger_client.RoomIdPhoneNumbersBody() # RoomIdPhoneNumbersBody | Provide either the ID or phone number in the request body. (optional)

try:
    # Assign phone numbers to a Zoom Room
    api_response = api_instance.assign_phone_number_to_zoom_room(room_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->assign_phone_number_to_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**|  | 
 **body** | [**RoomIdPhoneNumbersBody**](RoomIdPhoneNumbersBody.md)| Provide either the ID or phone number in the request body. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zoom_room**
> InlineResponse20057 get_zoom_room(room_id)

Get a Zoom Room under Zoom Phone license

Use this API to get a specific [Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711) in an account that has the Zoom Phone license assigned.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
room_id = 'room_id_example' # str | 

try:
    # Get a Zoom Room under Zoom Phone license
    api_response = api_instance.get_zoom_room(room_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->get_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**|  | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unassigned_zoom_rooms**
> InlineResponse20056 list_unassigned_zoom_rooms(keyword=keyword)

List Zoom Rooms without Zoom Phone assignment

Use this API to retrieve [Zoom Rooms](https://support.zoom.us/hc/en-us/articles/360025153711) that are not assigned a Zoom Phone.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
keyword = 'keyword_example' # str | A search keyword for Zoom Room's name. (optional)

try:
    # List Zoom Rooms without Zoom Phone assignment
    api_response = api_instance.list_unassigned_zoom_rooms(keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->list_unassigned_zoom_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| A search keyword for Zoom Room&#x27;s name. | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zoom_rooms**
> InlineResponse20055 list_zoom_rooms(page_size=page_size, next_page_token=next_page_token, site_id=site_id, calling_type=calling_type)

List Zoom Rooms under Zoom Phone license

Use this API to retrieve a list of [Zoom Rooms](https://support.zoom.us/hc/en-us/articles/360025153711) under the account that has the Zoom Phone license assigned.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
site_id = 'site_id_example' # str | The site ID retrievable from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. (optional)
calling_type = 56 # int | Type of calling plan. (optional)

try:
    # List Zoom Rooms under Zoom Phone license
    api_response = api_instance.list_zoom_rooms(page_size=page_size, next_page_token=next_page_token, site_id=site_id, calling_type=calling_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->list_zoom_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **site_id** | **str**| The site ID retrievable from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. | [optional] 
 **calling_type** | **int**| Type of calling plan. | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_zoom_room**
> object remove_zoom_room(room_id)

Remove a Zoom Room from a ZP account

Use this API to remove [Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711#h_140e30ba-5a88-40b9-b799-16883fa0a037) from a Zoom Phone account.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
room_id = 'room_id_example' # str | 

try:
    # Remove a Zoom Room from a ZP account
    api_response = api_instance.remove_zoom_room(room_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->remove_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_calling_plan_from_room**
> object unassign_calling_plan_from_room(room_id, type, billing_account_id=billing_account_id)

Remove a calling plan from a Zoom Room

Use this API to unassign a [calling plan](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) from a [Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711#h_140e30ba-5a88-40b9-b799-16883fa0a037).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
room_id = 'room_id_example' # str | 
type = 56 # int | The [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) of the calling plan that was assigned to the Zoom Room. (e.g: The value of type would be \"200\" for Unlimited US/Canada calling plan.) 
billing_account_id = 'billing_account_id_example' # str | The billing account ID. If the zoom room is located in India, the parameter is required. (optional)

try:
    # Remove a calling plan from a Zoom Room
    api_response = api_instance.unassign_calling_plan_from_room(room_id, type, billing_account_id=billing_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->unassign_calling_plan_from_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**|  | 
 **type** | **int**| The [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) of the calling plan that was assigned to the Zoom Room. (e.g: The value of type would be \&quot;200\&quot; for Unlimited US/Canada calling plan.)  | 
 **billing_account_id** | **str**| The billing account ID. If the zoom room is located in India, the parameter is required. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_phone_number_from_zoom_room**
> object unassign_phone_number_from_zoom_room(room_id, phone_number_id)

Remove a phone number from a Zoom Room

Use this API to unassign a [phone number](https://support.zoom.us/hc/en-us/articles/360020808292-Managing-Phone-Numbers#h_38ba8b01-26e3-4b1b-a9b5-0717c00a7ca6) from a [Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711#h_140e30ba-5a88-40b9-b799-16883fa0a037).  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  * The Zoom Room must have been previously assigned a Zoom Phone number

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
room_id = 'room_id_example' # str | Provide roomId of the Zoom Room.
phone_number_id = 'phone_number_id_example' # str | Provide phoneNumberId of the Zoom Room. 

try:
    # Remove a phone number from a Zoom Room
    api_response = api_instance.unassign_phone_number_from_zoom_room(room_id, phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->unassign_phone_number_from_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Provide roomId of the Zoom Room. | 
 **phone_number_id** | **str**| Provide phoneNumberId of the Zoom Room.  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zoom_room**
> object update_zoom_room(room_id, body=body)

Update a Zoom Room under Zoom Phone license

Use this API to update a [Zoom Room](https://support.zoom.us/hc/en-us/articles/360025153711) in an account that has the Zoom Phone license assigned.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.ZoomRoomsApi(swagger_client.ApiClient(configuration))
room_id = 'room_id_example' # str | 
body = swagger_client.RoomsRoomIdBody() # RoomsRoomIdBody |  (optional)

try:
    # Update a Zoom Room under Zoom Phone license
    api_response = api_instance.update_zoom_room(room_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoomRoomsApi->update_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**|  | 
 **body** | [**RoomsRoomIdBody**](RoomsRoomIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

