# OptionsDeleteBatchOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fee** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.options.models.options_delete_batch_orders_v1_resp_item import OptionsDeleteBatchOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsDeleteBatchOrdersV1RespItem from a JSON string
options_delete_batch_orders_v1_resp_item_instance = OptionsDeleteBatchOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsDeleteBatchOrdersV1RespItem.to_json())

# convert the object into a dict
options_delete_batch_orders_v1_resp_item_dict = options_delete_batch_orders_v1_resp_item_instance.to_dict()
# create an instance of OptionsDeleteBatchOrdersV1RespItem from a dict
options_delete_batch_orders_v1_resp_item_from_dict = OptionsDeleteBatchOrdersV1RespItem.from_dict(options_delete_batch_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


