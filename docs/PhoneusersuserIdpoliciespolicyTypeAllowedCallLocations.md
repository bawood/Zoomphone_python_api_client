# PhoneusersuserIdpoliciespolicyTypeAllowedCallLocations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to define where the extension or user can make and accept calls and send SMS. When the extension or user is outside of the allowed locations, calls will follow \&quot;When a call is not answered\&quot; settings, meanwhile outbound and inbound emergency calls and SMS will still be allowed. Note: SMS settings will only be available to users. | [optional] 
**reset** | **bool** | Whether the user&#x27;s automatic call recording reset option will use the phone site&#x27;s settings. | [optional] 
**allow_internal_calls** | **bool** | Whether to allow internal calls/SMS when outside of allowed locations. | [optional] 
**allowed_locations** | [**PhonecommonAreascommonAreaIdpoliciespolicyTypeAllowedCallLocationsAllowedLocations**](PhonecommonAreascommonAreaIdpoliciespolicyTypeAllowedCallLocationsAllowedLocations.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

