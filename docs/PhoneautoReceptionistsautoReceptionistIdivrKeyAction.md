# PhoneautoReceptionistsautoReceptionistIdivrKeyAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **int** | The action after clicking the key.&lt;br&gt; For key &#x60;0&#x60;-&#x60;9&#x60; 100 Leave voicemail to the current extension 200 Leave voicemail to the user 300 Leave voicemail to the auto receptionist 400 Leave voicemail to the  call queue 500 Leave voicemail to the shared line group 2 Forward to the user 3 Forward to Zoom Room 4 Forward to the common area 5 Forward to Cisco/Polycom Room 6 Forward to the auto receptionist 7 Forward to the call queue 8 Forward to the shared line group 9 Forward to external contacts 10 Forward to a phone number 15 Forward to the contact center 16 Forward to the meeting service 17 Forward to the meeting service number -1 Disabled  For key * or # 21 Repeat menu greeting 22 Return to the root menu 23 Return to the previous menu -1 Disabled | [optional] 
**key** | **str** | The key. The following values are supported: numeric(&#x27;0&#x27;-&#x27;9&#x27;), *, #. | [optional] 
**target** | [**PhoneautoReceptionistsautoReceptionistIdivrKeyActionTarget**](PhoneautoReceptionistsautoReceptionistIdivrKeyActionTarget.md) |  | [optional] 
**voicemail_greeting_id** | **str** | The voicemail greeting file ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

