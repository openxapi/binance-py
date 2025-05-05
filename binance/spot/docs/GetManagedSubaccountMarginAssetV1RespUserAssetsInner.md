# GetManagedSubaccountMarginAssetV1RespUserAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**borrowed** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**net_asset** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_margin_asset_v1_resp_user_assets_inner import GetManagedSubaccountMarginAssetV1RespUserAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountMarginAssetV1RespUserAssetsInner from a JSON string
get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_instance = GetManagedSubaccountMarginAssetV1RespUserAssetsInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountMarginAssetV1RespUserAssetsInner.to_json())

# convert the object into a dict
get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_dict = get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_instance.to_dict()
# create an instance of GetManagedSubaccountMarginAssetV1RespUserAssetsInner from a dict
get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_from_dict = GetManagedSubaccountMarginAssetV1RespUserAssetsInner.from_dict(get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


