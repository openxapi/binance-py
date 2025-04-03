# UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] [default to '']
**price** | **str** |  | [default to '']
**price_match** | **str** |  | [optional] [default to '']
**quantity** | **str** |  | [default to '']
**side** | **str** |  | [default to '']
**symbol** | **str** |  | [default to '']

## Example

```python
from binance.derivatives.umfutures.models.umfutures_update_batch_orders_v1_req_batch_orders_item import UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem from a JSON string
umfutures_update_batch_orders_v1_req_batch_orders_item_instance = UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.to_json())

# convert the object into a dict
umfutures_update_batch_orders_v1_req_batch_orders_item_dict = umfutures_update_batch_orders_v1_req_batch_orders_item_instance.to_dict()
# create an instance of UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem from a dict
umfutures_update_batch_orders_v1_req_batch_orders_item_from_dict = UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.from_dict(umfutures_update_batch_orders_v1_req_batch_orders_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


