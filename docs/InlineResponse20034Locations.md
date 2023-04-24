# InlineResponse20034Locations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bssid** | **str** | The emergency service location&#x27;s BSSID (Basic Service Set Identifier). | [optional] 
**elin** | [**InlineResponse20034Elin**](InlineResponse20034Elin.md) |  | [optional] 
**id** | **str** | The emergency service location&#x27;s ID. | [optional] 
**identifier** | **str** | The emergency service location&#x27;s unique ID. | [optional] 
**name** | **str** | The emergency service location&#x27;s name. | [optional] 
**network_switches** | [**list[InlineResponse20034NetworkSwitches]**](InlineResponse20034NetworkSwitches.md) |  | [optional] 
**parent_location_id** | **str** | The parent location&#x27;s ID. | [optional] 
**private_ip** | **str** | The emergency service location&#x27;s subnet or private IP address. | [optional] 
**public_ip** | **str** | The emergency service location&#x27;s public IP address. | [optional] 
**sip_group** | [**InlineResponse20034SipGroup**](InlineResponse20034SipGroup.md) |  | [optional] 
**site** | [**InlineResponse20034Site**](InlineResponse20034Site.md) |  | [optional] 
**emergency_address** | [**InlineResponse20034EmergencyAddress**](InlineResponse20034EmergencyAddress.md) |  | [optional] 
**minimum_match_criteria** | **bool** | If true, it requires a user&#x27;s location match on both public and private IP address, or BSSID, or network switch; detecting only a public IP address is not enough to detect the location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

