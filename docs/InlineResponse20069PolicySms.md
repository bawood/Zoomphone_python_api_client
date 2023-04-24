# InlineResponse20069PolicySms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to allow users, call queues, and auto receptionists to send and receive messages. You will still need to assign a valid calling plan and phone number to each user for them to send and receive messages. | [optional] 
**international_sms** | **bool** | Whether the user can send and receive international messages. | [optional] 
**international_sms_countries** | **list[str]** | The country to which users can send and receive international messages. The [country ISO code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries). | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits modifying the current settings. | [optional] 
**modified** | **bool** | Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

