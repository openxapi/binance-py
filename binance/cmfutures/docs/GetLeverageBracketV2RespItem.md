# GetLeverageBracketV2RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[GetLeverageBracketV1RespItemBracketsInner]**](GetLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**notional_coef** | **float** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_leverage_bracket_v2_resp_item import GetLeverageBracketV2RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetLeverageBracketV2RespItem from a JSON string
get_leverage_bracket_v2_resp_item_instance = GetLeverageBracketV2RespItem.from_json(json)
# print the JSON string representation of the object
print(GetLeverageBracketV2RespItem.to_json())

# convert the object into a dict
get_leverage_bracket_v2_resp_item_dict = get_leverage_bracket_v2_resp_item_instance.to_dict()
# create an instance of GetLeverageBracketV2RespItem from a dict
get_leverage_bracket_v2_resp_item_from_dict = GetLeverageBracketV2RespItem.from_dict(get_leverage_bracket_v2_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


