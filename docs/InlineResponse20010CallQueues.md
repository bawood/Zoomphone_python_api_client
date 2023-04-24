# InlineResponse20010CallQueues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_id** | **str** | The extension ID. | [optional] 
**extension_number** | **int** | The extension number assigned to the queue. | [optional] 
**id** | **str** | Unique identifier of the call queue. | [optional] 
**name** | **str** | Name of the Call Queue. | [optional] 
**phone_numbers** | [**list[InlineResponse20010PhoneNumbers]**](InlineResponse20010PhoneNumbers.md) | Phone number(s) assigned to the call queue. | [optional] 
**site** | [**InlineResponse20010Site**](InlineResponse20010Site.md) |  | [optional] 
**status** | **str** | Status of the Call Queue. &#x60;active&#x60;: Call queue is enabled and active. &#x60;inactive&#x60;: Call queue is inactive. Inactive call queues cannot be called but will retain its settings and appear in the [Call Queues](https://zoom.us/pbx/page/telephone/groups#/groups) page. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

