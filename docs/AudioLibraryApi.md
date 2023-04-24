# swagger_client.AudioLibraryApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_an_audio**](AudioLibraryApi.md#add_an_audio) | **POST** /phone/users/{userId}/audios | Add an audio item for text-to-speech conversion
[**add_audio_item**](AudioLibraryApi.md#add_audio_item) | **POST** /phone/users/{userId}/audios/batch | Add audio items
[**delete_audio_item**](AudioLibraryApi.md#delete_audio_item) | **DELETE** /phone/audios/{audioId} | Delete an audio item
[**get_audio_item**](AudioLibraryApi.md#get_audio_item) | **GET** /phone/audios/{audioId} | Get an audio item
[**list_audio_items**](AudioLibraryApi.md#list_audio_items) | **GET** /phone/users/{userId}/audios | List audio items
[**update_audio_item**](AudioLibraryApi.md#update_audio_item) | **PATCH** /phone/audios/{audioId} | Update an audio item

# **add_an_audio**
> InlineResponse20126 add_an_audio(user_id, body=body)

Add an audio item for text-to-speech conversion

Adds an audio item for [text-to-speech conversion](https://support.zoom.us/hc/en-us/articles/4402414203533-Using-the-audio-library-to-customize-audio#h_01F8B0D2ZJBKEDH10DFZ7J2CM7).  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:write`,`phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light` 

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
api_instance = swagger_client.AudioLibraryApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = swagger_client.UserIdAudiosBody() # UserIdAudiosBody |  (optional)

try:
    # Add an audio item for text-to-speech conversion
    api_response = api_instance.add_an_audio(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioLibraryApi->add_an_audio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**UserIdAudiosBody**](UserIdAudiosBody.md)|  | [optional] 

### Return type

[**InlineResponse20126**](InlineResponse20126.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_audio_item**
> InlineResponse20080 add_audio_item(user_id, body=body)

Add audio items

Adds audio items. You can only upload voice files at this time.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:write`,`phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Heavy`   **Size and quantity limits for audio attachments:** * Up to 5 attachments * Each file size should be no more than 1MB

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
api_instance = swagger_client.AudioLibraryApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = swagger_client.AudiosBatchBody() # AudiosBatchBody |  (optional)

try:
    # Add audio items
    api_response = api_instance.add_audio_item(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioLibraryApi->add_audio_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**AudiosBatchBody**](AudiosBatchBody.md)|  | [optional] 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audio_item**
> delete_audio_item(audio_id)

Delete an audio item

Deletes an audio item.  **Prerequisites:** * Business, or Education account * Zoom Phone license   **Scopes:** `phone:write`,`phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AudioLibraryApi(swagger_client.ApiClient(configuration))
audio_id = 'audio_id_example' # str | Unique identifier of the audio item.

try:
    # Delete an audio item
    api_instance.delete_audio_item(audio_id)
except ApiException as e:
    print("Exception when calling AudioLibraryApi->delete_audio_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_id** | **str**| Unique identifier of the audio item. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_item**
> InlineResponse200 get_audio_item(audio_id)

Get an audio item

Gets an audio item.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:read`,`phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AudioLibraryApi(swagger_client.ApiClient(configuration))
audio_id = 'audio_id_example' # str | Unique identifier of the audio item.

try:
    # Get an audio item
    api_response = api_instance.get_audio_item(audio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioLibraryApi->get_audio_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_id** | **str**| Unique identifier of the audio item. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audio_items**
> InlineResponse20080 list_audio_items(user_id)

List audio items

Gets the audio items.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:read`,`phone:read:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AudioLibraryApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # List audio items
    api_response = api_instance.list_audio_items(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioLibraryApi->list_audio_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audio_item**
> update_audio_item(audio_id, body=body)

Update an audio item

Updates an audio item.  **Prerequisites:** * Business or Education account * Zoom Phone license   **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Light`

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
api_instance = swagger_client.AudioLibraryApi(swagger_client.ApiClient(configuration))
audio_id = 'audio_id_example' # str | Unique identifier of the audio item.
body = swagger_client.AudiosAudioIdBody() # AudiosAudioIdBody |  (optional)

try:
    # Update an audio item
    api_instance.update_audio_item(audio_id, body=body)
except ApiException as e:
    print("Exception when calling AudioLibraryApi->update_audio_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_id** | **str**| Unique identifier of the audio item. | 
 **body** | [**AudiosAudioIdBody**](AudiosAudioIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

