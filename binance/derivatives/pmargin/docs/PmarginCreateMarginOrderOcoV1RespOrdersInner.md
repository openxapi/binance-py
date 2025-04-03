# PmarginCreateMarginOrderOcoV1RespOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_margin_order_oco_v1_resp_orders_inner import PmarginCreateMarginOrderOcoV1RespOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateMarginOrderOcoV1RespOrdersInner from a JSON string
pmargin_create_margin_order_oco_v1_resp_orders_inner_instance = PmarginCreateMarginOrderOcoV1RespOrdersInner.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateMarginOrderOcoV1RespOrdersInner.to_json())

# convert the object into a dict
pmargin_create_margin_order_oco_v1_resp_orders_inner_dict = pmargin_create_margin_order_oco_v1_resp_orders_inner_instance.to_dict()
# create an instance of PmarginCreateMarginOrderOcoV1RespOrdersInner from a dict
pmargin_create_margin_order_oco_v1_resp_orders_inner_from_dict = PmarginCreateMarginOrderOcoV1RespOrdersInner.from_dict(pmargin_create_margin_order_oco_v1_resp_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


