# PhonesitessiteIdPolicyBlockExternalCalls

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**reset** | **bool** | Whether the current settings will use the phone account&#x27;s settings (compatible with the old or new policy frameworks). | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**block_business_hours** | **bool** |  | [optional] 
**block_closed_hours** | **bool** |  | [optional] 
**block_holiday_hours** | **bool** |  | [optional] 
**block_call_action** | **int** | The action when a call is blocked. 9-Disconnect, 0-Forward to voicemail/videomail. | [optional] 
**block_call_change_type** | **int** | Used only in the old policy framework. Apply changes to a new extensions or all extensions. &#x60;1&#x60; - All extension, &#x60;0&#x60; - New extensions. | [optional] 
**e2e_encryption** | [**PhonesitessiteIdPolicyBlockExternalCallsE2eEncryption**](PhonesitessiteIdPolicyBlockExternalCallsE2eEncryption.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

