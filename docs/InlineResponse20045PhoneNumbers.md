# InlineResponse20045PhoneNumbers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**InlineResponse20045Assignee**](InlineResponse20045Assignee.md) |  | [optional] 
**capability** | **list[str]** | The capability for the phone number, whether it can take incoming calls, make outgoing calls, or both. Values include &#x60;incoming&#x60;, &#x60;outgoing&#x60;, or both of these values. | [optional] 
**carrier** | [**InlineResponse20045Carrier**](InlineResponse20045Carrier.md) |  | [optional] 
**display_name** | **str** | The display name for the phone number. | [optional] 
**emergency_address** | [**InlineResponse20045EmergencyAddress**](InlineResponse20045EmergencyAddress.md) |  | [optional] 
**emergency_address_status** | **int** | Displayed when the &#x60;type&#x60; request parameter is &#x60;byoc&#x60;. The emergency address status: &#x60;1&#x60;-carrier update required, &#x60;2&#x60;-confirmed | [optional] 
**emergency_address_update_time** | **str** | Displayed when the &#x60;type&#x60; request parameter is &#x60;byoc&#x60;. The time of emergency address info update (format: &#x27;yyyy-MM-ddThh:dd:ssZ&#x27;). | [optional] 
**id** | **str** | Unique Identifier of the Phone Number. | [optional] 
**location** | **str** | Location (city, state and country) where the Phone number is assigned. | [optional] 
**number** | **str** | Phone number in E164 format. | [optional] 
**number_type** | **str** | The type of number. Values can be one of the following:&lt;br&gt; &#x60;toll&#x60;, &#x60;tollfree&#x60; | [optional] 
**sip_group** | [**InlineResponse20045SipGroup**](InlineResponse20045SipGroup.md) |  | [optional] 
**site** | [**InlineResponse2007Site**](InlineResponse2007Site.md) |  | [optional] 
**source** | **str** | Source of phone number. | [optional] 
**status** | **str** | Status of the number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

