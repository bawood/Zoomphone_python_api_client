# InlineResponse20030SettingsCallDistribution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle_multiple_calls** | **bool** | The maximum number of calls that can be handled simultaneously is less than half of the total amount of available call queue members. Note that the first incoming call may not be answered first.  Returned only except &#x60;simultaneous&#x60; ring mode. | [optional] 
**ring_duration** | **int** | Ringing duration for each member: * &#x60;10&#x60;  * &#x60;15&#x60;  * &#x60;20&#x60;  * &#x60;25&#x60;  * &#x60;30&#x60;  * &#x60;35&#x60;  * &#x60;40&#x60;  * &#x60;45&#x60;  * &#x60;50&#x60;  * &#x60;55&#x60;  * &#x60;60&#x60;   Returned only except &#x60;simultaneous&#x60; ring mode. | [optional] 
**ring_mode** | **str** | The call distribution ring mode:  * &#x60;simultaneous&#x60;  * &#x60;sequential&#x60;  * &#x60;rotating&#x60;  * &#x60;longest_idle&#x60; | [optional] 
**skip_offline_device_phone_number** | **bool** | 1. Devices with Zoom app or client not launched and mobile phone with screen locked will be skipped.   2. Phone numbers added to user&#x27;s call handling settings will be skipped.  Returned only except &#x60;simultaneous&#x60; ring mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

