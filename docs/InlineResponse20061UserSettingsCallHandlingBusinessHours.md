# InlineResponse20061UserSettingsCallHandlingBusinessHours

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_hour_action** | **int** | When a call is not answered:&lt;br&gt; 0-Forward to a voicemail;&lt;br&gt; 1-Play a message, then disconnect; &lt;br&gt; 9-Disconnect; &lt;br&gt; 11-Forward to an external number; &lt;br&gt; 26-Forward to External Contacts; &lt;br&gt; 50-Forward to another extension | [optional] 
**connect_to_operator** | [**InlineResponse20061UserSettingsCallHandlingBusinessHoursConnectToOperator**](InlineResponse20061UserSettingsCallHandlingBusinessHoursConnectToOperator.md) |  | [optional] 
**busy_action** | **int** | When the user is busy on another call:&lt;br&gt; 0-Forward to a voicemail;&lt;br&gt; 1-Play a message, then disconnect; &lt;br&gt; 11-Forward to an external number; &lt;br&gt; 12-Call waiting; &lt;br&gt; 13-Play a busy signal; &lt;br&gt; 26-Forward to External Contacts; &lt;br&gt; 50-Forward to another extension. | [optional] 
**busy_connect_operator** | [**InlineResponse20061UserSettingsCallHandlingBusinessHoursBusyConnectOperator**](InlineResponse20061UserSettingsCallHandlingBusinessHoursBusyConnectOperator.md) |  | [optional] 
**custom_hours** | [**list[InlineResponse20061UserSettingsCallHandlingBusinessHoursCustomHours]**](InlineResponse20061UserSettingsCallHandlingBusinessHoursCustomHours.md) |  | [optional] 
**ring_type** | **str** | The call handling ring mode:&lt;br&gt; 0-Simultaneous,&lt;br&gt; 1-Sequential | [optional] 
**ringing_duration** | **str** | Ringing duration for each device in seconds. Values:&lt;br&gt; 10,15,20,25,30,35,40,45,50,55,60 | [optional] 
**type** | **int** | Values:  1-24 Hours, 7 Days a Week;  2-Custom Hours | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

