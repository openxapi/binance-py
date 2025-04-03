# PmarginGetUmLeverageBracketV1RespItemBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket** | **int** |  | [optional] 
**cum** | **int** |  | [optional] 
**initial_leverage** | **int** |  | [optional] 
**maint_margin_ratio** | **float** |  | [optional] 
**notional_cap** | **int** |  | [optional] 
**notional_floor** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_leverage_bracket_v1_resp_item_brackets_inner import PmarginGetUmLeverageBracketV1RespItemBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmLeverageBracketV1RespItemBracketsInner from a JSON string
pmargin_get_um_leverage_bracket_v1_resp_item_brackets_inner_instance = PmarginGetUmLeverageBracketV1RespItemBracketsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmLeverageBracketV1RespItemBracketsInner.to_json())

# convert the object into a dict
pmargin_get_um_leverage_bracket_v1_resp_item_brackets_inner_dict = pmargin_get_um_leverage_bracket_v1_resp_item_brackets_inner_instance.to_dict()
# create an instance of PmarginGetUmLeverageBracketV1RespItemBracketsInner from a dict
pmargin_get_um_leverage_bracket_v1_resp_item_brackets_inner_from_dict = PmarginGetUmLeverageBracketV1RespItemBracketsInner.from_dict(pmargin_get_um_leverage_bracket_v1_resp_item_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


