# DeleteMarginOpenOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
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
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.delete_margin_open_orders_v1_resp_item import DeleteMarginOpenOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMarginOpenOrdersV1RespItem from a JSON string
delete_margin_open_orders_v1_resp_item_instance = DeleteMarginOpenOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(DeleteMarginOpenOrdersV1RespItem.to_json())

# convert the object into a dict
delete_margin_open_orders_v1_resp_item_dict = delete_margin_open_orders_v1_resp_item_instance.to_dict()
# create an instance of DeleteMarginOpenOrdersV1RespItem from a dict
delete_margin_open_orders_v1_resp_item_from_dict = DeleteMarginOpenOrdersV1RespItem.from_dict(delete_margin_open_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


