# InlineResponse20078PolicyCallPark

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_not_picked_up_action** | **int** | The action when a parked call is not picked up. 100-Ring back to parker, 0-Forward to voicemail of the parker, 9-Disconnect, 50-Forward to another extension. | [optional] 
**enable** | **bool** | Whether to allow calls placed on hold to be resumed from another location using a retrieval code. | [optional] 
**expiration_period** | **int** | A time limit for parked calls, unit minutes. After the expiration period ends, the retrieval code is no longer valid and a new code will be generated. | [optional] 
**forward_to** | [**InlineResponse20078PolicyCallParkForwardTo**](InlineResponse20078PolicyCallParkForwardTo.md) |  | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits modifying the current settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

