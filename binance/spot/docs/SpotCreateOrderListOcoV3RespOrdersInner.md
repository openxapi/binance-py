# SpotCreateOrderListOcoV3RespOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_list_oco_v3_resp_orders_inner import SpotCreateOrderListOcoV3RespOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderListOcoV3RespOrdersInner from a JSON string
spot_create_order_list_oco_v3_resp_orders_inner_instance = SpotCreateOrderListOcoV3RespOrdersInner.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderListOcoV3RespOrdersInner.to_json())

# convert the object into a dict
spot_create_order_list_oco_v3_resp_orders_inner_dict = spot_create_order_list_oco_v3_resp_orders_inner_instance.to_dict()
# create an instance of SpotCreateOrderListOcoV3RespOrdersInner from a dict
spot_create_order_list_oco_v3_resp_orders_inner_from_dict = SpotCreateOrderListOcoV3RespOrdersInner.from_dict(spot_create_order_list_oco_v3_resp_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


