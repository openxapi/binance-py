# MarginGetMarginLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_names** | **List[str]** |  | [optional] 
**brackets** | [**List[MarginGetMarginLeverageBracketV1RespItemBracketsInner]**](MarginGetMarginLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**rank** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_leverage_bracket_v1_resp_item import MarginGetMarginLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginLeverageBracketV1RespItem from a JSON string
margin_get_margin_leverage_bracket_v1_resp_item_instance = MarginGetMarginLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginLeverageBracketV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_leverage_bracket_v1_resp_item_dict = margin_get_margin_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginLeverageBracketV1RespItem from a dict
margin_get_margin_leverage_bracket_v1_resp_item_from_dict = MarginGetMarginLeverageBracketV1RespItem.from_dict(margin_get_margin_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


