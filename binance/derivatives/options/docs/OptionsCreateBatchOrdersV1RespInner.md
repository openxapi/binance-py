# OptionsCreateBatchOrdersV1RespInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**mmp** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**post_only** | **bool** |  | [optional] 
**price** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_create_batch_orders_v1_resp_inner import OptionsCreateBatchOrdersV1RespInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCreateBatchOrdersV1RespInner from a JSON string
options_create_batch_orders_v1_resp_inner_instance = OptionsCreateBatchOrdersV1RespInner.from_json(json)
# print the JSON string representation of the object
print(OptionsCreateBatchOrdersV1RespInner.to_json())

# convert the object into a dict
options_create_batch_orders_v1_resp_inner_dict = options_create_batch_orders_v1_resp_inner_instance.to_dict()
# create an instance of OptionsCreateBatchOrdersV1RespInner from a dict
options_create_batch_orders_v1_resp_inner_from_dict = OptionsCreateBatchOrdersV1RespInner.from_dict(options_create_batch_orders_v1_resp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


