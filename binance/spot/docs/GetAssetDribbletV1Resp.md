# GetAssetDribbletV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**user_asset_dribblets** | [**List[GetAssetDribbletV1RespUserAssetDribbletsInner]**](GetAssetDribbletV1RespUserAssetDribbletsInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_dribblet_v1_resp import GetAssetDribbletV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetDribbletV1Resp from a JSON string
get_asset_dribblet_v1_resp_instance = GetAssetDribbletV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAssetDribbletV1Resp.to_json())

# convert the object into a dict
get_asset_dribblet_v1_resp_dict = get_asset_dribblet_v1_resp_instance.to_dict()
# create an instance of GetAssetDribbletV1Resp from a dict
get_asset_dribblet_v1_resp_from_dict = GetAssetDribbletV1Resp.from_dict(get_asset_dribblet_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


