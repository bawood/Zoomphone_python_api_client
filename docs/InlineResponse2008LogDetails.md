# InlineResponse2008LogDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time** | **str** | Start time of the call. | [optional] 
**hold_time** | **int** | Hold time during a call in seconds. | [optional] 
**device_private_ip** | **str** | Display the device&#x27;s private IP address if the account has the &#x60;show_device_ip_for_call_log&#x60; parameter set to &#x60;enabled&#x60;. | [optional] 
**device_public_ip** | **str** | Display the device&#x27;s public IP address if the account has the &#x60;show_device_ip_for_call_log&#x60; parameter set to &#x60;enabled&#x60;. | [optional] 
**duration** | **int** | Duration of the call in seconds. | [optional] 
**forward_to** | [**InlineResponse2008ForwardTo**](InlineResponse2008ForwardTo.md) |  | [optional] 
**id** | **str** | Call log ID. | [optional] 
**path** | **str** | Path of the call. | [optional] 
**result** | **str** | Result of the call: &#x60;Missed&#x60; | &#x60;Voicemail&#x60;| &#x60;Call connected&#x60;|&#x60;Rejected&#x60;| &#x60;Blocked&#x60;| &#x60;Busy&#x60;|&#x60;Wrong Number&#x60;| &#x60;No Answer&#x60;| &#x60;International Disabled&#x60;|&#x60;Internal Error&#x60;| &#x60;Call failed&#x60;| &#x60;Restricted Number&#x60;|&#x60;Call Cancel&#x60;| &#x60;Message&#x60;| &#x60;Answered by Other Member&#x60;|&#x60;Call Cancelled&#x60;| &#x60;Park&#x60;| &#x60;Parked&#x60;| &#x60;Blocked by non-GAL&#x60;| &#x60;Blocked by info-Barriers&#x60;|&#x60;Recording Failure&#x60;| &#x60;Recorded&#x60;| &#x60;Auto Recorded&#x60;. | [optional] 
**site** | [**InlineResponse2008Site**](InlineResponse2008Site.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

