# CallHandlingRoutingForwardTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The extension&#x27;s name. | [optional] 
**extension_id** | **str** | The extension ID. | [optional] 
**extension_number** | **int** | The extension number. | [optional] 
**extension_type** | **str** | The type of extension:  * &#x60;user&#x60;  * &#x60;autoReceptionist&#x60;   * &#x60;callQueue&#x60; | [optional] 
**id** | **str** | The ID of the extension &#x60;user&#x60;, &#x60;autoReceptionist&#x60;, &#x60;device&#x60;, or &#x60;callQueue&#x60;. | [optional] 
**phone_number** | **str** | The extension&#x27;s phone number or forward to an external number, in [E.164 format](https://en.wikipedia.org/wiki/E.164) format. | [optional] 
**description** | **str** | Forward to an external number description. | [optional] 
**voicemail_greeting** | **object** | The voicemail greeting prompt. It returns only when &#x60;call_not_answer_action&#x60; is set to &#x60;1&#x60; (Forward to a voicemail) for the &#x60;Call Queue&#x60; or &#x60;Auto Receptionist&#x60; &#x60;call_handling&#x60; sub-setting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

