# InlineResponse20078Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_hoc_call_recording** | [**InlineResponse20078PolicyAdHocCallRecording**](InlineResponse20078PolicyAdHocCallRecording.md) |  | [optional] 
**ad_hoc_call_recording_access_members** | [**list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]**](PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1.md) | The shared ad hoc call recording access member list. | [optional] 
**auto_call_recording** | [**InlineResponse20078PolicyAutoCallRecording**](InlineResponse20078PolicyAutoCallRecording.md) |  | [optional] 
**auto_call_recording_access_members** | [**list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]**](PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1.md) | The shared automatic call recording access member list. | [optional] 
**call_overflow** | [**InlineResponse20078PolicyCallOverflow**](InlineResponse20078PolicyCallOverflow.md) |  | [optional] 
**call_park** | [**InlineResponse20078PolicyCallPark**](InlineResponse20078PolicyCallPark.md) |  | [optional] 
**call_transferring** | [**InlineResponse20078PolicyCallTransferring**](InlineResponse20078PolicyCallTransferring.md) |  | [optional] 
**delegation** | **bool** | Whether the user can use [call delegation](https://support.zoom.us/hc/en-us/articles/360032881731-Setting-up-call-delegation-shared-lines-appearance-). | [optional] 
**elevate_to_meeting** | **bool** | Whether the user can elevate their phone calls to a meeting. | [optional] 
**emergency_address_management** | [**PhoneusersuserIdPolicyEmergencyAddressManagement**](PhoneusersuserIdPolicyEmergencyAddressManagement.md) |  | [optional] 
**emergency_calls_to_psap** | **bool** | When disabled, emergency calls placed by the user will not be delivered to the Public Safety Answering Point(PSAP), but still will be delivered to the Internal Safety Response Team based on the settings. | [optional] 
**forwarding_to_external_numbers** | **bool** | Whether call forwarding to external numbers is enabled. Use the &#x60;call_handling_forwarding_to_other_users&#x60; instead. | [optional] 
**call_handling_forwarding_to_other_users** | [**InlineResponse20078PolicyCallHandlingForwardingToOtherUsers**](InlineResponse20078PolicyCallHandlingForwardingToOtherUsers.md) |  | [optional] 
**hand_off_to_room** | [**InlineResponse20078PolicyHandOffToRoom**](InlineResponse20078PolicyHandOffToRoom.md) |  | [optional] 
**international_calling** | **bool** | Whether the current extension can make international calls outside of their calling plan. | [optional] 
**mobile_switch_to_carrier** | [**InlineResponse20078PolicyMobileSwitchToCarrier**](InlineResponse20078PolicyMobileSwitchToCarrier.md) |  | [optional] 
**select_outbound_caller_id** | [**InlineResponse20078PolicySelectOutboundCallerId**](InlineResponse20078PolicySelectOutboundCallerId.md) |  | [optional] 
**sms** | [**InlineResponse20078PolicySms**](InlineResponse20078PolicySms.md) |  | [optional] 
**voicemail** | [**InlineResponse20078PolicyVoicemail**](InlineResponse20078PolicyVoicemail.md) |  | [optional] 
**voicemail_access_members** | [**list[PhoneusersuserIdsettingssettingTypeVoicemailAccessMembers]**](PhoneusersuserIdsettingssettingTypeVoicemailAccessMembers.md) | The shared voicemail access member list. | [optional] 
**zoom_phone_on_mobile** | [**InlineResponse20078PolicyZoomPhoneOnMobile**](InlineResponse20078PolicyZoomPhoneOnMobile.md) |  | [optional] 
**personal_audio_library** | [**InlineResponse20078PolicyPersonalAudioLibrary**](InlineResponse20078PolicyPersonalAudioLibrary.md) |  | [optional] 
**voicemail_transcription** | [**InlineResponse20078PolicyVoicemailTranscription**](InlineResponse20078PolicyVoicemailTranscription.md) |  | [optional] 
**voicemail_notification_by_email** | [**InlineResponse20078PolicyVoicemailNotificationByEmail**](InlineResponse20078PolicyVoicemailNotificationByEmail.md) |  | [optional] 
**shared_voicemail_notification_by_email** | [**InlineResponse20078PolicySharedVoicemailNotificationByEmail**](InlineResponse20078PolicySharedVoicemailNotificationByEmail.md) |  | [optional] 
**check_voicemails_over_phone** | [**InlineResponse20078PolicyCheckVoicemailsOverPhone**](InlineResponse20078PolicyCheckVoicemailsOverPhone.md) |  | [optional] 
**audio_intercom** | [**InlineResponse20078PolicyAudioIntercom**](InlineResponse20078PolicyAudioIntercom.md) |  | [optional] 
**e2e_encryption** | [**InlineResponse20078PolicyE2eEncryption**](InlineResponse20078PolicyE2eEncryption.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

