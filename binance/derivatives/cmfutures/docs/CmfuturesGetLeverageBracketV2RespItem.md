# CmfuturesGetLeverageBracketV2RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[CmfuturesGetLeverageBracketV1RespItemBracketsInner]**](CmfuturesGetLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**notional_coef** | **float** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_leverage_bracket_v2_resp_item import CmfuturesGetLeverageBracketV2RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetLeverageBracketV2RespItem from a JSON string
cmfutures_get_leverage_bracket_v2_resp_item_instance = CmfuturesGetLeverageBracketV2RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetLeverageBracketV2RespItem.to_json())

# convert the object into a dict
cmfutures_get_leverage_bracket_v2_resp_item_dict = cmfutures_get_leverage_bracket_v2_resp_item_instance.to_dict()
# create an instance of CmfuturesGetLeverageBracketV2RespItem from a dict
cmfutures_get_leverage_bracket_v2_resp_item_from_dict = CmfuturesGetLeverageBracketV2RespItem.from_dict(cmfutures_get_leverage_bracket_v2_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


