# GetLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[GetLeverageBracketV1RespItemBracketsInner]**](GetLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**pair** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_leverage_bracket_v1_resp_item import GetLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetLeverageBracketV1RespItem from a JSON string
get_leverage_bracket_v1_resp_item_instance = GetLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetLeverageBracketV1RespItem.to_json())

# convert the object into a dict
get_leverage_bracket_v1_resp_item_dict = get_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of GetLeverageBracketV1RespItem from a dict
get_leverage_bracket_v1_resp_item_from_dict = GetLeverageBracketV1RespItem.from_dict(get_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


