# GetAccountSnapshotV1RespSnapshotVosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetAccountSnapshotV1RespSnapshotVosInnerData**](GetAccountSnapshotV1RespSnapshotVosInnerData.md) |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_account_snapshot_v1_resp_snapshot_vos_inner import GetAccountSnapshotV1RespSnapshotVosInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountSnapshotV1RespSnapshotVosInner from a JSON string
get_account_snapshot_v1_resp_snapshot_vos_inner_instance = GetAccountSnapshotV1RespSnapshotVosInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountSnapshotV1RespSnapshotVosInner.to_json())

# convert the object into a dict
get_account_snapshot_v1_resp_snapshot_vos_inner_dict = get_account_snapshot_v1_resp_snapshot_vos_inner_instance.to_dict()
# create an instance of GetAccountSnapshotV1RespSnapshotVosInner from a dict
get_account_snapshot_v1_resp_snapshot_vos_inner_from_dict = GetAccountSnapshotV1RespSnapshotVosInner.from_dict(get_account_snapshot_v1_resp_snapshot_vos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


