# InlineResponse20069PolicyAutoCallRecording

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_stop_resume_recording** | **bool** | Whether the stop and resume of automatic call recording is enabled. | [optional] 
**disconnect_on_recording_failure** | **bool** | Whether a call disconnects when there is an issue with the automatic call recording and the call cannot reconnect after five seconds. This does **not** include emergency calls. | [optional] 
**enable** | **bool** | Whether automatic call recording is enabled. | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits the modification of the current settings. | [optional] 
**modified** | **bool** | Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework). | [optional] 
**recording_calls** | **str** | The type of calls automatically recorded:  * &#x60;inbound&#x60;  * &#x60;outbound&#x60;  * &#x60;both&#x60; | [optional] 
**recording_explicit_consent** | **bool** | Whether the &#x60;Press 1 option that provides recording consent&#x60; is enabled. | [optional] 
**recording_start_prompt** | **bool** | Whether a prompt plays to call participants when the recording has started. | [optional] 
**recording_transcription** | **bool** | Whether the call recording transcription is enabled. | [optional] 
**play_recording_beep_tone** | [**InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone**](InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

