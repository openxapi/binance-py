# MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset


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
from binance.margin.models.margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset import MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset from a JSON string
margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset_instance = MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.to_json())

# convert the object into a dict
margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset_dict = margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset_instance.to_dict()
# create an instance of MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset from a dict
margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset_from_dict = MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.from_dict(margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


