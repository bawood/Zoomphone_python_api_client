# InlineResponse2004KeyActions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **int** | The action after clicking the key.&lt;br&gt; For key &#x60;0&#x60;-&#x60;9&#x60;&lt;br&gt; &#x60;100&#x60; Leave voicemail to the current extension&lt;br&gt; &#x60;200&#x60; Leave voicemail to the user&lt;br&gt; &#x60;300&#x60; Leave voicemail to the auto receptionist&lt;br&gt; &#x60;400&#x60; Leave voicemail to the  call queue&lt;br&gt; &#x60;500&#x60; Leave voicemail to the shared line group&lt;br&gt; &#x60;2&#x60; Forward to the user&lt;br&gt; &#x60;3&#x60; Forward to Zoom Room&lt;br&gt; &#x60;4&#x60; Forward to the common area&lt;br&gt; &#x60;5&#x60; Forward to Cisco/Polycom Room&lt;br&gt; &#x60;6&#x60; Forward to the auto receptionist&lt;br&gt; &#x60;7&#x60; Forward to the call queue&lt;br&gt; &#x60;8&#x60; Forward to the shared line group&lt;br&gt; &#x60;9&#x60; Forward to external contacts&lt;br&gt; &#x60;10&#x60; Forward to a phone number&lt;br&gt; &#x60;15&#x60; Forward to the contact center&lt;br&gt; &#x60;16&#x60; Forward to the meeting service&lt;br&gt; &#x60;17&#x60; Forward to the meeting service number&lt;br&gt; &#x60;-1&#x60; Disabled  For key * or #&lt;br&gt; &#x60;21&#x60; Repeat menu greeting&lt;br&gt; &#x60;22&#x60; Return to the root menu&lt;br&gt; &#x60;23&#x60; Return to the previous menu&lt;br&gt; &#x60;-1&#x60; Disabled | [optional] 
**key** | **str** | The key. The following values are supported: numeric(&#x27;0&#x27;-&#x27;9&#x27;), *, #. | [optional] 
**target** | [**InlineResponse2004Target**](InlineResponse2004Target.md) |  | [optional] 
**voicemail_greeting** | [**InlineResponse2004VoicemailGreeting**](InlineResponse2004VoicemailGreeting.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

