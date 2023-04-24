# PhoneDevicesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_to** | **str** | User ID or email address of the user to whom this device is to be assigned. The User ID and the email of the user can be retrieved using the [List Users](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods#operation/users) API. | [optional] 
**assignee_extension_ids** | **list[str]** | Available only for the account that has enabled the common area feature.   Extension ID of the [&#x60;user&#x60;](https://marketplace.zoom.us/docs/api-reference/phone/methods/#operation/phoneUser) or [&#x60;common area&#x60; ID](https://marketplace.zoom.us/docs/api-reference/phone/methods/#operation/listCommonAreas). | [optional] 
**display_name** | **str** | Display name of the desk phone. | 
**mac_address** | **str** | The MAC address of the desk phone.   Note: If you&#x27;re using a wireless phone, enter the wired MAC address, not the wireless MAC address. | 
**model** | **str** | Model name of the device. | [optional] 
**type** | **str** | Manufacturer (brand) name of the device. | [optional] 
**provision_template_id** | **str** | Provision template id. Supported only by some devices. Empty string represents &#x27;No value set&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

