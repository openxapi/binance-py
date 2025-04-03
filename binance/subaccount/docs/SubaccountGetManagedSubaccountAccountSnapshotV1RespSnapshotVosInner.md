# SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData**](SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInnerData.md) |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner import SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner from a JSON string
subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_instance = SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_dict = subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner from a dict
subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_from_dict = SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner.from_dict(subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


