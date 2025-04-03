# MarginCreateMarginOrderOcoV1RespOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_create_margin_order_oco_v1_resp_orders_inner import MarginCreateMarginOrderOcoV1RespOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginCreateMarginOrderOcoV1RespOrdersInner from a JSON string
margin_create_margin_order_oco_v1_resp_orders_inner_instance = MarginCreateMarginOrderOcoV1RespOrdersInner.from_json(json)
# print the JSON string representation of the object
print(MarginCreateMarginOrderOcoV1RespOrdersInner.to_json())

# convert the object into a dict
margin_create_margin_order_oco_v1_resp_orders_inner_dict = margin_create_margin_order_oco_v1_resp_orders_inner_instance.to_dict()
# create an instance of MarginCreateMarginOrderOcoV1RespOrdersInner from a dict
margin_create_margin_order_oco_v1_resp_orders_inner_from_dict = MarginCreateMarginOrderOcoV1RespOrdersInner.from_dict(margin_create_margin_order_oco_v1_resp_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


