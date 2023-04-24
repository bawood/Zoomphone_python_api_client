# PhoneExternalContactsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The external contact&#x27;s description. | [optional] 
**email** | **str** | The external contact&#x27;s email address. | [optional] 
**extension_number** | **str** | The external contact&#x27;s extension number in the original phone system. Make certain that this extension number is **not** duplicated with an existing extension number in the account. | [optional] 
**id** | **str** | The customer-configured external contact ID. It is recommended that you use a primary key from the original phone system.  If you do **not** use this parameter, the API automatically generates an &#x60;externalContactId&#x60;. | [optional] 
**name** | **str** | The external contact&#x27;s username or extension display name. | 
**phone_numbers** | **list[str]** | A comma-separated list of the external contact&#x27;s phone numbers. This value **must** be in [E.164](https://en.wikipedia.org/wiki/E.164) format. If you do not provide an extension number, you **must** provide this value. | [optional] 
**routing_path** | **str** | The external contact&#x27;s SIP group, to define the call routing path. This is for customers that use SIP trunking. | [optional] 
**auto_call_recorded** | **bool** | Whether to allow the automatic call recording. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

