# GetLeverageBracketV1RespItemBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket** | **int** |  | [optional] 
**cum** | **int** |  | [optional] 
**initial_leverage** | **int** |  | [optional] 
**maint_margin_ratio** | **float** |  | [optional] 
**qty_cap** | **int** |  | [optional] 
**qtyl_floor** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_leverage_bracket_v1_resp_item_brackets_inner import GetLeverageBracketV1RespItemBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLeverageBracketV1RespItemBracketsInner from a JSON string
get_leverage_bracket_v1_resp_item_brackets_inner_instance = GetLeverageBracketV1RespItemBracketsInner.from_json(json)
# print the JSON string representation of the object
print(GetLeverageBracketV1RespItemBracketsInner.to_json())

# convert the object into a dict
get_leverage_bracket_v1_resp_item_brackets_inner_dict = get_leverage_bracket_v1_resp_item_brackets_inner_instance.to_dict()
# create an instance of GetLeverageBracketV1RespItemBracketsInner from a dict
get_leverage_bracket_v1_resp_item_brackets_inner_from_dict = GetLeverageBracketV1RespItemBracketsInner.from_dict(get_leverage_bracket_v1_resp_item_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


