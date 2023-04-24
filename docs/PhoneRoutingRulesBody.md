# PhoneRoutingRulesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Routing rule name. | [optional] 
**number_pattern** | **str** | Perl-compatible number_pattern expression. | [optional] 
**sip_group_id** | **str** | Unique identifier of the SIP group. Cannot be null when &#x27;type&#x27; &#x3D; &#x27;sip_group&#x27;. | [optional] 
**site_id** | **str** | Unique identifier of the site.&#x60;nullable&#x60; | [optional] 
**translation** | **str** | Optional replacement pattern: must be in E.164 format.&#x60;nullable&#x60; | [optional] 
**type** | **str** | Routing path type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

