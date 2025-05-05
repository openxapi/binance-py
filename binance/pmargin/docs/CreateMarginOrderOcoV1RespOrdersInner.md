# CreateMarginOrderOcoV1RespOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.create_margin_order_oco_v1_resp_orders_inner import CreateMarginOrderOcoV1RespOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginOrderOcoV1RespOrdersInner from a JSON string
create_margin_order_oco_v1_resp_orders_inner_instance = CreateMarginOrderOcoV1RespOrdersInner.from_json(json)
# print the JSON string representation of the object
print(CreateMarginOrderOcoV1RespOrdersInner.to_json())

# convert the object into a dict
create_margin_order_oco_v1_resp_orders_inner_dict = create_margin_order_oco_v1_resp_orders_inner_instance.to_dict()
# create an instance of CreateMarginOrderOcoV1RespOrdersInner from a dict
create_margin_order_oco_v1_resp_orders_inner_from_dict = CreateMarginOrderOcoV1RespOrdersInner.from_dict(create_margin_order_oco_v1_resp_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


