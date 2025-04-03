# OptionsDeleteBatchOrdersV1RespInner


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
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_delete_batch_orders_v1_resp_inner import OptionsDeleteBatchOrdersV1RespInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsDeleteBatchOrdersV1RespInner from a JSON string
options_delete_batch_orders_v1_resp_inner_instance = OptionsDeleteBatchOrdersV1RespInner.from_json(json)
# print the JSON string representation of the object
print(OptionsDeleteBatchOrdersV1RespInner.to_json())

# convert the object into a dict
options_delete_batch_orders_v1_resp_inner_dict = options_delete_batch_orders_v1_resp_inner_instance.to_dict()
# create an instance of OptionsDeleteBatchOrdersV1RespInner from a dict
options_delete_batch_orders_v1_resp_inner_from_dict = OptionsDeleteBatchOrdersV1RespInner.from_dict(options_delete_batch_orders_v1_resp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


