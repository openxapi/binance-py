# GetManagedSubaccountFetchFutureAssetV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**snapshot_vos** | [**List[GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner]**](GetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_fetch_future_asset_v1_resp import GetManagedSubaccountFetchFutureAssetV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountFetchFutureAssetV1Resp from a JSON string
get_managed_subaccount_fetch_future_asset_v1_resp_instance = GetManagedSubaccountFetchFutureAssetV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountFetchFutureAssetV1Resp.to_json())

# convert the object into a dict
get_managed_subaccount_fetch_future_asset_v1_resp_dict = get_managed_subaccount_fetch_future_asset_v1_resp_instance.to_dict()
# create an instance of GetManagedSubaccountFetchFutureAssetV1Resp from a dict
get_managed_subaccount_fetch_future_asset_v1_resp_from_dict = GetManagedSubaccountFetchFutureAssetV1Resp.from_dict(get_managed_subaccount_fetch_future_asset_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


