# UsersUserIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emergency_address_id** | **str** | The emergency address ID. | [optional] 
**extension_number** | **str** | The extension number of the user. The number must be complete (i.e. site number + short extension). | [optional] 
**policy** | [**PhoneusersuserIdPolicy**](PhoneusersuserIdPolicy.md) |  | [optional] 
**site_id** | **str** | The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672) where the user should be moved or assigned.  | [optional] 
**template_id** | **str** | The settings template ID. If the &#x60;site_id&#x60; field is set, look for the template site with the value of the &#x60;site_id&#x60; field. The template ID has precedence and the policy will be ignored even if the &#x60;policy&#x60; field is set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

