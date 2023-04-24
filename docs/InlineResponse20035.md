# InlineResponse20035

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bssid** | **str** | The emergency service location&#x27;s BSSIDs (Basic Service Set Identifiers). | [optional] 
**elin** | [**InlineResponse20035Elin**](InlineResponse20035Elin.md) |  | [optional] 
**emergency_address** | [**InlineResponse20035EmergencyAddress**](InlineResponse20035EmergencyAddress.md) |  | [optional] 
**id** | **str** | The emergency location&#x27;s ID. | [optional] 
**name** | **str** | The emergency location&#x27;s name. | [optional] 
**network_switches** | [**list[InlineResponse20035NetworkSwitches]**](InlineResponse20035NetworkSwitches.md) |  | [optional] 
**parent_location_id** | **str** | The emergency location&#x27;s parent location ID. | [optional] 
**private_ip** | **str** | The emergency location&#x27;s subnet or private IP address. | [optional] 
**public_ip** | **str** | The emergency location&#x27;s public IP address. | [optional] 
**sip_group** | [**InlineResponse20035SipGroup**](InlineResponse20035SipGroup.md) |  | [optional] 
**site** | [**InlineResponse20035Site**](InlineResponse20035Site.md) |  | [optional] 
**minimum_match_criteria** | **bool** | If true, it requires a user&#x27;s location match on both public and private IP address, or BSSID, or network switch; detecting only a public IP address is not enough to detect the location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

