# RoutingRulesRoutingRuleIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Routing rule name. | [optional] 
**number_pattern** | **str** | Perl-compatible number_pattern expression. | [optional] 
**order** | **int** | Routing rule order to be applied, &#x27;1&#x27; being the highest. Order inserting occurs when this field is filled. It will automatically readjust the order of rules between the target order and the current order. | [optional] 
**sip_group_id** | **str** | Unique identifier of the SIP Group: must not be null when &#x27;type&#x27; &#x3D; &#x27;sip_group&#x27;. | [optional] 
**translation** | **str** | &#x60;nullable&#x60; Optional replacement pattern: must be in E.164 format. | [optional] 
**type** | **str** | Routing path type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

