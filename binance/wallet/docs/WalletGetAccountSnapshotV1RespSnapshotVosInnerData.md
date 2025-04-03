# WalletGetAccountSnapshotV1RespSnapshotVosInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[WalletGetAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner]**](WalletGetAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner.md) |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data import WalletGetAccountSnapshotV1RespSnapshotVosInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAccountSnapshotV1RespSnapshotVosInnerData from a JSON string
wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data_instance = WalletGetAccountSnapshotV1RespSnapshotVosInnerData.from_json(json)
# print the JSON string representation of the object
print(WalletGetAccountSnapshotV1RespSnapshotVosInnerData.to_json())

# convert the object into a dict
wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data_dict = wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data_instance.to_dict()
# create an instance of WalletGetAccountSnapshotV1RespSnapshotVosInnerData from a dict
wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data_from_dict = WalletGetAccountSnapshotV1RespSnapshotVosInnerData.from_dict(wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


