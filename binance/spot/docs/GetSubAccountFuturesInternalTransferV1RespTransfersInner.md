# GetSubAccountFuturesInternalTransferV1RespTransfersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**to** | **str** |  | [optional] 
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_internal_transfer_v1_resp_transfers_inner import GetSubAccountFuturesInternalTransferV1RespTransfersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesInternalTransferV1RespTransfersInner from a JSON string
get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_instance = GetSubAccountFuturesInternalTransferV1RespTransfersInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesInternalTransferV1RespTransfersInner.to_json())

# convert the object into a dict
get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_dict = get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_instance.to_dict()
# create an instance of GetSubAccountFuturesInternalTransferV1RespTransfersInner from a dict
get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_from_dict = GetSubAccountFuturesInternalTransferV1RespTransfersInner.from_dict(get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


