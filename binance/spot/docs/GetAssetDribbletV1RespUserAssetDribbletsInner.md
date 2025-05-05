# GetAssetDribbletV1RespUserAssetDribbletsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operate_time** | **int** |  | [optional] 
**total_service_charge_amount** | **str** |  | [optional] 
**total_transfered_amount** | **str** |  | [optional] 
**trans_id** | **int** |  | [optional] 
**user_asset_dribblet_details** | [**List[GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner]**](GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_dribblet_v1_resp_user_asset_dribblets_inner import GetAssetDribbletV1RespUserAssetDribbletsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetDribbletV1RespUserAssetDribbletsInner from a JSON string
get_asset_dribblet_v1_resp_user_asset_dribblets_inner_instance = GetAssetDribbletV1RespUserAssetDribbletsInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetDribbletV1RespUserAssetDribbletsInner.to_json())

# convert the object into a dict
get_asset_dribblet_v1_resp_user_asset_dribblets_inner_dict = get_asset_dribblet_v1_resp_user_asset_dribblets_inner_instance.to_dict()
# create an instance of GetAssetDribbletV1RespUserAssetDribbletsInner from a dict
get_asset_dribblet_v1_resp_user_asset_dribblets_inner_from_dict = GetAssetDribbletV1RespUserAssetDribbletsInner.from_dict(get_asset_dribblet_v1_resp_user_asset_dribblets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


