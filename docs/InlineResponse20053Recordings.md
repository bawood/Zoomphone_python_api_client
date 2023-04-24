# InlineResponse20053Recordings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | The phone call&#x27;s unique ID. | [optional] 
**call_log_id** | **str** | The phone call log&#x27;s unique ID. | [optional] 
**callee_name** | **str** | The contact name of the callee. | [optional] 
**callee_number** | **str** | The phone number of the callee. Could be an e164 number or an extension. Extension number is a combination of the site number and a short extension. | [optional] 
**callee_number_type** | **int** | The callee&#x27;s number type:  * &#x60;1&#x60; — Internal number.  * &#x60;2&#x60; — External number. * &#x60;3&#x60; — Customized emergency number. | [optional] 
**caller_name** | **str** | The contact name of the caller. | [optional] 
**caller_number** | **str** | The phone number associated with the caller. Could be an e164 number or an extension. Extension number is a combination of the site number and the short extension. | [optional] 
**caller_number_type** | **int** | The caller&#x27;s number type:  * &#x60;1&#x60; — Internal  number.  * &#x60;2&#x60; — External number. | [optional] 
**outgoing_by** | [**InlineResponse2009OutgoingBy**](InlineResponse2009OutgoingBy.md) |  | [optional] 
**accepted_by** | [**InlineResponse20053AcceptedBy**](InlineResponse20053AcceptedBy.md) |  | [optional] 
**date_time** | **datetime** | The date and time when the recording was received. | [optional] 
**direction** | **str** | The direction of the call. Values: &#x60;inbound&#x60; or &#x60;outbound&#x60;. | [optional] 
**download_url** | **str** | The download URL for the recording. | [optional] 
**duration** | **int** | The call recording&#x27;s duration, in seconds. | [optional] 
**end_time** | **datetime** | The recording&#x27;s end time. | [optional] 
**id** | **str** | The unique identifier of the recording. | [optional] 
**owner** | [**InlineResponse20053Owner**](InlineResponse20053Owner.md) |  | [optional] 
**recording_type** | **str** | The recording type. The allowed values are &#x60;OnDemand&#x60; or &#x60;Automatic&#x60;. | [optional] 
**site** | [**InlineResponse20053Site**](InlineResponse20053Site.md) |  | [optional] 
**transcript_download_url** | **str** | The download URL for the recording transcript. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

