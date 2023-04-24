# PhoneLocationsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bssid** | **str** | A comma-separated list of the emergency service location&#x27;s BSSIDs (Basic Service Set Identifiers). | [optional] 
**elin_phone_number_id** | **str** | The ELIN (Emergency Location Identification Number). This value must be a phone number ID or phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. | [optional] 
**emergency_address_id** | **str** | The emergency location address ID. | 
**name** | **str** | The emergency service location&#x27;s name. | 
**parent_location_id** | **str** | The parent location&#x27;s ID to assign to the emergency service location. | [optional] 
**private_ip** | **str** | A comma-separated list of the emergency service location&#x27;s subnet or private IP addresses. This field is required if &#x60;minimum_match_criteria&#x60; is true. | [optional] 
**public_ip** | **str** | A comma-separated list of the emergency service location&#x27;s public IP addresses. This parameter is required for top locations. | [optional] 
**sip_group_id** | **str** | The SIP group ID to assign to the emergency service location. This value is not required for non-top locations. | [optional] 
**site_id** | **str** | The site ID. | [optional] 
**minimum_match_criteria** | **bool** | If true, it requires a user&#x27;s location match on both public and private IP address, or BSSID, or network switch; detecting only a public IP address is not enough to detect the location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

