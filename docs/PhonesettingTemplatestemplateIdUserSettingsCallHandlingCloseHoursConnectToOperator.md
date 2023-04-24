# PhonesettingTemplatestemplateIdUserSettingsCallHandlingCloseHoursConnectToOperator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to enable connect to the operator, and you must input the &#x60;id&#x60; if you want to enable. Available only when the &#x60;close_hour_action&#x60; is &#x60;0&#x60;. | [optional] 
**id** | **str** | The extension ID of user, zoomRoom, commonAreaPhone, autoReceptionist, callQueue, or sharedLineGroup. It&#x27;s available only when the &#x60;close_hour_action&#x60; is &#x60;0&#x60; or &#x60;50&#x60; | [optional] 
**external_number** | [**PhonesettingTemplatestemplateIdUserSettingsCallHandlingCloseHoursConnectToOperatorExternalNumber**](PhonesettingTemplatestemplateIdUserSettingsCallHandlingCloseHoursConnectToOperatorExternalNumber.md) |  | [optional] 
**play_callee_voicemail_greeting** | **bool** | Whether to play the callee&#x27;s voicemail greeting when the caller reaches the end of forwarding sequence. Make available only when the &#x60;close_hour_action&#x60; is &#x60;0&#x60; or &#x60;50&#x60;. | [optional] 
**require_press_1_before_connecting** | **bool** | Whether to require pressing 1 before connecting the call. Make available only when the &#x60;close_hour_action&#x60; is &#x60;11&#x60; or &#x27;26&#x27;. | [optional] 
**allow_caller_check_voicemail** | **bool** | Whether to allow callers to check their voicemail. Make available only when the &#x60;close_hour_action&#x60; is &#x60;0&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

