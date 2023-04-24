# PhonebatchLocationsNetworkSwitches

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | The location&#x27;s assigned MAC address. It&#x27;s required if the &#x60;network_switches&#x60; value is set. | [optional] 
**port** | **str** | The location&#x27;s port label. You **cannot** pass this parameter with the &#x60;port_prefix&#x60; and &#x60;port_range&#x60; parameter. | [optional] 
**port_prefix** | **str** | The location&#x27;s port prefix. The prefix value **cannot** end with a digit.  This parameter passes with the &#x60;port_range_from&#x60; and &#x60;port_range_to&#x60; parameters. | [optional] 
**port_range_from** | **str** | The location&#x27;s port starting range number. It can be a non-negative integer value.  This value **must** be less than or equal to the &#x60;port_range_to&#x60; value. | [optional] 
**port_range_to** | **str** | The location&#x27;s port ending range number. It can be a non-negative integer value.  This value **cannot** be less than the &#x60;port_range_from&#x60; value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

