# PmarginGetCmLeverageBracketV1RespItemBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket** | **int** |  | [optional] 
**cum** | **int** |  | [optional] 
**initial_leverage** | **int** |  | [optional] 
**maint_margin_ratio** | **float** |  | [optional] 
**qty_cap** | **int** |  | [optional] 
**qty_floor** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_cm_leverage_bracket_v1_resp_item_brackets_inner import PmarginGetCmLeverageBracketV1RespItemBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmLeverageBracketV1RespItemBracketsInner from a JSON string
pmargin_get_cm_leverage_bracket_v1_resp_item_brackets_inner_instance = PmarginGetCmLeverageBracketV1RespItemBracketsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmLeverageBracketV1RespItemBracketsInner.to_json())

# convert the object into a dict
pmargin_get_cm_leverage_bracket_v1_resp_item_brackets_inner_dict = pmargin_get_cm_leverage_bracket_v1_resp_item_brackets_inner_instance.to_dict()
# create an instance of PmarginGetCmLeverageBracketV1RespItemBracketsInner from a dict
pmargin_get_cm_leverage_bracket_v1_resp_item_brackets_inner_from_dict = PmarginGetCmLeverageBracketV1RespItemBracketsInner.from_dict(pmargin_get_cm_leverage_bracket_v1_resp_item_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


