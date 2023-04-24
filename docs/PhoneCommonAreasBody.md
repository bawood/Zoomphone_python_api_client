# PhoneCommonAreasBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calling_plans** | [**list[PhonecommonAreasCallingPlans]**](PhonecommonAreasCallingPlans.md) |  | [optional] 
**country_iso_code** | **str** | Two-lettered country [code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries). | [optional] 
**display_name** | **str** | Display name of the common area. Enter at least 3 characters. | 
**extension_number** | **int** | Extension number assigned to the common area. If the site code is enabled, provide the short extension number instead. | [optional] 
**site_id** | **str** | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. | [optional] 
**timezone** | **str** | [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

