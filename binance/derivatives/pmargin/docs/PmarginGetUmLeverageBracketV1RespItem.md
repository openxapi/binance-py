# PmarginGetUmLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[PmarginGetUmLeverageBracketV1RespItemBracketsInner]**](PmarginGetUmLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**notional_coef** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_leverage_bracket_v1_resp_item import PmarginGetUmLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmLeverageBracketV1RespItem from a JSON string
pmargin_get_um_leverage_bracket_v1_resp_item_instance = PmarginGetUmLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmLeverageBracketV1RespItem.to_json())

# convert the object into a dict
pmargin_get_um_leverage_bracket_v1_resp_item_dict = pmargin_get_um_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetUmLeverageBracketV1RespItem from a dict
pmargin_get_um_leverage_bracket_v1_resp_item_from_dict = PmarginGetUmLeverageBracketV1RespItem.from_dict(pmargin_get_um_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


