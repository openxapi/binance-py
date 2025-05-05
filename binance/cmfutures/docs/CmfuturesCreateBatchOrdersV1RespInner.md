# CmfuturesCreateBatchOrdersV1RespInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_price** | **str** |  | [optional] 
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**cum_base** | **str** |  | [optional] 
**cum_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_type** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_match** | **str** |  | [optional] 
**price_protect** | **bool** |  | [optional] 
**price_rate** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**working_type** | **str** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.cmfutures_create_batch_orders_v1_resp_inner import CmfuturesCreateBatchOrdersV1RespInner

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesCreateBatchOrdersV1RespInner from a JSON string
cmfutures_create_batch_orders_v1_resp_inner_instance = CmfuturesCreateBatchOrdersV1RespInner.from_json(json)
# print the JSON string representation of the object
print(CmfuturesCreateBatchOrdersV1RespInner.to_json())

# convert the object into a dict
cmfutures_create_batch_orders_v1_resp_inner_dict = cmfutures_create_batch_orders_v1_resp_inner_instance.to_dict()
# create an instance of CmfuturesCreateBatchOrdersV1RespInner from a dict
cmfutures_create_batch_orders_v1_resp_inner_from_dict = CmfuturesCreateBatchOrdersV1RespInner.from_dict(cmfutures_create_batch_orders_v1_resp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


