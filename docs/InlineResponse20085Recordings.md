# InlineResponse20085Recordings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | The phone call&#x27;s unique ID. | [optional] 
**call_log_id** | **str** | The phone call log&#x27;s unique ID. | [optional] 
**callee_name** | **str** | The contact name of callee. | [optional] 
**callee_number** | **str** | The number of callee. | [optional] 
**callee_number_type** | **int** | The callee&#x27;s number type:  * &#x60;1&#x60; — Internal number.  * &#x60;2&#x60; — External number. * &#x60;3&#x60; — Customized emergency number. | [optional] 
**caller_name** | **str** | The contact name of caller. | [optional] 
**caller_number** | **str** | The number of caller. | [optional] 
**caller_number_type** | **int** | The caller&#x27;s number type:  * &#x60;1&#x60; — Internal number.  * &#x60;2&#x60; — External number. | [optional] 
**outgoing_by** | [**InlineResponse2009OutgoingBy**](InlineResponse2009OutgoingBy.md) |  | [optional] 
**accepted_by** | [**InlineResponse20085AcceptedBy**](InlineResponse20085AcceptedBy.md) |  | [optional] 
**date_time** | **str** | The date and time when the record is received. | [optional] 
**direction** | **str** | Direction of the call. \&quot;inbound\&quot; | \&quot;outbound\&quot; | [optional] 
**download_url** | **str** | The download URL for the recording. For security purposes, you must provide an OAuth access token in the auth header to download the recording file using this url. &lt;br&gt;  Example request:&lt;br&gt; &#x60;&#x60;&#x60; curl --request GET \\   --url {download_url} \\   --header &#x27;authorization: Bearer {access_token} \\   --header &#x27;content-type: application/json&#x27; &#x60;&#x60;&#x60;  | [optional] 
**duration** | **int** | The call recording&#x27;s duration, in seconds. | [optional] 
**id** | **str** | The ID of the recording. | [optional] 
**transcript_download_url** | **str** | Download url for the recording transcript. For security purposes, you must provide an OAuth access token in the auth header to download the recording transcript file using this url. &lt;br&gt;  Example request:&lt;br&gt; &#x60;&#x60;&#x60; curl --request GET \\   --url {transcript_download_url} \\   --header &#x27;authorization: Bearer {access_token} \\   --header &#x27;content-type: application/json&#x27; &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

