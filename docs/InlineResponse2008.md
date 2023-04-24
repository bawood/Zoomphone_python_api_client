# InlineResponse2008

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | Unique identifier of the phone call. | [optional] 
**call_type** | **str** | The type of call:  * &#x60;voip&#x60; (Voice over IP) * &#x60;pstn&#x60; (Public Switched Telephone Network) * &#x60;tollfree&#x60; * &#x60;international&#x60; * &#x60;contactCenter&#x60; | [optional] 
**callee_country_code** | **str** | Country calling code. | [optional] 
**callee_country_iso_code** | **str** | ISO alpha2 country code. | [optional] 
**callee_did_number** | **str** | Callee&#x27;s DID (direct inward dial) number in e164 format. | [optional] 
**callee_name** | **str** | Contact name of callee. | [optional] 
**callee_number** | **str** | Number of callee. | [optional] 
**callee_number_type** | **int** | The callee&#x27;s number type: * &#x60;1&#x60; — Extension number. * &#x60;2&#x60; — Phone number. * &#x60;3&#x60; — Customized emergency number. | [optional] 
**callee_number_source** | **str** | Indicates where the phone number comes from: * &#x60;internal&#x60; — ZP native. * &#x60;external&#x60; — BYOC or Provider Exchange. * &#x60;byop&#x60; — Premise peering. Not available when &#x60;callee_number_type &#x3D; 1&#x60;. | [optional] 
**caller_country_code** | **str** | Country calling code. | [optional] 
**caller_country_iso_code** | **str** | ISO alpha2 country code. | [optional] 
**caller_did_number** | **str** | Caller&#x27;s DID (direct inward dial) number in e164 format. | [optional] 
**caller_name** | **str** | Contact name of caller. | [optional] 
**caller_number** | **str** | Number of caller. | [optional] 
**caller_number_type** | **int** | The caller&#x27;s number type:  * &#x60;1&#x60; — Extension number.  * &#x60;2&#x60; — Phone number. | [optional] 
**caller_number_source** | **str** | Indicates where the phone number comes from: * &#x60;internal&#x60; — ZP native. * &#x60;external&#x60; — BYOC or Provider Exchange. * &#x60;byop&#x60; — Premise peering. Not available when &#x60;caller_number_type &#x3D; 1&#x60;. | [optional] 
**caller_billing_reference_id** | **str** | Billing reference ID (for peering phone numbers). | [optional] 
**date_time** | **str** | Start time of the call. | [optional] 
**device_private_ip** | **str** | Display the device&#x27;s private IP address if the account has the &#x60;show_device_ip_for_call_log&#x60; parameter set to &#x60;enabled&#x60;. | [optional] 
**device_public_ip** | **str** | Display the device&#x27;s public IP address if the account has the &#x60;show_device_ip_for_call_log&#x60; parameter set to &#x60;enabled&#x60;. | [optional] 
**direction** | **str** | Direction of the call: &#x60;inbound&#x60; | &#x60;outbound&#x60; | [optional] 
**duration** | **int** | Duration of the call in seconds. | [optional] 
**has_recording** | **bool** | Whether the call has a recording. See [announcement](https://marketplace.zoom.us/docs/guides/stay-up-to-date/announcements#deprecation-of-the-has_voicemail-and-has_recording-responses-in-phone-api) from July, 2021. | [optional] 
**has_voicemail** | **bool** | Whether the call has a voicemail. See [announcement](https://marketplace.zoom.us/docs/guides/stay-up-to-date/announcements#deprecation-of-the-has_voicemail-and-has_recording-responses-in-phone-api) from July, 2021. | [optional] 
**id** | **str** | The call log ID. | [optional] 
**log_details** | [**list[InlineResponse2008LogDetails]**](InlineResponse2008LogDetails.md) | The call segment details. | [optional] 
**path** | **str** | Path of the call. | [optional] 
**result** | **str** | Result of the call: &#x60;Missed&#x60; | &#x60;Voicemail&#x60; | &#x60;Call connected&#x60; | &#x60;Rejected&#x60; | &#x60;Blocked&#x60;| &#x60;Busy&#x60;| &#x60;Wrong Number&#x60;| &#x60;No Answer&#x60;| &#x60;International Disabled&#x60;| &#x60;Internal Error&#x60;| &#x60;Call failed&#x60; | &#x60;Restricted Number&#x60;| &#x60;Call Cancel&#x60; | &#x60;Message&#x60;| &#x60;Answered by Other Member&#x60; | &#x60;Call Cancelled&#x60; | &#x60;Park&#x60; | &#x60;Parked&#x60; | &#x60;Blocked by non-GAL&#x60; |  &#x60;Blocked by info-Barriers&#x60; | &#x60;Recording Failure&#x60;| &#x60;Recorded&#x60;| &#x60;Auto Recorded&#x60;. | [optional] 
**department** | **str** | Name of the user&#x27;s department. | [optional] 
**cost_center** | **str** | The cost center name to which a user belongs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

