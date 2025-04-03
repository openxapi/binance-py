# PmarginCreateMarginOrderV1RespFillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_margin_order_v1_resp_fills_inner import PmarginCreateMarginOrderV1RespFillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateMarginOrderV1RespFillsInner from a JSON string
pmargin_create_margin_order_v1_resp_fills_inner_instance = PmarginCreateMarginOrderV1RespFillsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateMarginOrderV1RespFillsInner.to_json())

# convert the object into a dict
pmargin_create_margin_order_v1_resp_fills_inner_dict = pmargin_create_margin_order_v1_resp_fills_inner_instance.to_dict()
# create an instance of PmarginCreateMarginOrderV1RespFillsInner from a dict
pmargin_create_margin_order_v1_resp_fills_inner_from_dict = PmarginCreateMarginOrderV1RespFillsInner.from_dict(pmargin_create_margin_order_v1_resp_fills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


