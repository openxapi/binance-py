# GetAccountSnapshotV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**snapshot_vos** | [**List[GetAccountSnapshotV1RespSnapshotVosInner]**](GetAccountSnapshotV1RespSnapshotVosInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_account_snapshot_v1_resp import GetAccountSnapshotV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountSnapshotV1Resp from a JSON string
get_account_snapshot_v1_resp_instance = GetAccountSnapshotV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountSnapshotV1Resp.to_json())

# convert the object into a dict
get_account_snapshot_v1_resp_dict = get_account_snapshot_v1_resp_instance.to_dict()
# create an instance of GetAccountSnapshotV1Resp from a dict
get_account_snapshot_v1_resp_from_dict = GetAccountSnapshotV1Resp.from_dict(get_account_snapshot_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


