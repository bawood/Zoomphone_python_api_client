# InlineResponse2004CallerEntersNoAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **int** | The action if the caller enters no action after the prompt played.&lt;br&gt; &#x60;-1&#x60; Disconnect the call&lt;br&gt; &#x60;2&#x60; Forward to the user &lt;br&gt;&#x60;4&#x60; Forward to the common area &lt;br&gt;&#x60;5&#x60; Forward to Cisco/Polycom Room &lt;br&gt;&#x60;6&#x60; Forward to the auto receptionist &lt;br&gt;&#x60;7&#x60; Forward to the call queue &lt;br&gt;&#x60;8&#x60; Forward to the shared line group &lt;br&gt;&#x60;15&#x60; Forward to the Contact Center  | [optional] 
**audio_prompt_repeat** | **int** | The number of times to repeat the audio prompt. | [optional] 
**forward_to** | [**InlineResponse2004CallerEntersNoActionForwardTo**](InlineResponse2004CallerEntersNoActionForwardTo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

