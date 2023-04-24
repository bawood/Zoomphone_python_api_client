# InlineResponse20065

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the shared line group. | [optional] 
**extension_number** | **int** | The extension number assigned to the shared line group. | [optional] 
**id** | **str** | The unique identifier of the shared line group. | [optional] 
**members** | [**InlineResponse20065Members**](InlineResponse20065Members.md) |  | [optional] 
**phone_numbers** | [**list[InlineResponse20065PhoneNumbers]**](InlineResponse20065PhoneNumbers.md) | Object representing information about phone number(s) assigned to the group. | [optional] 
**primary_number** | **str** | If you have multiple direct phone numbers assigned to the shared line group, this is the primary number selected for desk phones. The primary number shares the same line as the extension number. This means if a caller is routed to the shared line group through an auto receptionist, the line associated with the primary number will be used. | [optional] 
**site** | [**InlineResponse20065Site**](InlineResponse20065Site.md) |  | [optional] 
**status** | **str** | The status of the shared line group. | [optional] 
**timezone** | **str** | The timezone used for the business hours. | [optional] 
**policy** | [**InlineResponse20065Policy**](InlineResponse20065Policy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

