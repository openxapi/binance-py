# CmfuturesGetLeverageBracketV1RespItemBracketsInner


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
from binance.derivatives.cmfutures.models.cmfutures_get_leverage_bracket_v1_resp_item_brackets_inner import CmfuturesGetLeverageBracketV1RespItemBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetLeverageBracketV1RespItemBracketsInner from a JSON string
cmfutures_get_leverage_bracket_v1_resp_item_brackets_inner_instance = CmfuturesGetLeverageBracketV1RespItemBracketsInner.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetLeverageBracketV1RespItemBracketsInner.to_json())

# convert the object into a dict
cmfutures_get_leverage_bracket_v1_resp_item_brackets_inner_dict = cmfutures_get_leverage_bracket_v1_resp_item_brackets_inner_instance.to_dict()
# create an instance of CmfuturesGetLeverageBracketV1RespItemBracketsInner from a dict
cmfutures_get_leverage_bracket_v1_resp_item_brackets_inner_from_dict = CmfuturesGetLeverageBracketV1RespItemBracketsInner.from_dict(cmfutures_get_leverage_bracket_v1_resp_item_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


