# SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataAssetsInner]**](SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataAssetsInner.md) |  | [optional] 
**position** | [**List[SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataPositionInner]**](SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataPositionInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data import SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData from a JSON string
subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_instance = SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_dict = subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData from a dict
subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_from_dict = SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData.from_dict(subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


