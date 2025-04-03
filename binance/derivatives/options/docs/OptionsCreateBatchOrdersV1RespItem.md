# OptionsCreateBatchOrdersV1RespItem


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

## Example

```python
from binance.derivatives.options.models.options_create_batch_orders_v1_resp_item import OptionsCreateBatchOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCreateBatchOrdersV1RespItem from a JSON string
options_create_batch_orders_v1_resp_item_instance = OptionsCreateBatchOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsCreateBatchOrdersV1RespItem.to_json())

# convert the object into a dict
options_create_batch_orders_v1_resp_item_dict = options_create_batch_orders_v1_resp_item_instance.to_dict()
# create an instance of OptionsCreateBatchOrdersV1RespItem from a dict
options_create_batch_orders_v1_resp_item_from_dict = OptionsCreateBatchOrdersV1RespItem.from_dict(options_create_batch_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


