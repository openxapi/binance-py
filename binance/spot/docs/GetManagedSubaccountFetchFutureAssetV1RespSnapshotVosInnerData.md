# GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataAssetsInner]**](GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataAssetsInner.md) |  | [optional] 
**position** | [**List[GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataPositionInner]**](GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerDataPositionInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data import GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData from a JSON string
get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_instance = GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData.to_json())

# convert the object into a dict
get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_dict = get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_instance.to_dict()
# create an instance of GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData from a dict
get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_from_dict = GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInnerData.from_dict(get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


