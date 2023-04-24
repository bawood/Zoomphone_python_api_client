# InlineResponse20069PolicyCallPark

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_not_picked_up_action** | **int** | The action when a parked call is not picked up.   &#x60;100&#x60; - Ring back to parker  &#x60;0&#x60; - Forward to voicemail of the parker  &#x60;9&#x60; - Disconnect   &#x60;50&#x60; - Forward to another extension | [optional] 
**enable** | **bool** | Whether to allow calls placed on hold to be resumed from another location using a retrieval code. | [optional] 
**expiration_period** | **int** | A time limit for parked calls in minutes. After the expiration period ends, the retrieval code is no longer valid and a new code will be generated. | [optional] 
**forward_to** | [**InlineResponse20069PolicyCallParkForwardTo**](InlineResponse20069PolicyCallParkForwardTo.md) |  | [optional] 
**sequence** | **int** | Only used in the new policy framework. Choose how parked calls are assigned to a BLF (Busy Lamp Field) key. Sequential assignment will park the call at the next available BLF key. Random assignment will park the call at a randomly selected BLF key.  &#x60;0&#x60; - Random  &#x60;1&#x60; - Sequential | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits modifying the current settings. | [optional] 
**modified** | **bool** | Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

