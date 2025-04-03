# WalletGetAssetCustodyTransferHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[WalletGetAssetCustodyTransferHistoryV1RespRowsInner]**](WalletGetAssetCustodyTransferHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_custody_transfer_history_v1_resp import WalletGetAssetCustodyTransferHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetCustodyTransferHistoryV1Resp from a JSON string
wallet_get_asset_custody_transfer_history_v1_resp_instance = WalletGetAssetCustodyTransferHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetCustodyTransferHistoryV1Resp.to_json())

# convert the object into a dict
wallet_get_asset_custody_transfer_history_v1_resp_dict = wallet_get_asset_custody_transfer_history_v1_resp_instance.to_dict()
# create an instance of WalletGetAssetCustodyTransferHistoryV1Resp from a dict
wallet_get_asset_custody_transfer_history_v1_resp_from_dict = WalletGetAssetCustodyTransferHistoryV1Resp.from_dict(wallet_get_asset_custody_transfer_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


