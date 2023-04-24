# swagger_client.PhoneNumbersApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_byoc_number**](PhoneNumbersApi.md#add_byoc_number) | **POST** /phone/byoc_numbers | Add BYOC phone numbers
[**assign_phone_number**](PhoneNumbersApi.md#assign_phone_number) | **POST** /phone/users/{userId}/phone_numbers | Assign a phone number to a user
[**assign_phone_number_to_emergency_number_pool**](PhoneNumbersApi.md#assign_phone_number_to_emergency_number_pool) | **POST** /phone/emergency_number_pools/phone_numbers | Assign phone numbers to the emergency number pool
[**delete_unassigned_phone_numbers**](PhoneNumbersApi.md#delete_unassigned_phone_numbers) | **DELETE** /phone/numbers | Delete unassigned phone numbers
[**get_phone_number_details**](PhoneNumbersApi.md#get_phone_number_details) | **GET** /phone/numbers/{numberId} | Get a phone number
[**list_account_phone_numbers**](PhoneNumbersApi.md#list_account_phone_numbers) | **GET** /phone/numbers | List phone numbers
[**unassign_phone_number**](PhoneNumbersApi.md#unassign_phone_number) | **DELETE** /phone/users/{userId}/phone_numbers/{phoneNumberId} | Unassign a phone number
[**unassign_phone_number_from_emergency_number_pool**](PhoneNumbersApi.md#unassign_phone_number_from_emergency_number_pool) | **DELETE** /phone/emergency_number_pools/phone_numbers/{phoneNumberId} | Unassign phone numbers from the emergency number pool
[**update_phone_number_details**](PhoneNumbersApi.md#update_phone_number_details) | **PATCH** /phone/numbers/{numberId} | Update a phone number
[**update_site_for_unassigned_phone_numbers**](PhoneNumbersApi.md#update_site_for_unassigned_phone_numbers) | **PATCH** /phone/numbers/sites/{siteId} | Update a site&#x27;s unassigned phone numbers

# **add_byoc_number**
> InlineResponse2014 add_byoc_number(body=body)

Add BYOC phone numbers

Use this API to add BYOC (Bring Your Own Carrier) phone numbers to Zoom Phone.  **Scopes:** `phone:write:admin`, `phone:write`, or `phone:master`</br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise plan  * A Zoom Phone license

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneByocNumbersBody() # PhoneByocNumbersBody |  (optional)

try:
    # Add BYOC phone numbers
    api_response = api_instance.add_byoc_number(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->add_byoc_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneByocNumbersBody**](PhoneByocNumbersBody.md)|  | [optional] 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_number**
> InlineResponse20084 assign_phone_number(user_id, body=body)

Assign a phone number to a user

Assigns a [phone number](https://support.zoom.us/hc/en-us/articles/360020808292-Managing-Phone-Numbers) to a user who has already enabled Zoom Phone.  **Scopes:** `phone:write`, `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = swagger_client.UserIdPhoneNumbersBody() # UserIdPhoneNumbersBody | Provide either the ID or phone number in the request body. (optional)

try:
    # Assign a phone number to a user
    api_response = api_instance.assign_phone_number(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->assign_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**UserIdPhoneNumbersBody**](UserIdPhoneNumbersBody.md)| Provide either the ID or phone number in the request body. | [optional] 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_number_to_emergency_number_pool**
> InlineResponse20029 assign_phone_number_to_emergency_number_pool(body=body)

Assign phone numbers to the emergency number pool

Assigns phone numbers to the [Emergency Number Pool](https://support.zoom.us/hc/en-us/articles/360062110192-Routing-emergency-calls).  **Scopes:** `phone:write`, `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmergencyNumberPoolsPhoneNumbersBody() # EmergencyNumberPoolsPhoneNumbersBody | Provide either an ID or a number in the request body. (optional)

try:
    # Assign phone numbers to the emergency number pool
    api_response = api_instance.assign_phone_number_to_emergency_number_pool(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->assign_phone_number_to_emergency_number_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmergencyNumberPoolsPhoneNumbersBody**](EmergencyNumberPoolsPhoneNumbersBody.md)| Provide either an ID or a number in the request body. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_unassigned_phone_numbers**
> delete_unassigned_phone_numbers(phone_numbers)

Delete unassigned phone numbers

Deletes unassigned [phone numbers](https://support.zoom.us/hc/en-us/articles/360020808292-Managing-Phone-Numbers#h_38ba8b01-26e3-4b1b-a9b5-0717c00a7ca6). Up to 20 phone numbers can be removed in a single request.  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  * The user must have been previously assigned a Zoom Phone number  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
phone_numbers = ['phone_numbers_example'] # list[str] | Comma seperated list of unassigned phone numbers in E164 format or phone number IDs.

try:
    # Delete unassigned phone numbers
    api_instance.delete_unassigned_phone_numbers(phone_numbers)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->delete_unassigned_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_numbers** | [**list[str]**](str.md)| Comma seperated list of unassigned phone numbers in E164 format or phone number IDs. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_number_details**
> InlineResponse20046 get_phone_number_details(number_id)

Get a phone number

Gets information about an account's Zoom Phone number.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom phone license

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
number_id = 'number_id_example' # str | Unique Identifier of the Phone Number. This can be retrieved from the List Phone Numbers API.

try:
    # Get a phone number
    api_response = api_instance.get_phone_number_details(number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->get_phone_number_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number_id** | **str**| Unique Identifier of the Phone Number. This can be retrieved from the List Phone Numbers API. | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_phone_numbers**
> InlineResponse20045 list_account_phone_numbers(next_page_token=next_page_token, type=type, extension_type=extension_type, page_size=page_size, number_type=number_type, pending_numbers=pending_numbers, site_id=site_id)

List phone numbers

Lists all Zoom Phone numbers in a Zoom account.  **Scopes:** `phone:read:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`  **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
type = 'type_example' # str | The query response by number assignment. The value can be one of the following: <br> `assigned`: The number has been assigned to either a user, a call queue, an auto-receptionist or a common area in an account. <br>`unassigned`: The number is not assigned to anyone.<br> `all`: Include both assigned and unassigned numbers in the response.<br> `byoc`: Include Bring Your Own Carrier (BYOC) numbers only in the response. (optional)
extension_type = 'extension_type_example' # str | The type of assignee to whom the number is assigned. The parameter can be set only if `type` parameter is set as `assigned`. The value can be one of the following:<br> `user`<br> `callQueue`<br> `autoReceptionist`<br> `commonAreaPhone` (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
number_type = 'number_type_example' # str | The type of phone number. The value can be either `toll` or `tollfree`. (optional)
pending_numbers = true # bool | Include or exclude pending numbers in the response. The value can be either `true` or `false`. (optional)
site_id = 'site_id_example' # str | Unique identifier of the site. Use this query parameter if you have enabled multiple sites and would like to filter the response of this API call by a specific phone site. See [Managing multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) or [Adding a site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15) for details. (optional)

try:
    # List phone numbers
    api_response = api_instance.list_account_phone_numbers(next_page_token=next_page_token, type=type, extension_type=extension_type, page_size=page_size, number_type=number_type, pending_numbers=pending_numbers, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->list_account_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **type** | **str**| The query response by number assignment. The value can be one of the following: &lt;br&gt; &#x60;assigned&#x60;: The number has been assigned to either a user, a call queue, an auto-receptionist or a common area in an account. &lt;br&gt;&#x60;unassigned&#x60;: The number is not assigned to anyone.&lt;br&gt; &#x60;all&#x60;: Include both assigned and unassigned numbers in the response.&lt;br&gt; &#x60;byoc&#x60;: Include Bring Your Own Carrier (BYOC) numbers only in the response. | [optional] 
 **extension_type** | **str**| The type of assignee to whom the number is assigned. The parameter can be set only if &#x60;type&#x60; parameter is set as &#x60;assigned&#x60;. The value can be one of the following:&lt;br&gt; &#x60;user&#x60;&lt;br&gt; &#x60;callQueue&#x60;&lt;br&gt; &#x60;autoReceptionist&#x60;&lt;br&gt; &#x60;commonAreaPhone&#x60; | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **number_type** | **str**| The type of phone number. The value can be either &#x60;toll&#x60; or &#x60;tollfree&#x60;. | [optional] 
 **pending_numbers** | **bool**| Include or exclude pending numbers in the response. The value can be either &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **site_id** | **str**| Unique identifier of the site. Use this query parameter if you have enabled multiple sites and would like to filter the response of this API call by a specific phone site. See [Managing multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) or [Adding a site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15) for details. | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_phone_number**
> object unassign_phone_number(user_id, phone_number_id)

Unassign a phone number

Unassigns Zoom Phone user's [phone number](https://support.zoom.us/hc/en-us/articles/360020808292-Managing-Phone-Numbers#h_38ba8b01-26e3-4b1b-a9b5-0717c00a7ca6).  After assigning a phone number, you can remove it if you do not want it to be assigned to anyone.  **Scopes:** `phone:write`, `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license  * The user must have been previously assigned a Zoom Phone number

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | Provide either userId or email address of the user.
phone_number_id = 'phone_number_id_example' # str | Provide either phone number or phoneNumberId of the user. 

try:
    # Unassign a phone number
    api_response = api_instance.unassign_phone_number(user_id, phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->unassign_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Provide either userId or email address of the user. | 
 **phone_number_id** | **str**| Provide either phone number or phoneNumberId of the user.  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_phone_number_from_emergency_number_pool**
> object unassign_phone_number_from_emergency_number_pool(phone_number_id, site_id=site_id)

Unassign phone numbers from the emergency number pool

Unassigns phone numbers from the [Emergency Number Pool](https://support.zoom.us/hc/en-us/articles/360062110192-Routing-emergency-calls).  **Scopes:** `phone:write`, `phone:write:admin`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
phone_number_id = 'phone_number_id_example' # str | Provide either the phone number or the `phoneNumberId`.
site_id = 'site_id_example' # str | Required if multiple sites are enabled. Unique identifier of the site (optional)

try:
    # Unassign phone numbers from the emergency number pool
    api_response = api_instance.unassign_phone_number_from_emergency_number_pool(phone_number_id, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->unassign_phone_number_from_emergency_number_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**| Provide either the phone number or the &#x60;phoneNumberId&#x60;. | 
 **site_id** | **str**| Required if multiple sites are enabled. Unique identifier of the site | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_number_details**
> object update_phone_number_details(number_id, body=body)

Update a phone number

Updates a Zoom Phone number's information.  **Scopes:** `phone:write`, `phone:write:admin`, `phone:master`<br>**[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Paid account

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
number_id = 'number_id_example' # str | Phone number ID.
body = swagger_client.NumbersNumberIdBody() # NumbersNumberIdBody |  (optional)

try:
    # Update a phone number
    api_response = api_instance.update_phone_number_details(number_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->update_phone_number_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number_id** | **str**| Phone number ID. | 
 **body** | [**NumbersNumberIdBody**](NumbersNumberIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_for_unassigned_phone_numbers**
> update_site_for_unassigned_phone_numbers(site_id, body=body)

Update a site's unassigned phone numbers

Updates a site's unassigned [phone numbers](https://support.zoom.us/hc/en-us/articles/360020808292-Managing-Phone-Numbers#h_38ba8b01-26e3-4b1b-a9b5-0717c00a7ca6). Up to 20 phone numbers can be updated in a single request.   **Prerequisites:**  * A Pro or higher account plan  * A Zoom Phone license  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.PhoneNumbersApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the site
body = swagger_client.SitesSiteIdBody() # SitesSiteIdBody |  (optional)

try:
    # Update a site's unassigned phone numbers
    api_instance.update_site_for_unassigned_phone_numbers(site_id, body=body)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->update_site_for_unassigned_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the site | 
 **body** | [**SitesSiteIdBody**](SitesSiteIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

