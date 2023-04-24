# InlineResponse20046Assignee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_prompt_language** | **str** |  | [optional] 
**display_number** | **str** | Used for meeting service. Define how the number will be formatted and displayed in meeting invitations and emails. | [optional] 
**extension_number** | **int** | Extension number of the Phone. | [optional] 
**greeting** | [**InlineResponse20046AssigneeGreeting**](InlineResponse20046AssigneeGreeting.md) |  | [optional] 
**id** | **str** | ID of the user to whom the number and the following are assigned: emergency number pool (if the account has multiple sites enabled, the ID is &#x60;siteId&#x60;, else &#x60;accountId&#x60;) and company location  | [optional] 
**label** | **str** | Optional, used for meeting service. This label will be appended to the number in parentheses, and will appear in meeting invitations and the zoom client. Formatting rules: Maximum 32 characters Do not use digits Do not use characters \&quot;(\&quot; \&quot;)\&quot; \&quot;,\&quot; \&quot;;\&quot; or \&quot;:\&quot; | [optional] 
**meeting_id** | **str** | Meeting ID used for meeting service. | [optional] 
**name** | **str** | Name of the user to whom the number, emergency number pool and company location are assigned. | [optional] 
**on_hold_music** | [**InlineResponse20046AssigneeOnHoldMusic**](InlineResponse20046AssigneeOnHoldMusic.md) |  | [optional] 
**type** | **str** | Indicates who the phone number belongs to.&lt;br&gt; &#x60;user&#x60;: Number has been assigned to an existing phone user allowing them to receive calls through their extension number or direct phone number.&lt;br&gt; &#x60;callQueue&#x60;: Phone number has been assigned to a [call queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues).&lt;br&gt; &#x60;commonAreaPhone&#x60;: Phone number has been assigned to a [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-common-area-phones).&lt;br&gt; &#x60;autoReceptionist&#x60;: Phone number has been assigned to an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Integrated-Voice-Response-IVR-).&lt;br&gt; &#x60;emergencyNumberPool&#x60; &#x60;companyLocation&#x60; &#x60;meetingService&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

