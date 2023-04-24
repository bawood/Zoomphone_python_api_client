# InlineResponse20069PolicyCallHandlingForwardingToOtherUsers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**call_forwarding_type** | **int** | &#x60;1&#x60; - Low restriction (external numbers not allowed) &#x60;2&#x60; - Medium restriction (external numbers and external contacts not allowed)  &#x60;3&#x60; - High restriction (external numbers, external contacts and internal extensions without inbound automatic call recording not allowed) &#x60;4&#x60; - No restriction | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits the modification of the current settings. | [optional] 
**modified** | **bool** | Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

