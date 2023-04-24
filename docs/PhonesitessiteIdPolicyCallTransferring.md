# PhonesitessiteIdPolicyCallTransferring

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_transferring_type** | **int** | 1-No restriction. 2-Medium restriction (external numbers and external contacts not allowed). 3-High restriction (external numbers, unrecorded external contacts, and internal extensions without inbound automatic recording not allowed). 4-Low restriction (external numbers not allowed). | [optional] 
**enable** | **bool** | Whether to allow users to warm or blind transfer their calls. This does not apply to warm transfer on IP Phones except for Yealink. | [optional] 
**reset** | **bool** | Whether the current settings will use the phone account&#x27;s settings (applicable if the current settings are using the new policy framework). | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

