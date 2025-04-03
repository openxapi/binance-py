# WalletGetAssetCustodyTransferHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**client_tran_id** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**transfer_type** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_custody_transfer_history_v1_resp_rows_inner import WalletGetAssetCustodyTransferHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetCustodyTransferHistoryV1RespRowsInner from a JSON string
wallet_get_asset_custody_transfer_history_v1_resp_rows_inner_instance = WalletGetAssetCustodyTransferHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetCustodyTransferHistoryV1RespRowsInner.to_json())

# convert the object into a dict
wallet_get_asset_custody_transfer_history_v1_resp_rows_inner_dict = wallet_get_asset_custody_transfer_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of WalletGetAssetCustodyTransferHistoryV1RespRowsInner from a dict
wallet_get_asset_custody_transfer_history_v1_resp_rows_inner_from_dict = WalletGetAssetCustodyTransferHistoryV1RespRowsInner.from_dict(wallet_get_asset_custody_transfer_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


