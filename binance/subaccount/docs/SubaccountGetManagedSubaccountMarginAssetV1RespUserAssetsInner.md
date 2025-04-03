# SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner


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
from binance.subaccount.models.subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner import SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner from a JSON string
subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_instance = SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_dict = subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner from a dict
subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_from_dict = SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner.from_dict(subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


