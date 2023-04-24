# PhoneusersuserIdPolicyCallOverflow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_overflow_type** | **int** | &#x60;1&#x60; - Low restriction (external numbers not allowed) &#x60;2&#x60; - Medium restriction (external numbers and external contacts not allowed)  &#x60;3&#x60; - High restriction (external numbers, external contacts and internal extensions without inbound automatic call recording not allowed) &#x60;4&#x60; - No restriction | [optional] 
**enable** | **bool** | Whether to allow user to forward calls to other numbers. | [optional] 
**reset** | **bool** | Whether the current settings will use the phone site&#x27;s settings (applicable if the current settings are using the new policy framework). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

