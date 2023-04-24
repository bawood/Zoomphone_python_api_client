# InlineResponse20022RestrictedCallHours

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to define when the extension or user cannot make or accept calls and send SMS. In the restricted hours, calls will follow \&quot;When a call is not answered\&quot; settings. Outbound and inbound emergency calls will still be allowed. Note: SMS settings will only be available to users. | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits modifying the current settings. | [optional] 
**modified** | **bool** | Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework). | [optional] 
**time_zone** | [**InlineResponse20022RestrictedCallHoursTimeZone**](InlineResponse20022RestrictedCallHoursTimeZone.md) |  | [optional] 
**allow_internal_calls** | **bool** | Whether to allow internal calls/SMS during restricted hours. | [optional] 
**restricted_hours** | [**InlineResponse20022RestrictedCallHoursRestrictedHours**](InlineResponse20022RestrictedCallHoursRestrictedHours.md) |  | [optional] 
**restricted_holiday_hours** | [**InlineResponse20022RestrictedCallHoursRestrictedHolidayHours**](InlineResponse20022RestrictedCallHoursRestrictedHolidayHours.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

