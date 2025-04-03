# SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner]**](SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner.md) |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data import SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData from a JSON string
subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data_instance = SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data_dict = subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData from a dict
subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data_from_dict = SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData.from_dict(subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


