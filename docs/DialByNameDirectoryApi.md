# swagger_client.DialByNameDirectoryApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_users_to_directory**](DialByNameDirectoryApi.md#add_users_to_directory) | **POST** /phone/dial_by_name_directory/extensions | Add users to a directory
[**add_users_to_directory_by_site**](DialByNameDirectoryApi.md#add_users_to_directory_by_site) | **POST** /phone/sites/{siteId}/dial_by_name_directory/extensions | Add users to a directory of a site
[**delete_users_from_directory**](DialByNameDirectoryApi.md#delete_users_from_directory) | **DELETE** /phone/dial_by_name_directory/extensions | Delete users from a directory
[**delete_users_from_directory_by_site**](DialByNameDirectoryApi.md#delete_users_from_directory_by_site) | **DELETE** /phone/sites/{siteId}/dial_by_name_directory/extensions | Delete users from a directory of a site
[**list_users_from_directory**](DialByNameDirectoryApi.md#list_users_from_directory) | **GET** /phone/dial_by_name_directory/extensions | List users in directory
[**list_users_from_directory_by_site**](DialByNameDirectoryApi.md#list_users_from_directory_by_site) | **GET** /phone/sites/{siteId}/dial_by_name_directory/extensions | List users in a directory by site

# **add_users_to_directory**
> add_users_to_directory(body=body)

Add users to a directory

Use this API to add users to a [directory](https://support.zoom.us/hc/en-us/articles/4404938949389-Using-a-dial-by-name-directory).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.DialByNameDirectoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DialByNameDirectoryExtensionsBody() # DialByNameDirectoryExtensionsBody |  (optional)

try:
    # Add users to a directory
    api_instance.add_users_to_directory(body=body)
except ApiException as e:
    print("Exception when calling DialByNameDirectoryApi->add_users_to_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DialByNameDirectoryExtensionsBody**](DialByNameDirectoryExtensionsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_users_to_directory_by_site**
> add_users_to_directory_by_site(site_id, body=body)

Add users to a directory of a site

Use this API to add users to a [directory](https://support.zoom.us/hc/en-us/articles/4404938949389-Using-a-dial-by-name-directory) of the specified site.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light` 

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
api_instance = swagger_client.DialByNameDirectoryApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites).
body = swagger_client.DialByNameDirectoryExtensionsBody1() # DialByNameDirectoryExtensionsBody1 |  (optional)

try:
    # Add users to a directory of a site
    api_instance.add_users_to_directory_by_site(site_id, body=body)
except ApiException as e:
    print("Exception when calling DialByNameDirectoryApi->add_users_to_directory_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). | 
 **body** | [**DialByNameDirectoryExtensionsBody1**](DialByNameDirectoryExtensionsBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_from_directory**
> delete_users_from_directory(site_id, extension_ids=extension_ids)

Delete users from a directory

Use this API to delete users from the [directory](https://support.zoom.us/hc/en-us/articles/4404938949389-Using-a-dial-by-name-directory).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.DialByNameDirectoryApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites)
extension_ids = ['extension_ids_example'] # list[str] | Extension Ids. If the value is not specified, delete the value of `site_id` from  `included sites` and delete all users related with `site_id` from directory. (optional)

try:
    # Delete users from a directory
    api_instance.delete_users_from_directory(site_id, extension_ids=extension_ids)
except ApiException as e:
    print("Exception when calling DialByNameDirectoryApi->delete_users_from_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) | 
 **extension_ids** | [**list[str]**](str.md)| Extension Ids. If the value is not specified, delete the value of &#x60;site_id&#x60; from  &#x60;included sites&#x60; and delete all users related with &#x60;site_id&#x60; from directory. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_from_directory_by_site**
> delete_users_from_directory_by_site(site_id, site_id=site_id, extension_ids=extension_ids)

Delete users from a directory of a site

Use this API to delete users from a [directory](https://support.zoom.us/hc/en-us/articles/4404938949389-Using-a-dial-by-name-directory) of the specified site.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:write:admin`  **Rate Limit Label:** `Light`

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
api_instance = swagger_client.DialByNameDirectoryApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites).
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) to which users to delete belongs (optional)
extension_ids = ['extension_ids_example'] # list[str] | Extension Ids. If the value is not specified, delete the value of `site_id` from  `included sites` and delete all users related with `site_id` from directory (optional)

try:
    # Delete users from a directory of a site
    api_instance.delete_users_from_directory_by_site(site_id, site_id=site_id, extension_ids=extension_ids)
except ApiException as e:
    print("Exception when calling DialByNameDirectoryApi->delete_users_from_directory_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). | 
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) to which users to delete belongs | [optional] 
 **extension_ids** | [**list[str]**](str.md)| Extension Ids. If the value is not specified, delete the value of &#x60;site_id&#x60; from  &#x60;included sites&#x60; and delete all users related with &#x60;site_id&#x60; from directory | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_from_directory**
> InlineResponse20094 list_users_from_directory(site_id, page_size=page_size, next_page_token=next_page_token, in_directory=in_directory)

List users in directory

Use this API to get users that are in or not in a [directory](https://support.zoom.us/hc/en-us/articles/4404938949389-Using-a-dial-by-name-directory).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Medium`

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
api_instance = swagger_client.DialByNameDirectoryApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites).
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
in_directory = false # bool | Whether the user belongs to the directory. (optional) (default to false)

try:
    # List users in directory
    api_response = api_instance.list_users_from_directory(site_id, page_size=page_size, next_page_token=next_page_token, in_directory=in_directory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DialByNameDirectoryApi->list_users_from_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **in_directory** | **bool**| Whether the user belongs to the directory. | [optional] [default to false]

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_from_directory_by_site**
> InlineResponse20095 list_users_from_directory_by_site(site_id, page_size=page_size, next_page_token=next_page_token, in_directory=in_directory, site_id=site_id)

List users in a directory by site

Use this API to get users that are in or not in a [directory](https://support.zoom.us/hc/en-us/articles/4404938949389-Using-a-dial-by-name-directory) of the specified site.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:**`phone:read:admin`  **Rate Limit Label:** `Medium`

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
api_instance = swagger_client.DialByNameDirectoryApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites).
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
in_directory = false # bool | Whether the user belongs to the directory. (optional) (default to false)
site_id = 'site_id_example' # str | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) to which users to get belongs. (optional)

try:
    # List users in a directory by site
    api_response = api_instance.list_users_from_directory_by_site(site_id, page_size=page_size, next_page_token=next_page_token, in_directory=in_directory, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DialByNameDirectoryApi->list_users_from_directory_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites). | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **in_directory** | **bool**| Whether the user belongs to the directory. | [optional] [default to false]
 **site_id** | **str**| Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) to which users to get belongs. | [optional] 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

