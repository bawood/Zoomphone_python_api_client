# InlineResponse20036CallLogs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | The unique identifier of the phone call. | [optional] 
**callee** | [**InlineResponse20036Callee**](InlineResponse20036Callee.md) |  | [optional] 
**caller** | [**InlineResponse20036Caller**](InlineResponse20036Caller.md) |  | [optional] 
**date_time** | **str** | The date and time when the call started. | [optional] 
**direction** | **str** | The direction of the call. The value of this field can be either &#x60;internal&#x60; or &#x60;outbound&#x60;. | [optional] 
**duration** | **int** | The duration of the call in seconds. | [optional] 
**mos** | **str** | The  Mean Opinion Score (MOS). Zoom uses MOS as the main measurement to report on voice quality. MOS measures voice quality on a scale of one to five. A score of 1 indicates unacceptable voice quality for all users. A score of five is the best voice quality. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

