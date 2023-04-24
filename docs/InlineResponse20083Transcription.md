# InlineResponse20083Transcription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The content of the voicemail transcript | [optional] 
**status** | **int** | The status of the voicemail transcript: * &#x60;0&#x60; — Transcript is not available. * &#x60;1&#x60; — Transcript is processing. * &#x60;2&#x60; — Transcript processed successfully. * &#x60;4&#x60; — Transcript is disabled. * &#x60;5&#x60; — Transcript is enabled. * &#x60;9&#x60; — Transcript web error. * &#x60;11&#x60; — Transcript download error. * &#x60;12&#x60; — Transcript upload error. * &#x60;13&#x60; — Transcript web database error. * &#x60;14&#x60; — Transcript BYOS (Bring Your Own Storage) upload error. * &#x60;409&#x60; — Transcript duplicate processing request error. * &#x60;415&#x60; — Transcript unsupported media error. * &#x60;422&#x60; — Transcript cannot be processed. * &#x60;500&#x60; — Transcript server error. * &#x60;601&#x60; — Transcript AISense after retry error. * &#x60;602&#x60; — Transcript AISense upload file error. * &#x60;603&#x60; — Transcript AISense download file error. * &#x60;999&#x60; — Transcript AISense error.  | [optional] 
**engine** | **str** | This field indicates the company that provides the transcription engine technology. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

