# InlineResponse20069PolicyBlockExternalCalls

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits modifying the current settings. | [optional] 
**modified** | **bool** | Whether the current settings have been modified. If modified, they can be reset(displayed when using old or new policy framework). | [optional] 
**block_business_hours** | **bool** |  | [optional] 
**block_closed_hours** | **bool** |  | [optional] 
**block_holiday_hours** | **bool** |  | [optional] 
**block_call_action** | **int** | The action when a call is blocked. &#x60;9&#x60; - Disconnect, &#x60;0&#x60;- Forward to voicemail/videomail. | [optional] 
**block_call_change_type** | **int** | Used only in the old policy framework. Apply changes to a new extensions or all extensions. &#x60;1&#x60; - All extension, &#x60;0&#x60; - New extensions. | [optional] 
**e2e_encryption** | [**PhonesitessiteIdPolicyBlockExternalCallsE2eEncryption**](PhonesitessiteIdPolicyBlockExternalCallsE2eEncryption.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

