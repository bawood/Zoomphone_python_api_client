# InlineResponse20075SmsHistories

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**list[InlineResponse20075Attachments]**](InlineResponse20075Attachments.md) |  | [optional] 
**date_time** | **str** | The UTC time the message was created. | [optional] 
**direction** | **str** | &#x60;In&#x60;(SMS received) or &#x60;Out&#x60;(SMS sent) | [optional] 
**message** | **str** | The content of the SMS. | [optional] 
**message_id** | **str** | The message ID. | [optional] 
**message_type** | **int** | The message type:&lt;br&gt; 1 - SMS&lt;br&gt; 2 - MMS&lt;br&gt; 3 - GROUP_SMS&lt;br&gt; 4 - GROUP_MMS&lt;br&gt; 5 - SMS_INTER&lt;br&gt; 6 - MSG_ON_NET | [optional] 
**sender** | [**InlineResponse20074Sender**](InlineResponse20074Sender.md) |  | [optional] 
**to_members** | [**list[InlineResponse20075ToMembers]**](InlineResponse20075ToMembers.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

