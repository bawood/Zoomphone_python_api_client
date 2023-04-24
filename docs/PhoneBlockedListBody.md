# PhoneBlockedListBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_type** | **str** | State whether you want the block type to be inbound or outbound.  &#x60;inbound&#x60;: Pass this value to prevent the blocked number or prefix from calling into the phone users.  &#x60;outbound&#x60;: Pass this value to prevent phone users from calling the blocked number or prefix. | [optional] 
**comment** | **str** | Provide a comment to help you identify the blocked number or prefix. | [optional] 
**country** | **str** | The country information. For example, entering US or CH. | [optional] 
**match_type** | **str** | Specify the match type for the blocked list:  * &#x60;phoneNumber&#x60;: Choose this option (Phone Number Match) if you want to block a specific phone number. Provide the phone number in the &#x60;phone_number&#x60; field and the country code in the &#x60;country&#x60; field.  * &#x60;prefix&#x60;: Choose this option (Prefix Match) if you want to block all numbers with a specific country or an area code. Enter a phone number in the &#x60;phone_number&#x60; field and in the &#x60;country&#x60; field, enter a country code as part of the prefix. | [optional] 
**phone_number** | **str** | The phone number to be blocked if you passed &#x60;phoneNumber&#x60; as the value for the &#x60;match_type&#x60; field. If you passed &#x60;prefix&#x60; as the value for the &#x60;match_type&#x60; field, provide the prefix of the phone number in the &#x60;country&#x60; field. | [optional] 
**status** | **str** | Enable or disable the blocking. One of the following values are allowed:  &#x60;active&#x60;: Keep the blocking active.  &#x60;inactive&#x60;: Disable the blocking. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

