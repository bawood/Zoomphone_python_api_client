# PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHours

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to define where the extension or user can make and accept calls and send SMS. When the extension or user is outside of the allowed locations, calls will follow \&quot;When a call is not answered\&quot; settings, meanwhile outbound and inbound emergency calls and SMS will still be allowed. Note: SMS settings will only be available to users. | [optional] 
**reset** | **bool** | If reset, the current settings will reset to the default setting. | [optional] 
**time_zone** | [**PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursTimeZone**](PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursTimeZone.md) |  | [optional] 
**allow_internal_calls** | **bool** | Whether to allow internal calls/SMS during restricted hours. | [optional] 
**restricted_hours** | [**PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursRestrictedHours**](PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursRestrictedHours.md) |  | [optional] 
**restricted_holiday_hours** | [**PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursRestrictedHolidayHours**](PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursRestrictedHolidayHours.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

