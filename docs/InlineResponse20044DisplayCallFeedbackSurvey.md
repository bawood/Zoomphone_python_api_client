# InlineResponse20044DisplayCallFeedbackSurvey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**locked** | **bool** | Whether the senior administrator allows users to modify the current settings. | [optional] 
**locked_by** | **str** | Which level of administrator prohibits the modification of the current settings. | [optional] 
**feedback_type** | **int** | This field allows you to display feedback survey, &#x60;1&#x60; - display for every call, &#x60;2&#x60; - display when call quality issues are detected. Default &#x60;1&#x60;, if set with value &#x60;2&#x60;, need to set &#x60;feed_back_mos&#x60; or &#x60;feedback_duration&#x60;. | [optional] 
**feedback_mos** | [**InlineResponse20044DisplayCallFeedbackSurveyFeedbackMos**](InlineResponse20044DisplayCallFeedbackSurveyFeedbackMos.md) |  | [optional] 
**feedback_duration** | [**InlineResponse20044DisplayCallFeedbackSurveyFeedbackDuration**](InlineResponse20044DisplayCallFeedbackSurveyFeedbackDuration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

