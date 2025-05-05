# GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**from_asset** | **str** |  | [optional] 
**operate_time** | **int** |  | [optional] 
**service_charge_amount** | **str** |  | [optional] 
**trans_id** | **int** |  | [optional] 
**transfered_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_dribblet_v1_resp_user_asset_dribblets_inner_user_asset_dribblet_details_inner import GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner from a JSON string
get_asset_dribblet_v1_resp_user_asset_dribblets_inner_user_asset_dribblet_details_inner_instance = GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner.to_json())

# convert the object into a dict
get_asset_dribblet_v1_resp_user_asset_dribblets_inner_user_asset_dribblet_details_inner_dict = get_asset_dribblet_v1_resp_user_asset_dribblets_inner_user_asset_dribblet_details_inner_instance.to_dict()
# create an instance of GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner from a dict
get_asset_dribblet_v1_resp_user_asset_dribblets_inner_user_asset_dribblet_details_inner_from_dict = GetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner.from_dict(get_asset_dribblet_v1_resp_user_asset_dribblets_inner_user_asset_dribblet_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


