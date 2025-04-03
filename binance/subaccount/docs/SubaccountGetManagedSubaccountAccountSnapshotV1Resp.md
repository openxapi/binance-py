# SubaccountGetManagedSubaccountAccountSnapshotV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**snapshot_vos** | [**List[SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner]**](SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_account_snapshot_v1_resp import SubaccountGetManagedSubaccountAccountSnapshotV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountAccountSnapshotV1Resp from a JSON string
subaccount_get_managed_subaccount_account_snapshot_v1_resp_instance = SubaccountGetManagedSubaccountAccountSnapshotV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountAccountSnapshotV1Resp.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_account_snapshot_v1_resp_dict = subaccount_get_managed_subaccount_account_snapshot_v1_resp_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountAccountSnapshotV1Resp from a dict
subaccount_get_managed_subaccount_account_snapshot_v1_resp_from_dict = SubaccountGetManagedSubaccountAccountSnapshotV1Resp.from_dict(subaccount_get_managed_subaccount_account_snapshot_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


