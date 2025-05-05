# GetManagedSubaccountAccountSnapshotV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**snapshot_vos** | [**List[GetAccountSnapshotV1RespSnapshotVosInner]**](GetAccountSnapshotV1RespSnapshotVosInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_account_snapshot_v1_resp import GetManagedSubaccountAccountSnapshotV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountAccountSnapshotV1Resp from a JSON string
get_managed_subaccount_account_snapshot_v1_resp_instance = GetManagedSubaccountAccountSnapshotV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountAccountSnapshotV1Resp.to_json())

# convert the object into a dict
get_managed_subaccount_account_snapshot_v1_resp_dict = get_managed_subaccount_account_snapshot_v1_resp_instance.to_dict()
# create an instance of GetManagedSubaccountAccountSnapshotV1Resp from a dict
get_managed_subaccount_account_snapshot_v1_resp_from_dict = GetManagedSubaccountAccountSnapshotV1Resp.from_dict(get_managed_subaccount_account_snapshot_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


