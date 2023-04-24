# PhonesitessiteIdPolicySms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to allow users, call queues and auto receptionists to send and receive messages. You will still need to assign a valid calling plan and phone number to each user in order for them to send and receive messages. | [optional] 
**reset** | **bool** | Whether the current settings will use the phone account&#x27;s settings (applicable if the current settings are using the new policy framework). | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**international_sms** | **bool** | Whether the user can send and receive international messages. | [optional] 
**international_sms_countries** | **list[str]** | The country which users can send and receive international messages. The [country ISO code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

