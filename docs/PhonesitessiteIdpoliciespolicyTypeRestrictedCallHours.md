# PhonesitessiteIdpoliciespolicyTypeRestrictedCallHours

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to define when the user cannot make or accept calls and send SMS. In the restricted hours, calls will follow \&quot;When a call is not answered\&quot; settings. Outbound and inbound emergency calls will still be allowed. | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**reset** | **bool** | Whether the current settings will use the phone account&#x27;s settings (applicable if the current settings are using the new policy framework). | [optional] 
**time_zone** | [**PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursTimeZone**](PhonecommonAreascommonAreaIdpoliciespolicyTypeRestrictedCallHoursTimeZone.md) |  | [optional] 
**allow_internal_calls** | **bool** | Whether to allow internal calls/SMS during restricted hours. | [optional] 
**restricted_hours** | [**PhonesitessiteIdpoliciespolicyTypeRestrictedCallHoursRestrictedHours**](PhonesitessiteIdpoliciespolicyTypeRestrictedCallHoursRestrictedHours.md) |  | [optional] 
**restricted_holiday_hours** | [**PhonesitessiteIdpoliciespolicyTypeRestrictedCallHoursRestrictedHolidayHours**](PhonesitessiteIdpoliciespolicyTypeRestrictedCallHoursRestrictedHolidayHours.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

