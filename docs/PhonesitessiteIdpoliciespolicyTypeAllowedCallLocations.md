# PhonesitessiteIdpoliciespolicyTypeAllowedCallLocations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to define where the extension or user can make and accept calls and send SMS. When the extension or user is outside of the allowed locations, calls will follow \&quot;When a call is not answered\&quot; settings, meanwhile outbound and inbound emergency calls and SMS will still be allowed. Note: SMS settings will only be available to users. | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**reset** | **bool** | Whether the current settings will use the phone account&#x27;s settings (applicable if the current settings are using the new policy framework). | [optional] 
**allow_internal_calls** | **bool** | Whether to allow internal calls/SMS when outside of allowed locations. | [optional] 
**allowed_locations** | [**PhonecommonAreascommonAreaIdpoliciespolicyTypeAllowedCallLocationsAllowedLocations**](PhonecommonAreascommonAreaIdpoliciespolicyTypeAllowedCallLocationsAllowedLocations.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

