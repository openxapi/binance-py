# CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] [default to '']
**price** | **str** |  | [optional] [default to '']
**quantity** | **str** |  | [optional] [default to '']
**recv_window** | **int** |  | [optional] 
**side** | **str** |  | [default to '']
**symbol** | **str** |  | [default to '']
**timestamp** | **int** |  | 

## Example

```python
from binance.cmfutures.models.cmfutures_update_batch_orders_v1_req_batch_orders_item import CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem from a JSON string
cmfutures_update_batch_orders_v1_req_batch_orders_item_instance = CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.to_json())

# convert the object into a dict
cmfutures_update_batch_orders_v1_req_batch_orders_item_dict = cmfutures_update_batch_orders_v1_req_batch_orders_item_instance.to_dict()
# create an instance of CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem from a dict
cmfutures_update_batch_orders_v1_req_batch_orders_item_from_dict = CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.from_dict(cmfutures_update_batch_orders_v1_req_batch_orders_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


