# InlineResponse2006

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_type** | **str** | Block type.  * &#x60;inbound&#x60;: The blocked number or numbers with the specifie prefix are prevented from calling in to phone users.  * &#x60;outbound&#x60;: The phone users  are prevented from calling the blocked number or numbers with the specified prefix. | [optional] 
**comment** | **str** | Provide a comment to help you identify the blocked number or prefix. | [optional] 
**id** | **str** | Unique identifier of the blocked list. | [optional] 
**match_type** | **str** | Indicates the match type for the blocked list. The values can be one of the following:  * &#x60;phoneNumber&#x60;: Indicates that only a specific phone number that is shown in the &#x60;phone_number&#x60; field is blocked.  * &#x60;prefix&#x60;: Indicates that all numbers starting with prefix that is shown in the &#x60;phone_number&#x60; field are blocked. | [optional] 
**phone_number** | **str** | The phone number or the prefix number that is blocked based on the &#x60;match_type&#x60;. Displayed in E164 format. | [optional] 
**status** | **str** | Indicates whether the blocking is active or inactive.  *n&#x60;active&#x60;: The blocked list is active.  * &#x60;inactive&#x60;: The blocked list is inactive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

