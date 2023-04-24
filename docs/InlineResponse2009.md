# InlineResponse2009

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | The phone call&#x27;s unique ID. | [optional] 
**call_log_id** | **str** | The phone call log&#x27;s unique ID. | [optional] 
**callee_name** | **str** | The callee&#x27;s contact name. | [optional] 
**callee_number** | **str** | The callee&#x27;s phone number. | [optional] 
**callee_number_type** | **int** | The callee&#x27;s number type:  * &#x60;1&#x60; — Internal number.  * &#x60;2&#x60; — External number. * &#x60;3&#x60; — Customized emergency number. | [optional] 
**caller_name** | **str** | The caller&#x27;s contact name. | [optional] 
**caller_number** | **str** | The caller&#x27;s phone number. | [optional] 
**caller_number_type** | **int** | The caller&#x27;s number type:  * &#x60;1&#x60; — Internal number.  * &#x60;2&#x60; — External number. | [optional] 
**outgoing_by** | [**InlineResponse2009OutgoingBy**](InlineResponse2009OutgoingBy.md) |  | [optional] 
**accepted_by** | [**InlineResponse2009AcceptedBy**](InlineResponse2009AcceptedBy.md) |  | [optional] 
**date_time** | **datetime** | The date and time at which the recording was received. | [optional] 
**direction** | **str** | The call&#x27;s direction: * &#x60;inbound&#x60; * &#x60;outbound&#x60; | [optional] 
**download_url** | **str** | The URL from which to download the recording. For security purposes, you **must** provide an OAuth access token in the Authorizatoin header to download the recording file using this URL. For example:  &#x60;&#x60;&#x60;curl --request GET \\   --url {download_url} \\   --header &#x27;authorization: Bearer {access_token} \\   --header &#x27;content-type: application/json&#x27; &#x60;&#x60;&#x60; | [optional] 
**duration** | **int** | The call recording&#x27;s duration, in seconds. | [optional] 
**end_time** | **datetime** | The recording&#x27;s end time. | [optional] 
**id** | **str** | The recording&#x27;s ID. | [optional] 
**owner** | [**InlineResponse2009Owner**](InlineResponse2009Owner.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

