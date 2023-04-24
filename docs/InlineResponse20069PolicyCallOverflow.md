# InlineResponse20069PolicyCallOverflow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_overflow_type** | **int** | &#x60;1&#x60; - Can forward to internal extensions and to external contacts. &#x60;2&#x60; - Can forward only to internal extensions. &#x60;3&#x60; - Can forward only to internal extensions that require inbound Automatic Call Recording. &#x60;4&#x60; - Can forward to internal extensions, external contacts, and external numbers. | [optional] 
**enable** | **bool** | Whether to allow users to forward their calls to other numbers. | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits modifying the current settings. | [optional] 
**modified** | **bool** | Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

