# SubaccountGetManagedSubaccountFetchFutureAssetV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**snapshot_vos** | [**List[SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner]**](SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_fetch_future_asset_v1_resp import SubaccountGetManagedSubaccountFetchFutureAssetV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountFetchFutureAssetV1Resp from a JSON string
subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_instance = SubaccountGetManagedSubaccountFetchFutureAssetV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountFetchFutureAssetV1Resp.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_dict = subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountFetchFutureAssetV1Resp from a dict
subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_from_dict = SubaccountGetManagedSubaccountFetchFutureAssetV1Resp.from_dict(subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


