# PhoneusersuserIdPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_hoc_call_recording** | [**PhoneusersuserIdPolicyAdHocCallRecording**](PhoneusersuserIdPolicyAdHocCallRecording.md) |  | [optional] 
**auto_call_recording** | [**PhoneusersuserIdPolicyAutoCallRecording**](PhoneusersuserIdPolicyAutoCallRecording.md) |  | [optional] 
**call_overflow** | [**PhoneusersuserIdPolicyCallOverflow**](PhoneusersuserIdPolicyCallOverflow.md) |  | [optional] 
**call_park** | [**PhoneusersuserIdPolicyCallPark**](PhoneusersuserIdPolicyCallPark.md) |  | [optional] 
**call_transferring** | [**PhoneusersuserIdPolicyCallTransferring**](PhoneusersuserIdPolicyCallTransferring.md) |  | [optional] 
**delegation** | **bool** | Whether the user can use [call delegation](https://support.zoom.us/hc/en-us/articles/360032881731-Setting-up-call-delegation-shared-lines-appearance-). | [optional] 
**elevate_to_meeting** | **bool** | Whether the user can elevate their phone calls to a meeting. | [optional] 
**emergency_address_management** | [**PhoneusersuserIdPolicyEmergencyAddressManagement**](PhoneusersuserIdPolicyEmergencyAddressManagement.md) |  | [optional] 
**emergency_calls_to_psap** | **bool** | When disabled, emergency calls placed by the user will not be delivered to the Public Safety Answering Point(PSAP), but still will be delivered to the Internal Safety Response Team based on the settings. | [optional] 
**forwarding_to_external_numbers** | **bool** | Whether to allow call forwarding to external numbers. Use the &#x60;call_handling_forwarding_to_other_users&#x60; instead. | [optional] 
**call_handling_forwarding_to_other_users** | [**PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers**](PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.md) |  | [optional] 
**hand_off_to_room** | [**PhoneusersuserIdPolicyHandOffToRoom**](PhoneusersuserIdPolicyHandOffToRoom.md) |  | [optional] 
**international_calling** | **bool** | Whether the current extension can make international calls outside of their calling plan. | [optional] 
**mobile_switch_to_carrier** | [**PhoneusersuserIdPolicyMobileSwitchToCarrier**](PhoneusersuserIdPolicyMobileSwitchToCarrier.md) |  | [optional] 
**select_outbound_caller_id** | [**PhoneusersuserIdPolicySelectOutboundCallerId**](PhoneusersuserIdPolicySelectOutboundCallerId.md) |  | [optional] 
**sms** | [**PhoneusersuserIdPolicySms**](PhoneusersuserIdPolicySms.md) |  | [optional] 
**voicemail** | [**PhoneusersuserIdPolicyVoicemail**](PhoneusersuserIdPolicyVoicemail.md) |  | [optional] 
**voicemail_access_members** | [**list[PhoneusersuserIdPolicyVoicemailAccessMembers]**](PhoneusersuserIdPolicyVoicemailAccessMembers.md) | This field updates a voicemail setting. &lt;b&gt;Deprecated:&lt;/b&gt; we will completely deprecate this property in a future release. Use &#x60;Add/Update/Delete a user&#x27;s shared access setting&#x60; API instead, with settingType &#x27;voice-mail&#x27; to manage the voicemail access members. | [optional] 
**zoom_phone_on_mobile** | [**PhoneusersuserIdPolicyZoomPhoneOnMobile**](PhoneusersuserIdPolicyZoomPhoneOnMobile.md) |  | [optional] 
**personal_audio_library** | [**PhoneusersuserIdPolicyPersonalAudioLibrary**](PhoneusersuserIdPolicyPersonalAudioLibrary.md) |  | [optional] 
**voicemail_transcription** | [**PhoneusersuserIdPolicyVoicemailTranscription**](PhoneusersuserIdPolicyVoicemailTranscription.md) |  | [optional] 
**voicemail_notification_by_email** | [**PhoneusersuserIdPolicyVoicemailNotificationByEmail**](PhoneusersuserIdPolicyVoicemailNotificationByEmail.md) |  | [optional] 
**shared_voicemail_notification_by_email** | [**PhoneusersuserIdPolicySharedVoicemailNotificationByEmail**](PhoneusersuserIdPolicySharedVoicemailNotificationByEmail.md) |  | [optional] 
**check_voicemails_over_phone** | [**PhoneusersuserIdPolicyCheckVoicemailsOverPhone**](PhoneusersuserIdPolicyCheckVoicemailsOverPhone.md) |  | [optional] 
**audio_intercom** | [**PhoneusersuserIdPolicyAudioIntercom**](PhoneusersuserIdPolicyAudioIntercom.md) |  | [optional] 
**e2e_encryption** | [**PhoneusersuserIdPolicyE2eEncryption**](PhoneusersuserIdPolicyE2eEncryption.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

