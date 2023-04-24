# InlineResponse20086

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_code** | **str** | The area code of user. | [optional] 
**audio_prompt_language** | **str** | The audio prompt language code.&lt;br&gt; American English: &#x60;en-US&#x60;&lt;br&gt; British English: &#x60;en-GB&#x60;&lt;br&gt; Español americano: &#x60;es-US&#x60;&lt;br&gt; Français canadien: &#x60;fr-CA&#x60;&lt;br&gt; Dansk: &#x60;da-DK&#x60;&lt;br&gt; Deutsch: &#x60;de-DE&#x60;&lt;br&gt; Español: &#x60;es-ES&#x60;&lt;br&gt; Français: &#x60;fr-FR&#x60;&lt;br&gt; Italiano: &#x60;it-IT&#x60;&lt;br&gt; Nederlands: &#x60;nl-NL&#x60;&lt;br&gt; Portugues portugal: &#x60;pt-PT&#x60;&lt;br&gt; Japanese: &#x60;ja-JP&#x60;&lt;br&gt; Korean: &#x60;ko-KO&#x60;&lt;br&gt; Portugues brasil: &#x60;pt-BR&#x60;&lt;br&gt; Chinese: &#x60;zh-CN&#x60;&lt;br&gt; Taiwanese: &#x60;zh-TW&#x60;&lt;br&gt; | [optional] 
**company_number** | **str** | The [company number](https://support.zoom.us/hc/en-us/articles/360028553691) can be used by external callers to reach your phone users (by dialing the main company number and the user&#x27;s extension). It can also be used by phone users as their caller ID when making calls. | [optional] 
**country** | [**InlineResponse20086Country**](InlineResponse20086Country.md) |  | [optional] 
**delegation** | [**InlineResponse20086Delegation**](InlineResponse20086Delegation.md) |  | [optional] 
**desk_phone** | [**InlineResponse20086DeskPhone**](InlineResponse20086DeskPhone.md) |  | [optional] 
**extension_number** | **int** | The owner&#x27;s extension number. | [optional] 
**music_on_hold_id** | **str** | The music on hold ID.   Options: empty char - default and &#x60;0&#x60; - disable | [optional] 
**outbound_caller** | [**InlineResponse20086OutboundCaller**](InlineResponse20086OutboundCaller.md) |  | [optional] 
**outbound_caller_ids** | [**list[InlineResponse20086OutboundCallerIds]**](InlineResponse20086OutboundCallerIds.md) |  | [optional] 
**status** | **str** | The status of the user. | [optional] 
**voice_mail** | [**list[InlineResponse20086VoiceMail]**](InlineResponse20086VoiceMail.md) | The shared voicemail access member list. &lt;b&gt;Deprecated&lt;/b&gt;, we will completely deprecate this property in a future release. Instead use policy.voicemail_access_members property from &#x27;Get a user&#x27;s profile&#x27; API. | [optional] 
**intercom** | [**InlineResponse20086Intercom**](InlineResponse20086Intercom.md) |  | [optional] 
**auto_call_recording_access_members** | [**list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]**](PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1.md) | The shared automatic call recording access member list. &lt;b&gt;Deprecated&lt;/b&gt;, we will completely deprecate this property in a future release. Instead use policy.auto_call_recording_access_members property from &#x27;Get a user&#x27;s profile&#x27; API. | [optional] 
**ad_hoc_call_recording_access_members** | [**list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]**](PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1.md) | The shared ad hoc call recording access member list. &lt;b&gt;Deprecated&lt;/b&gt;, we will completely deprecate this property in a future release. Instead use policy.ad_hoc_call_recording_access_members property from &#x27;Get a user&#x27;s profile&#x27; API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

