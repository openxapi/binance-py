# GetMarginLeverageBracketV1RespItemBracketsInner


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
from binance.spot.models.get_margin_leverage_bracket_v1_resp_item_brackets_inner import GetMarginLeverageBracketV1RespItemBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginLeverageBracketV1RespItemBracketsInner from a JSON string
get_margin_leverage_bracket_v1_resp_item_brackets_inner_instance = GetMarginLeverageBracketV1RespItemBracketsInner.from_json(json)
# print the JSON string representation of the object
print(GetMarginLeverageBracketV1RespItemBracketsInner.to_json())

# convert the object into a dict
get_margin_leverage_bracket_v1_resp_item_brackets_inner_dict = get_margin_leverage_bracket_v1_resp_item_brackets_inner_instance.to_dict()
# create an instance of GetMarginLeverageBracketV1RespItemBracketsInner from a dict
get_margin_leverage_bracket_v1_resp_item_brackets_inner_from_dict = GetMarginLeverageBracketV1RespItemBracketsInner.from_dict(get_margin_leverage_bracket_v1_resp_item_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


