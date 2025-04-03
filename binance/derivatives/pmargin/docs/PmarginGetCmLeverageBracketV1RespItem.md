# PmarginGetCmLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[PmarginGetCmLeverageBracketV1RespItemBracketsInner]**](PmarginGetCmLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_cm_leverage_bracket_v1_resp_item import PmarginGetCmLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmLeverageBracketV1RespItem from a JSON string
pmargin_get_cm_leverage_bracket_v1_resp_item_instance = PmarginGetCmLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmLeverageBracketV1RespItem.to_json())

# convert the object into a dict
pmargin_get_cm_leverage_bracket_v1_resp_item_dict = pmargin_get_cm_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetCmLeverageBracketV1RespItem from a dict
pmargin_get_cm_leverage_bracket_v1_resp_item_from_dict = PmarginGetCmLeverageBracketV1RespItem.from_dict(pmargin_get_cm_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


