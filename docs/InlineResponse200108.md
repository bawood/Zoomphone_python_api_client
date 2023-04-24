# InlineResponse200108

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The campaign ID. | [optional] 
**display_name** | **str** | The display name for the SMS campaign. | [optional] 
**status** | **str** | The status of the SMS campaign. Returns &#x60;--&#x60; if the campaign is in an exception status. | [optional] 
**service_type** | **str** | Which service the campaign is used for. | [optional] 
**brand** | [**InlineResponse200107Brand**](InlineResponse200107Brand.md) |  | [optional] 
**phone_numbers** | [**list[InlineResponse200108PhoneNumbers]**](InlineResponse200108PhoneNumbers.md) | Assigned phone numbers. | [optional] 
**auto_renew** | **bool** | Whether to keep the SMS capabilities for all phone numbers associated with this campaign. If &#x27;false&#x27;, the campaign will expire 90 days from the creation date. | [optional] 
**create_time** | **str** | The creation time of the campaign. | [optional] 
**use_case** | **str** | What will you be using these campaigns for. | [optional] 
**categories_fit** | **bool** | Whether *all* customer-facing messages fit into the categories &#x60;Account Notifications&#x60;, &#x60;Customer Care&#x60;, &#x60;Delivery Notifications&#x60;, &#x60;Marketing&#x60;, and &#x60;Public Service Announcements&#x60;. | [optional] 
**content_type** | **list[str]** | The message&#x27;s content type. | [optional] 
**sample_message_1** | **str** | The sample message 1. | [optional] 
**sample_message_2** | **str** | The sample message 2. | [optional] 
**sample_message_3** | **str** | The sample message 3. | [optional] 
**sample_message_4** | **str** | The sample message 4. | [optional] 
**sample_message_5** | **str** | The sample message 5. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

