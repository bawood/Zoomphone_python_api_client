# swagger_client.CommonAreasApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_common_area**](CommonAreasApi.md#add_common_area) | **POST** /phone/common_areas | Add a common area
[**add_common_area_setting**](CommonAreasApi.md#add_common_area_setting) | **POST** /phone/common_areas/{commonAreaId}/settings/{settingType} | Add common area settings
[**assign_calling_plans_to_common_area**](CommonAreasApi.md#assign_calling_plans_to_common_area) | **POST** /phone/common_areas/{commonAreaId}/calling_plans | Assign calling plans to a common area
[**assign_phone_numbers_to_common_area**](CommonAreasApi.md#assign_phone_numbers_to_common_area) | **POST** /phone/common_areas/{commonAreaId}/phone_numbers | Assign phone numbers to a common area
[**delete_common_area**](CommonAreasApi.md#delete_common_area) | **DELETE** /phone/common_areas/{commonAreaId} | Delete a common area
[**delete_common_area_setting**](CommonAreasApi.md#delete_common_area_setting) | **DELETE** /phone/common_areas/{commonAreaId}/settings/{settingType} | Delete common area setting
[**get_a_common_area**](CommonAreasApi.md#get_a_common_area) | **GET** /phone/common_areas/{commonAreaId} | Get common area details
[**get_common_area_policy_details**](CommonAreasApi.md#get_common_area_policy_details) | **GET** /phone/common_areas/{commonAreaId}/policies/{policyType} | Get common area policy details
[**get_common_area_settings**](CommonAreasApi.md#get_common_area_settings) | **GET** /phone/common_areas/{commonAreaId}/settings | Get common area settings
[**list_common_areas**](CommonAreasApi.md#list_common_areas) | **GET** /phone/common_areas | List common areas
[**unassign_calling_plans_from_common_area**](CommonAreasApi.md#unassign_calling_plans_from_common_area) | **DELETE** /phone/common_areas/{commonAreaId}/calling_plans/{type} | Unassign a calling plan from the common area
[**unassign_phone_numbers_from_common_area**](CommonAreasApi.md#unassign_phone_numbers_from_common_area) | **DELETE** /phone/common_areas/{commonAreaId}/phone_numbers/{phoneNumberId} | Unassign phone numbers from common area
[**update_common_area**](CommonAreasApi.md#update_common_area) | **PATCH** /phone/common_areas/{commonAreaId} | Update common area
[**update_common_area_policy**](CommonAreasApi.md#update_common_area_policy) | **PATCH** /phone/common_areas/{commonAreaId}/policies/{policyType} | Update common area policy
[**update_common_area_setting**](CommonAreasApi.md#update_common_area_setting) | **PATCH** /phone/common_areas/{commonAreaId}/settings/{settingType} | Update common area settings

# **add_common_area**
> InlineResponse20110 add_common_area(body=body)

Add a common area

Use this API to add an instance of common area. Configure devices shared by users and deployed in shared spaces.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license * Account owner or admin permissions  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneCommonAreasBody() # PhoneCommonAreasBody |  (optional)

try:
    # Add a common area
    api_response = api_instance.add_common_area(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->add_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneCommonAreasBody**](PhoneCommonAreasBody.md)|  | [optional] 

### Return type

[**InlineResponse20110**](InlineResponse20110.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_common_area_setting**
> InlineResponse20113 add_common_area_setting(common_area_id, setting_type, body=body)

Add common area settings

Use this API to add the common area setting according to the setting type, specifically for desk phones.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scope:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.
setting_type = 'setting_type_example' # str | Corresponds to the setting item you wish to modify. Allowed values: `desk_phone`
body = swagger_client.SettingsSettingTypeBody() # SettingsSettingTypeBody |  (optional)

try:
    # Add common area settings
    api_response = api_instance.add_common_area_setting(common_area_id, setting_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->add_common_area_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 
 **setting_type** | **str**| Corresponds to the setting item you wish to modify. Allowed values: &#x60;desk_phone&#x60; | 
 **body** | [**SettingsSettingTypeBody**](SettingsSettingTypeBody.md)|  | [optional] 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_calling_plans_to_common_area**
> InlineResponse20111 assign_calling_plans_to_common_area(common_area_id, body=body)

Assign calling plans to a common area

Use this API to assign calling plans to a common area.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scope:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.
body = swagger_client.CommonAreaIdCallingPlansBody() # CommonAreaIdCallingPlansBody |  (optional)

try:
    # Assign calling plans to a common area
    api_response = api_instance.assign_calling_plans_to_common_area(common_area_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->assign_calling_plans_to_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 
 **body** | [**CommonAreaIdCallingPlansBody**](CommonAreaIdCallingPlansBody.md)|  | [optional] 

### Return type

[**InlineResponse20111**](InlineResponse20111.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_numbers_to_common_area**
> InlineResponse20112 assign_phone_numbers_to_common_area(common_area_id, body=body)

Assign phone numbers to a common area

Assign phone numbers to a common area.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scope:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.
body = swagger_client.CommonAreaIdPhoneNumbersBody() # CommonAreaIdPhoneNumbersBody |  (optional)

try:
    # Assign phone numbers to a common area
    api_response = api_instance.assign_phone_numbers_to_common_area(common_area_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->assign_phone_numbers_to_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 
 **body** | [**CommonAreaIdPhoneNumbersBody**](CommonAreaIdPhoneNumbersBody.md)|  | [optional] 

### Return type

[**InlineResponse20112**](InlineResponse20112.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_common_area**
> object delete_common_area(common_area_id)

Delete a common area

Use this API to remove the common area.   **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.

try:
    # Delete a common area
    api_response = api_instance.delete_common_area(common_area_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->delete_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_common_area_setting**
> object delete_common_area_setting(common_area_id, setting_type, device_id)

Delete common area setting

Use this API to remove the common area subsetting from desk phones.   **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.
setting_type = 'setting_type_example' # str | Corresponds to the setting item you wish to modify. Allowed values: `desk_phone`
device_id = 'device_id_example' # str | Desk phone ID.

try:
    # Delete common area setting
    api_response = api_instance.delete_common_area_setting(common_area_id, setting_type, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->delete_common_area_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 
 **setting_type** | **str**| Corresponds to the setting item you wish to modify. Allowed values: &#x60;desk_phone&#x60; | 
 **device_id** | **str**| Desk phone ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_common_area**
> InlineResponse20020 get_a_common_area(common_area_id)

Get common area details

Use this API to get detailed information on the common area.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license * Account owner or admin permissions  **Scopes:** `phone:read:admin`<br> **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.

try:
    # Get common area details
    api_response = api_instance.get_a_common_area(common_area_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->get_a_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_common_area_policy_details**
> InlineResponse20022 get_common_area_policy_details()

Get common area policy details

Gets the common area policy details.  **Prerequisites:** * Pro or higher account plan with Zoom phone license  **Scope:** `phone:read:admin`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))

try:
    # Get common area policy details
    api_response = api_instance.get_common_area_policy_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->get_common_area_policy_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_common_area_settings**
> InlineResponse20021 get_common_area_settings(common_area_id)

Get common area settings

Use this API to get common area settings.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scope:** `phone:read:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | 

try:
    # Get common area settings
    api_response = api_instance.get_common_area_settings(common_area_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->get_common_area_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**|  | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_common_areas**
> InlineResponse20019 list_common_areas(page_size=page_size, next_page_token=next_page_token)

List common areas

Use this API to list common areas under an account.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:**  * Pro or a higher account with Zoom Phone license  * Account owner or admin permissions  **Scopes:** `phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List common areas
    api_response = api_instance.list_common_areas(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->list_common_areas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_calling_plans_from_common_area**
> unassign_calling_plans_from_common_area(common_area_id, type, billing_account_id=billing_account_id)

Unassign a calling plan from the common area

Use this API to unassign a calling plan from the common area.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:**  * A Pro or higher account with a Zoom Phone license  * An account owner or admin permissions   **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.
type = 'type_example' # str | Zoom Phone [calling plan](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) to remove.
billing_account_id = 'billing_account_id_example' # str | Billing account ID. If the common area is in India, the parameter is required. (optional)

try:
    # Unassign a calling plan from the common area
    api_instance.unassign_calling_plans_from_common_area(common_area_id, type, billing_account_id=billing_account_id)
except ApiException as e:
    print("Exception when calling CommonAreasApi->unassign_calling_plans_from_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 
 **type** | **str**| Zoom Phone [calling plan](https://marketplace.zoom.us/docs/api-reference/other-references/plans#zoom-phone-calling-plans) to remove. | 
 **billing_account_id** | **str**| Billing account ID. If the common area is in India, the parameter is required. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_phone_numbers_from_common_area**
> unassign_phone_numbers_from_common_area(common_area_id, phone_number_id)

Unassign phone numbers from common area

Use this API to unassign a phone number from a common area.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * A Pro or a higher account with a Zoom Phone license * An account owner or admin permissions  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | Common area ID or common area extension ID.
phone_number_id = 'phone_number_id_example' # str | The phone number or the phone number ID.

try:
    # Unassign phone numbers from common area
    api_instance.unassign_phone_numbers_from_common_area(common_area_id, phone_number_id)
except ApiException as e:
    print("Exception when calling CommonAreasApi->unassign_phone_numbers_from_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**| Common area ID or common area extension ID. | 
 **phone_number_id** | **str**| The phone number or the phone number ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_area**
> object update_common_area(common_area_id, body=body)

Update common area

Use this API to update the common area information.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:**  * Pro or a higher account with Zoom Phone license * Account owner or admin permissions  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | 
body = swagger_client.CommonAreasCommonAreaIdBody() # CommonAreasCommonAreaIdBody |  (optional)

try:
    # Update common area
    api_response = api_instance.update_common_area(common_area_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->update_common_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**|  | 
 **body** | [**CommonAreasCommonAreaIdBody**](CommonAreasCommonAreaIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_area_policy**
> object update_common_area_policy(body=body)

Update common area policy

Updates a common area's [Zoom Phone](https://support.zoom.us/hc/en-us/categories/360001370051-Zoom-Phone) policy.  **Scopes:** `phone:write:admin`<br>**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
body = swagger_client.PoliciesPolicyTypeBody4() # PoliciesPolicyTypeBody4 |  (optional)

try:
    # Update common area policy
    api_response = api_instance.update_common_area_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->update_common_area_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoliciesPolicyTypeBody4**](PoliciesPolicyTypeBody4.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_area_setting**
> object update_common_area_setting(common_area_id, setting_type, body=body)

Update common area settings

Use this API to update the common area setting according to the setting type, specifically for desk phones.  **Note**: For use by customers who opted for `Common Area Optimization`    **Prerequisites:** * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions.  **Scope:** `phone:write:admin`   **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.CommonAreasApi(swagger_client.ApiClient(configuration))
common_area_id = 'common_area_id_example' # str | 
setting_type = 'setting_type_example' # str | Corresponds to the setting item you wish to modify. Allowed values: `desk_phone`
body = swagger_client.SettingsSettingTypeBody1() # SettingsSettingTypeBody1 |  (optional)

try:
    # Update common area settings
    api_response = api_instance.update_common_area_setting(common_area_id, setting_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreasApi->update_common_area_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_id** | **str**|  | 
 **setting_type** | **str**| Corresponds to the setting item you wish to modify. Allowed values: &#x60;desk_phone&#x60; | 
 **body** | [**SettingsSettingTypeBody1**](SettingsSettingTypeBody1.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

