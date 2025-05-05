# GetUmLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[GetUmLeverageBracketV1RespItemBracketsInner]**](GetUmLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**notional_coef** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_leverage_bracket_v1_resp_item import GetUmLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmLeverageBracketV1RespItem from a JSON string
get_um_leverage_bracket_v1_resp_item_instance = GetUmLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetUmLeverageBracketV1RespItem.to_json())

# convert the object into a dict
get_um_leverage_bracket_v1_resp_item_dict = get_um_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of GetUmLeverageBracketV1RespItem from a dict
get_um_leverage_bracket_v1_resp_item_from_dict = GetUmLeverageBracketV1RespItem.from_dict(get_um_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


