# InlineResponse20093

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | The phone call&#x27;s unique ID. | [optional] 
**call_log_id** | **str** | The phone call log&#x27;s unique ID. | [optional] 
**callee_name** | **str** | The name of the callee. | [optional] 
**callee_number** | **str** | The number associated with the callee. Could be a phone number or an extension. Check the number type to differentiate the two. | [optional] 
**callee_number_type** | **int** | The callee&#x27;s number type:  * &#x60;1&#x60; — Internal number.  * &#x60;2&#x60; — External number. * &#x60;3&#x60; — Customized emergency number. | [optional] 
**caller_name** | **str** | The name of the caller. | [optional] 
**caller_number** | **str** | The number associated with the caller. Could be a phone number or an extension. Check the number type to differentiate the two.  | [optional] 
**caller_number_type** | **int** | The caller&#x27;s number type:  * &#x60;1&#x60; — Internal number.  * &#x60;2&#x60; — External number. | [optional] 
**date_time** | **str** | The date the voicemail was created. | [optional] 
**download_url** | **str** | The URL to download the voicemail. | [optional] 
**duration** | **int** | The duration of voicemail in seconds. | [optional] 
**id** | **str** | The voicemail ID. | [optional] 
**status** | **str** | The status of the voicemail. It can be either &#x27;read&#x27; or &#x27;unread&#x27; | [optional] 
**transcription** | [**InlineResponse20093Transcription**](InlineResponse20093Transcription.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

