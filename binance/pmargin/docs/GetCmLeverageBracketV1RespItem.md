# GetCmLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[GetCmLeverageBracketV1RespItemBracketsInner]**](GetCmLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_cm_leverage_bracket_v1_resp_item import GetCmLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCmLeverageBracketV1RespItem from a JSON string
get_cm_leverage_bracket_v1_resp_item_instance = GetCmLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetCmLeverageBracketV1RespItem.to_json())

# convert the object into a dict
get_cm_leverage_bracket_v1_resp_item_dict = get_cm_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of GetCmLeverageBracketV1RespItem from a dict
get_cm_leverage_bracket_v1_resp_item_from_dict = GetCmLeverageBracketV1RespItem.from_dict(get_cm_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


