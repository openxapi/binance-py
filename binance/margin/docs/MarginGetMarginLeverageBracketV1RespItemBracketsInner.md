# MarginGetMarginLeverageBracketV1RespItemBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fast_num** | **int** |  | [optional] 
**initial_margin_rate** | **float** |  | [optional] 
**leverage** | **int** |  | [optional] 
**maintenance_margin_rate** | **float** |  | [optional] 
**max_debt** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_leverage_bracket_v1_resp_item_brackets_inner import MarginGetMarginLeverageBracketV1RespItemBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginLeverageBracketV1RespItemBracketsInner from a JSON string
margin_get_margin_leverage_bracket_v1_resp_item_brackets_inner_instance = MarginGetMarginLeverageBracketV1RespItemBracketsInner.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginLeverageBracketV1RespItemBracketsInner.to_json())

# convert the object into a dict
margin_get_margin_leverage_bracket_v1_resp_item_brackets_inner_dict = margin_get_margin_leverage_bracket_v1_resp_item_brackets_inner_instance.to_dict()
# create an instance of MarginGetMarginLeverageBracketV1RespItemBracketsInner from a dict
margin_get_margin_leverage_bracket_v1_resp_item_brackets_inner_from_dict = MarginGetMarginLeverageBracketV1RespItemBracketsInner.from_dict(margin_get_margin_leverage_bracket_v1_resp_item_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


