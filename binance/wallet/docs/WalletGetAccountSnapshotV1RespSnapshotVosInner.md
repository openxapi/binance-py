# WalletGetAccountSnapshotV1RespSnapshotVosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WalletGetAccountSnapshotV1RespSnapshotVosInnerData**](WalletGetAccountSnapshotV1RespSnapshotVosInnerData.md) |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_account_snapshot_v1_resp_snapshot_vos_inner import WalletGetAccountSnapshotV1RespSnapshotVosInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAccountSnapshotV1RespSnapshotVosInner from a JSON string
wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_instance = WalletGetAccountSnapshotV1RespSnapshotVosInner.from_json(json)
# print the JSON string representation of the object
print(WalletGetAccountSnapshotV1RespSnapshotVosInner.to_json())

# convert the object into a dict
wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_dict = wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_instance.to_dict()
# create an instance of WalletGetAccountSnapshotV1RespSnapshotVosInner from a dict
wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_from_dict = WalletGetAccountSnapshotV1RespSnapshotVosInner.from_dict(wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


