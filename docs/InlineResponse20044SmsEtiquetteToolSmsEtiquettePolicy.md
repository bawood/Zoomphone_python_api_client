# InlineResponse20044SmsEtiquetteToolSmsEtiquettePolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The SMS etiquette policy ID. | [optional] 
**name** | **str** | The SMS etiquette policy name. | [optional] 
**description** | **str** | The SMS etiquette policy description. | [optional] 
**rule** | **int** | The SMS etiquette policy rule, &#x60;1&#x60; - Keywords, &#x60;2&#x60; - Regular Expression. | [optional] 
**content** | **str** | The SMS etiquette policy content. For rule &#x60;1&#x60;, add keywords separated by comma, the following characters are supported A-Z, a-z, 0-9. For rule &#x60;2&#x60;, add regular expressions, back references and zero-width assertions area not supported. | [optional] 
**action** | **int** | The actions taken when a policy is triggered, &#x60;1&#x60; - ask user to confirm sending of message, &#x60;2&#x60; - block the message. | [optional] 
**active** | **bool** | Whether active or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

