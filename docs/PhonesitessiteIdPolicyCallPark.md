# PhonesitessiteIdPolicyCallPark

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_not_picked_up_action** | **int** | The action when a parked call is not picked up.   &#x60;100&#x60; - Ring back to parker  &#x60;0&#x60; - Forward to voicemail of the parker  &#x60;9&#x60; - Disconnect   &#x60;50&#x60; - Forward to another extension | [optional] 
**enable** | **bool** | Whether to allow calls placed on hold to be resumed from another location using a retrieval code. | [optional] 
**reset** | **bool** | Whether the current settings will use the phone account&#x27;s settings (applicable if the current settings are using the new policy framework). | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**expiration_period** | **int** | A time limit for parked calls in minutes. After the expiration period ends, the retrieval code is no longer valid and a new code will be generated. | [optional] 
**forward_to_extension_id** | **str** | The extension&#x27;s forwarding information when &#x60;call_not_picked_up_action&#x60; uses the &#x60;50&#x60; - Forward to another extension. | [optional] 
**sequence** | **int** | Only used in the new policy framework. Choose how parked calls are assigned to a BLF (Busy Lamp Field) key. Sequential assignment will park the call at the next available BLF key. Random assignment will park the call at a randomly selected BLF key.  &#x60;0&#x60; - Random  &#x60;1&#x60; - Sequential | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

