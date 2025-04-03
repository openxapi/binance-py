# OptionsCreateBatchOrdersV1ReqOrdersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] [default to '']
**is_mmp** | **bool** |  | [optional] 
**new_order_resp_type** | **str** |  | [optional] [default to '']
**post_only** | **bool** |  | [optional] [default to False]
**price** | **str** |  | [optional] [default to '']
**quantity** | **str** |  | [default to '']
**reduce_only** | **bool** |  | [optional] [default to False]
**side** | **str** |  | [default to '']
**symbol** | **str** |  | [default to '']
**time_in_force** | **str** |  | [optional] [default to '']
**type** | **str** |  | [default to '']

## Example

```python
from binance.derivatives.options.models.options_create_batch_orders_v1_req_orders_item import OptionsCreateBatchOrdersV1ReqOrdersItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCreateBatchOrdersV1ReqOrdersItem from a JSON string
options_create_batch_orders_v1_req_orders_item_instance = OptionsCreateBatchOrdersV1ReqOrdersItem.from_json(json)
# print the JSON string representation of the object
print(OptionsCreateBatchOrdersV1ReqOrdersItem.to_json())

# convert the object into a dict
options_create_batch_orders_v1_req_orders_item_dict = options_create_batch_orders_v1_req_orders_item_instance.to_dict()
# create an instance of OptionsCreateBatchOrdersV1ReqOrdersItem from a dict
options_create_batch_orders_v1_req_orders_item_from_dict = OptionsCreateBatchOrdersV1ReqOrdersItem.from_dict(options_create_batch_orders_v1_req_orders_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


