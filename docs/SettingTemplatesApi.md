# swagger_client.SettingTemplatesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_setting_template**](SettingTemplatesApi.md#add_setting_template) | **POST** /phone/setting_templates | Add a setting template
[**get_setting_template**](SettingTemplatesApi.md#get_setting_template) | **GET** /phone/setting_templates/{templateId} | Get setting template details
[**list_setting_templates**](SettingTemplatesApi.md#list_setting_templates) | **GET** /phone/setting_templates | List setting templates
[**update_setting_template**](SettingTemplatesApi.md#update_setting_template) | **PATCH** /phone/setting_templates/{templateId} | Update a setting template

# **add_setting_template**
> InlineResponse20122 add_setting_template(body=body)

Add a setting template

Creates a Zoom Phone setting template for an account. After creating a phone template, the defined settings will become the default settings for an account.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or enterprise Zoom account  * A Zoom Phone license

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
api_instance = swagger_client.SettingTemplatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneSettingTemplatesBody() # PhoneSettingTemplatesBody |  (optional)

try:
    # Add a setting template
    api_response = api_instance.add_setting_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingTemplatesApi->add_setting_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneSettingTemplatesBody**](PhoneSettingTemplatesBody.md)|  | [optional] 

### Return type

[**InlineResponse20122**](InlineResponse20122.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_setting_template**
> InlineResponse20061 get_setting_template(template_id, custom_query_fields=custom_query_fields)

Get setting template details

Returns information about an account's phone template.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.SettingTemplatesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | The unique identifier of the template.
custom_query_fields = 'custom_query_fields_example' # str | This field provides the name of the field to use to filter the response. For example, if you provide \"description\" as the value of the field, you will get a response similar to the following: {“description”: “template description”}. (optional)

try:
    # Get setting template details
    api_response = api_instance.get_setting_template(template_id, custom_query_fields=custom_query_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingTemplatesApi->get_setting_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The unique identifier of the template. | 
 **custom_query_fields** | **str**| This field provides the name of the field to use to filter the response. For example, if you provide \&quot;description\&quot; as the value of the field, you will get a response similar to the following: {“description”: “template description”}. | [optional] 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_setting_templates**
> InlineResponse20060 list_setting_templates(page_size=page_size, next_page_token=next_page_token, site_id=site_id)

List setting templates

Gets a list of all the created phone template settings.  **Scopes:** `phone:read:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.SettingTemplatesApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | Number of records returns within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
site_id = 'site_id_example' # str | Unique identifier of the site. This field is required only if multiple sites have been enabled.  of the site. Required only when multiple sites are enabled. See [Managing multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for details. If this is not provided, the response lists the account level setting templates. (optional)

try:
    # List setting templates
    api_response = api_instance.list_setting_templates(page_size=page_size, next_page_token=next_page_token, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingTemplatesApi->list_setting_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of records returns within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **site_id** | **str**| Unique identifier of the site. This field is required only if multiple sites have been enabled.  of the site. Required only when multiple sites are enabled. See [Managing multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) for details. If this is not provided, the response lists the account level setting templates. | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setting_template**
> object update_setting_template(template_id, body=body)

Update a setting template

Updates or modifies a phone template's settings.  **Scopes:** `phone:write:admin` **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`  **Prerequisites:**  * A Business or Enterprise account  * A Zoom Phone license

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
api_instance = swagger_client.SettingTemplatesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | The Template ID.
body = swagger_client.SettingTemplatesTemplateIdBody() # SettingTemplatesTemplateIdBody |  (optional)

try:
    # Update a setting template
    api_response = api_instance.update_setting_template(template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingTemplatesApi->update_setting_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The Template ID. | 
 **body** | [**SettingTemplatesTemplateIdBody**](SettingTemplatesTemplateIdBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

