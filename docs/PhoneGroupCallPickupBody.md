# PhoneGroupCallPickupBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Name of the group. | 
**site_id** | **str** | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites). | 
**description** | **str** | Group call pickup description. | [optional] 
**extension_number** | **int** | Short extension number. | [optional] 
**delay** | **int** | Determines after how much time (in seconds) the group should be notified. | [optional] [default to DelayEnum._0]
**play_incoming_calls_sound** | [**PhonegroupCallPickupPlayIncomingCallsSound**](PhonegroupCallPickupPlayIncomingCallsSound.md) |  | [optional] 
**directed_call_pickup** | **bool** | Whether the ringtone is on. | [optional] [default to False]
**member_extension_ids** | **list[str]** | Extension ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

