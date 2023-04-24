# PhonebatchLocationsLocations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bssid** | **str** | The location&#x27;s BSSID (Basic Service Set Identifier). | [optional] 
**company_address** | [**PhonebatchLocationsCompanyAddress**](PhonebatchLocationsCompanyAddress.md) |  | 
**display_name** | **str** | The location&#x27;s display name. | 
**elin** | **str** | The location&#x27;s ELIN (Emergency Location Identification Number). This value can be a BYOC number. If you use a BYOC number, you will need to manually update the BYOC address with your carrier. | [optional] 
**identifier** | **str** | The location&#x27;s ID. | 
**network_switches** | [**list[PhonebatchLocationsNetworkSwitches]**](PhonebatchLocationsNetworkSwitches.md) |  | [optional] 
**parent_identifier** | **str** | The location&#x27;s parent location ID. Leave this value empty if the current location is a top location. | [optional] 
**private_ip** | **str** | The location&#x27;s subnet or private IP address. This field is required if &#x60;minimum_match_criteria&#x60; is true. | [optional] 
**public_ip** | **str** | The location&#x27;s public IP address. This field is required for top locations. | [optional] 
**sip_group_name** | **str** | The location&#x27;s assigned SIP routing group for outgoing calls. The system routes the call to the defined [SIP trunk](https://en.wikipedia.org/wiki/SIP_trunking) in the SIP groups when location-based routing is enabled.  This only affects top locations and ignores all other locations. | [optional] 
**minimum_match_criteria** | **bool** | If true, it requires a user&#x27;s location match on both public and private IP address, or BSSID, or network switch; detecting only a public IP address is not enough to detect the location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

