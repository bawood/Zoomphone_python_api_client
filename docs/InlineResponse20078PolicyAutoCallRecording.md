# InlineResponse20078PolicyAutoCallRecording

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_stop_resume_recording** | **bool** | Whether the stop of and resuming of automatic call recording is enabled. | [optional] 
**disconnect_on_recording_failure** | **bool** | Whether a call disconnects when there is an issue with automatic call recording and the call cannot reconnect after five seconds. This does **not** include emergency calls. | [optional] 
**enable** | **bool** | Whether automatic call recording is enabled. | [optional] 
**locked** | **bool** | Whether the senior administrator allow users to modify the current settings. | [optional] 
**locked_by** | **str** | This field specifies which level of administrator prohibits modifying the current settings. | [optional] 
**recording_calls** | **str** | The type of calls automatically recorded:  * &#x60;inbound&#x60;  * &#x60;outbound&#x60;  * &#x60;both&#x60; | [optional] 
**recording_explicit_consent** | **bool** | Whether press 1 to provide recording consent is enabled. | [optional] 
**recording_start_prompt** | **bool** | Whether a prompt plays to call participants when the recording has started. | [optional] 
**recording_transcription** | **bool** | Whether call recording transcription is enabled. | [optional] 
**play_recording_beep_tone** | [**InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone**](InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

