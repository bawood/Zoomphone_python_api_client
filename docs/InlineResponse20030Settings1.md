# InlineResponse20030Settings1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_callers_check_voicemail** | **bool** | Whether to allow the callers to check voicemails over a phone. Required only when the &#x60;call_not_answer_action&#x60; setting is set to &#x60;1&#x60; (Forward to a voicemail). | [optional] 
**call_forwarding_settings** | [**list[InlineResponse20030Settings1CallForwardingSettings]**](InlineResponse20030Settings1CallForwardingSettings.md) | The call forwarding settings. Returned only for the &#x60;call_forwarding&#x60; sub-setting. | [optional] 
**call_not_answer_action** | **int** | The action to take when a call is not answered:  * &#x60;1&#x60; — Forward to a voicemail.  * &#x60;2&#x60; — Forward to the user.  * &#x60;4&#x60; — Forward to the common area.  * &#x60;6&#x60; — Forward to the auto receptionist.  * &#x60;7&#x60; — Forward to a call queue.  * &#x60;8&#x60; — Forward to a shared line group.  * &#x60;9&#x60; — Forward to an external contact.  * &#x60;10&#x60; - Forward to a phone number.  * &#x60;11&#x60; — Disconnect.  * &#x60;12&#x60; — Play a message, then disconnect.  * &#x60;13&#x60; - Forward to message.  * &#x60;14&#x60; - Forward to interactive voice response (IVR).   Returned only for the &#x60;call_handling&#x60; sub-setting. | [optional] 
**connect_to_operator** | **bool** | Whether to allow callers to reach an operator. Returned only when the &#x60;call_not_answer_action&#x60; setting is set to &#x60;1&#x60; (Forward to a voicemail). | [optional] 
**max_wait_time** | **int** | The max wait time, in seconds, for &#x60;simultaneous&#x60; ring mode or the ring duration for each device for &#x60;sequential&#x60; ring mode:  * &#x60;10&#x60;  * &#x60;15&#x60;  * &#x60;20&#x60;  * &#x60;25&#x60;  * &#x60;30&#x60;  * &#x60;35&#x60;  * &#x60;40&#x60;  * &#x60;45&#x60;  * &#x60;50&#x60;  * &#x60;55&#x60;  * &#x60;60&#x60;   Returned only for the &#x60;call_handling&#x60; sub-setting. | [optional] 
**require_press_1_before_connecting** | **bool** | When a call is forwarded to a personal phone number, whether the user must press \&quot;1\&quot; before the call connects. This helps to ensure that missed calls do not reach to your personal voicemail. Returned only for the &#x60;call_forwarding&#x60; sub-setting. | [optional] 
**ring_mode** | **str** | The call handling&#x27;s ring mode setting:  * &#x60;simultaneous&#x60;  * &#x60;sequential&#x60;   Returned only for the &#x60;call_handling&#x60; sub-setting. | [optional] 
**routing** | [**InlineResponse20030SettingsRouting**](InlineResponse20030SettingsRouting.md) |  | [optional] 
**busy_routing** | [**InlineResponse20030SettingsRouting**](InlineResponse20030SettingsRouting.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

