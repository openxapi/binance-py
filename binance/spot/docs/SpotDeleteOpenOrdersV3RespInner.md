# SpotDeleteOpenOrdersV3RespInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_reports** | [**List[SpotDeleteOpenOrdersV3RespOrderItem]**](SpotDeleteOpenOrdersV3RespOrderItem.md) |  | [optional] 
**orders** | [**List[SpotCreateOrderListOcoV3RespOrdersInner]**](SpotCreateOrderListOcoV3RespOrdersInner.md) |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_delete_open_orders_v3_resp_inner import SpotDeleteOpenOrdersV3RespInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotDeleteOpenOrdersV3RespInner from a JSON string
spot_delete_open_orders_v3_resp_inner_instance = SpotDeleteOpenOrdersV3RespInner.from_json(json)
# print the JSON string representation of the object
print(SpotDeleteOpenOrdersV3RespInner.to_json())

# convert the object into a dict
spot_delete_open_orders_v3_resp_inner_dict = spot_delete_open_orders_v3_resp_inner_instance.to_dict()
# create an instance of SpotDeleteOpenOrdersV3RespInner from a dict
spot_delete_open_orders_v3_resp_inner_from_dict = SpotDeleteOpenOrdersV3RespInner.from_dict(spot_delete_open_orders_v3_resp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


