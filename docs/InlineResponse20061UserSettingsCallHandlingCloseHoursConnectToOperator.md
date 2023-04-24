# InlineResponse20061UserSettingsCallHandlingCloseHoursConnectToOperator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**id** | **str** | The phone extension ID of the user, zoomRoom, commonAreaPhone, autoReceptionist, callQueue, or sharedLineGroup. | [optional] 
**type** | **str** | Values:  1-user,  2-callQueue,   3-autoReceptionist,  4-commonAreaPhone,  5-zoomRoom,   7-sharedLineGroup | [optional] 
**external_number** | [**InlineResponse20061UserSettingsCallHandlingCloseHoursConnectToOperatorExternalNumber**](InlineResponse20061UserSettingsCallHandlingCloseHoursConnectToOperatorExternalNumber.md) |  | [optional] 
**play_callee_voicemail_greeting** | **bool** | Whether to play the callee&#x27;s voicemail greeting when the caller reaches the end of forwarding sequence. Make available only when the &#x60;close_hour_action&#x60; is &#x60;0&#x60; or &#x60;50&#x60;. | [optional] 
**require_press_1_before_connecting** | **bool** | Whether to require pressing 1 before connecting the call. Make available only when the &#x60;close_hour_action&#x60; is &#x60;11&#x60; or &#x27;26&#x27;. | [optional] 
**allow_caller_check_voicemail** | **bool** | Whether to allow callers to check their voicemail. Make available only when the &#x60;close_hour_action&#x60; is &#x60;0&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

