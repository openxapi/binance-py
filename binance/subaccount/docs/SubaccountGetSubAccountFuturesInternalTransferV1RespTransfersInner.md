# SubaccountGetSubAccountFuturesInternalTransferV1RespTransfersInner


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
from binance.subaccount.models.subaccount_get_sub_account_futures_internal_transfer_v1_resp_transfers_inner import SubaccountGetSubAccountFuturesInternalTransferV1RespTransfersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountFuturesInternalTransferV1RespTransfersInner from a JSON string
subaccount_get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_instance = SubaccountGetSubAccountFuturesInternalTransferV1RespTransfersInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountFuturesInternalTransferV1RespTransfersInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_dict = subaccount_get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountFuturesInternalTransferV1RespTransfersInner from a dict
subaccount_get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_from_dict = SubaccountGetSubAccountFuturesInternalTransferV1RespTransfersInner.from_dict(subaccount_get_sub_account_futures_internal_transfer_v1_resp_transfers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


