# InlineResponse20061UserSettingsCallHandlingCloseHoursBusyConnectOperator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**id** | **str** | The phone extension ID of the user, zoomRoom, commonArea, autoReceptionist, callQueue, or sharedLineGroup. | [optional] 
**type** | **str** | The Values:&lt;br&gt; 1-user,&lt;br&gt; 2-callQueue, &lt;br&gt; 3-autoReceptionist,&lt;br&gt; 4-commonArea,&lt;br&gt; 5-zoomRoom, &lt;br&gt; 7-sharedLineGroup. | [optional] 
**external_number** | [**PhonesettingTemplatestemplateIdUserSettingsCallHandlingCloseHoursBusyConnectOperatorExternalNumber**](PhonesettingTemplatestemplateIdUserSettingsCallHandlingCloseHoursBusyConnectOperatorExternalNumber.md) |  | [optional] 
**play_callee_voicemail_greeting** | **bool** | Whether to play the callee&#x27;s voicemail greeting when the caller reaches the end of forwarding sequence. Make available only when the &#x60;busy_action&#x60; is &#x60;0&#x60; or &#x60;50&#x60;. | [optional] 
**require_press_1_before_connecting** | **bool** | Whether to require pressing one before connecting the call. Make available only when the &#x60;busy_action&#x60; is &#x60;11&#x60; or &#x27;26&#x27;. | [optional] 
**allow_caller_check_voicemail** | **bool** | Whether to allow callers to check their voicemail. Make available only when the &#x60;busy_action&#x60; is &#x60;0&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

