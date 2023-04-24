# InlineResponse20027

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The emergency address line 1. | [optional] 
**address_line2** | **str** | The emergency address line 2. | [optional] 
**city** | **str** | The emergency address city. | [optional] 
**country** | **str** | The emergency address country. | [optional] 
**id** | **str** | The emergency address ID. | [optional] 
**is_default** | **bool** | Indicates whether the emergency address is default or not. | [optional] 
**level** | **int** | The emergency address owner level:  * &#x60;0&#x60; - Account/Company-level emergency address.   * &#x60;1&#x60; - User/Personal-level emergency address.  * &#x60;2&#x60; - Unknown company/pending emergency address. | [optional] 
**owner** | [**InlineResponse20027Owner**](InlineResponse20027Owner.md) |  | [optional] 
**site** | [**InlineResponse20026Site**](InlineResponse20026Site.md) |  | [optional] 
**state_code** | **str** | The emergency address state code. | [optional] 
**status** | **int** | The emergency address verification status:  * &#x60;1&#x60; — Verification not required.  * &#x60;2&#x60; — Unverified.  * &#x60;3&#x60; — Verification requested.  * &#x60;4&#x60; — Verified.  * &#x60;5&#x60; — Rejected.  * &#x60;6&#x60; — Verification failed. | [optional] 
**zip** | **str** | The emergency address zip code. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

