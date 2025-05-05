# GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**borrow_enabled** | **bool** |  | [optional] 
**borrowed** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**net_asset** | **str** |  | [optional] 
**net_asset_of_btc** | **str** |  | [optional] 
**repay_enabled** | **bool** |  | [optional] 
**total_asset** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_account_v1_resp_assets_inner_base_asset import GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset from a JSON string
get_margin_isolated_account_v1_resp_assets_inner_base_asset_instance = GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.to_json())

# convert the object into a dict
get_margin_isolated_account_v1_resp_assets_inner_base_asset_dict = get_margin_isolated_account_v1_resp_assets_inner_base_asset_instance.to_dict()
# create an instance of GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset from a dict
get_margin_isolated_account_v1_resp_assets_inner_base_asset_from_dict = GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.from_dict(get_margin_isolated_account_v1_resp_assets_inner_base_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


