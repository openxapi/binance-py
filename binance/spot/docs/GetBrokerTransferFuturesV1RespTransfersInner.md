# GetBrokerTransferFuturesV1RespTransfersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**client_tran_id** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**to** | **str** |  | [optional] 
**tran_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_transfer_futures_v1_resp_transfers_inner import GetBrokerTransferFuturesV1RespTransfersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerTransferFuturesV1RespTransfersInner from a JSON string
get_broker_transfer_futures_v1_resp_transfers_inner_instance = GetBrokerTransferFuturesV1RespTransfersInner.from_json(json)
# print the JSON string representation of the object
print(GetBrokerTransferFuturesV1RespTransfersInner.to_json())

# convert the object into a dict
get_broker_transfer_futures_v1_resp_transfers_inner_dict = get_broker_transfer_futures_v1_resp_transfers_inner_instance.to_dict()
# create an instance of GetBrokerTransferFuturesV1RespTransfersInner from a dict
get_broker_transfer_futures_v1_resp_transfers_inner_from_dict = GetBrokerTransferFuturesV1RespTransfersInner.from_dict(get_broker_transfer_futures_v1_resp_transfers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


