# InlineResponse20085

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **date** | The start time and date of the query. | [optional] 
**next_page_token** | **str** | The next page token paginates through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_count** | **int** | The total number of pages. | [optional] 
**page_size** | **int** | The number of records returned within a single API call for each page. | [optional] 
**recordings** | [**list[InlineResponse20085Recordings]**](InlineResponse20085Recordings.md) | The recordings. | [optional] 
**to** | **date** | The end time and date of the query. | [optional] 
**total_records** | **int** | The total number of records returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

