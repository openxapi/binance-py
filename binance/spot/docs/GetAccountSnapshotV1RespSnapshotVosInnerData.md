# GetAccountSnapshotV1RespSnapshotVosInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[GetAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner]**](GetAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner.md) |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_account_snapshot_v1_resp_snapshot_vos_inner_data import GetAccountSnapshotV1RespSnapshotVosInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountSnapshotV1RespSnapshotVosInnerData from a JSON string
get_account_snapshot_v1_resp_snapshot_vos_inner_data_instance = GetAccountSnapshotV1RespSnapshotVosInnerData.from_json(json)
# print the JSON string representation of the object
print(GetAccountSnapshotV1RespSnapshotVosInnerData.to_json())

# convert the object into a dict
get_account_snapshot_v1_resp_snapshot_vos_inner_data_dict = get_account_snapshot_v1_resp_snapshot_vos_inner_data_instance.to_dict()
# create an instance of GetAccountSnapshotV1RespSnapshotVosInnerData from a dict
get_account_snapshot_v1_resp_snapshot_vos_inner_data_from_dict = GetAccountSnapshotV1RespSnapshotVosInnerData.from_dict(get_account_snapshot_v1_resp_snapshot_vos_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


