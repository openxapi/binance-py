# GetUmLeverageBracketV1RespItemBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket** | **int** |  | [optional] 
**cum** | **int** |  | [optional] 
**initial_leverage** | **int** |  | [optional] 
**maint_margin_ratio** | **float** |  | [optional] 
**notional_cap** | **int** |  | [optional] 
**notional_floor** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_leverage_bracket_v1_resp_item_brackets_inner import GetUmLeverageBracketV1RespItemBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmLeverageBracketV1RespItemBracketsInner from a JSON string
get_um_leverage_bracket_v1_resp_item_brackets_inner_instance = GetUmLeverageBracketV1RespItemBracketsInner.from_json(json)
# print the JSON string representation of the object
print(GetUmLeverageBracketV1RespItemBracketsInner.to_json())

# convert the object into a dict
get_um_leverage_bracket_v1_resp_item_brackets_inner_dict = get_um_leverage_bracket_v1_resp_item_brackets_inner_instance.to_dict()
# create an instance of GetUmLeverageBracketV1RespItemBracketsInner from a dict
get_um_leverage_bracket_v1_resp_item_brackets_inner_from_dict = GetUmLeverageBracketV1RespItemBracketsInner.from_dict(get_um_leverage_bracket_v1_resp_item_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


