# GetMarginLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_names** | **List[str]** |  | [optional] 
**brackets** | [**List[GetMarginLeverageBracketV1RespItemBracketsInner]**](GetMarginLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**rank** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_leverage_bracket_v1_resp_item import GetMarginLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginLeverageBracketV1RespItem from a JSON string
get_margin_leverage_bracket_v1_resp_item_instance = GetMarginLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginLeverageBracketV1RespItem.to_json())

# convert the object into a dict
get_margin_leverage_bracket_v1_resp_item_dict = get_margin_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of GetMarginLeverageBracketV1RespItem from a dict
get_margin_leverage_bracket_v1_resp_item_from_dict = GetMarginLeverageBracketV1RespItem.from_dict(get_margin_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


