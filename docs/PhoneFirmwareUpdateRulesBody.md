# PhoneFirmwareUpdateRulesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. Required if multiple sites are enabled. | [optional] 
**version** | **str** | Firmware version. | 
**device_type** | **str** | Device type. | 
**device_model** | **str** | Device model name. | 
**restart_type** | **int** | Restart type: &#x60;1&#x60; - Restart the devices immediately. &#x60;2&#x60; - Restart with the next resync or auto pull | [optional] [default to Restart_typeEnum._1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

