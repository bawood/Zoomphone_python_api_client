# InlineResponse20024Provision

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sip_accounts** | [**list[InlineResponse20024ProvisionSipAccounts]**](InlineResponse20024ProvisionSipAccounts.md) | SIP Account details registered during the device provisioning process. This object will only be returned if manual provisioning was used for the device.   | [optional] 
**type** | **str** | [Provisioning type](https://support.zoom.us/hc/en-us/articles/360033223411). The value can be one of the following:  * &#x60;ztp&#x60; : Zero touch provisioning. * &#x60;assisted&#x60;: Assisted provisioning. * &#x60;manual&#x60;: Manual provisioning.    | [optional] 
**url** | **str** | Provisioning URL. This field will only be returned for devices that were provisioned via &#x60;assisted&#x60; provisioning type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

