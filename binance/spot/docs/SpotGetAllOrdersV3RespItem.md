# SpotGetAllOrdersV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**iceberg_qty** | **str** |  | [optional] 
**is_working** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_quote_order_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**working_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_all_orders_v3_resp_item import SpotGetAllOrdersV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetAllOrdersV3RespItem from a JSON string
spot_get_all_orders_v3_resp_item_instance = SpotGetAllOrdersV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetAllOrdersV3RespItem.to_json())

# convert the object into a dict
spot_get_all_orders_v3_resp_item_dict = spot_get_all_orders_v3_resp_item_instance.to_dict()
# create an instance of SpotGetAllOrdersV3RespItem from a dict
spot_get_all_orders_v3_resp_item_from_dict = SpotGetAllOrdersV3RespItem.from_dict(spot_get_all_orders_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


