# InlineResponse20044AutoCallRecording

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits the modification of the current settings. | [optional] 
**recording_calls** | **str** | The type of calls automatically recorded:  * &#x60;inbound&#x60;  * &#x60;outbound&#x60;  * &#x60;both&#x60; | [optional] 
**recording_transcription** | **bool** | Whether the call recording transcription is enabled. | [optional] 
**recording_start_prompt** | **bool** | Whether a prompt plays to call participants when the recording has started. | [optional] 
**recording_start_prompt_audio_id** | **str** | The audio that plays when the recording has started. You can use this audio ID to get the audio information using [Get an audio item](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Audio-Library/operation/GetAudioItem) API. | [optional] 
**recording_explicit_consent** | **bool** | Whether the &#x60;Press 1 option that provides recording consent&#x60; is enabled. | [optional] 
**allow_stop_resume_recording** | **bool** | Whether the stop and resume of automatic call recording is enabled. | [optional] 
**disconnect_on_recording_failure** | **bool** | Whether a call disconnects when there is an issue with the automatic call recording and the call cannot reconnect after five seconds. This does **not** include emergency calls. | [optional] 
**play_recording_beep_tone** | [**InlineResponse20044AutoCallRecordingPlayRecordingBeepTone**](InlineResponse20044AutoCallRecordingPlayRecordingBeepTone.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

