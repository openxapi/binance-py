# CmfuturesCreateBatchOrderV1ReqBatchOrdersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_price** | **str** |  | [optional] [default to '']
**callback_rate** | **str** |  | [optional] [default to '']
**close_position** | **str** |  | [optional] [default to '']
**new_client_order_id** | **str** |  | [optional] [default to '']
**new_order_resp_type** | **str** |  | [optional] [default to '']
**position_side** | **str** |  | [optional] [default to '']
**price** | **str** |  | [optional] [default to '']
**price_match** | **str** |  | [optional] [default to '']
**price_protect** | **str** |  | [optional] [default to '']
**quantity** | **str** |  | [optional] [default to '']
**reduce_only** | **str** |  | [optional] [default to '']
**self_trade_prevention_mode** | **str** |  | [optional] [default to '']
**side** | **str** |  | [default to '']
**stop_price** | **str** |  | [optional] [default to '']
**symbol** | **str** |  | [default to '']
**time_in_force** | **str** |  | [optional] [default to '']
**type** | **str** |  | [default to '']
**working_type** | **str** |  | [optional] [default to '']

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_create_batch_order_v1_req_batch_orders_item import CmfuturesCreateBatchOrderV1ReqBatchOrdersItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesCreateBatchOrderV1ReqBatchOrdersItem from a JSON string
cmfutures_create_batch_order_v1_req_batch_orders_item_instance = CmfuturesCreateBatchOrderV1ReqBatchOrdersItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesCreateBatchOrderV1ReqBatchOrdersItem.to_json())

# convert the object into a dict
cmfutures_create_batch_order_v1_req_batch_orders_item_dict = cmfutures_create_batch_order_v1_req_batch_orders_item_instance.to_dict()
# create an instance of CmfuturesCreateBatchOrderV1ReqBatchOrdersItem from a dict
cmfutures_create_batch_order_v1_req_batch_orders_item_from_dict = CmfuturesCreateBatchOrderV1ReqBatchOrdersItem.from_dict(cmfutures_create_batch_order_v1_req_batch_orders_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


