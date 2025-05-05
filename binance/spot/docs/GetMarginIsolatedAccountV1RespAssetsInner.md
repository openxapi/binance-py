# GetMarginIsolatedAccountV1RespAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset** | [**GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset**](GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**index_price** | **str** |  | [optional] 
**isolated_created** | **bool** |  | [optional] 
**liquidate_price** | **str** |  | [optional] 
**liquidate_rate** | **str** |  | [optional] 
**margin_level** | **str** |  | [optional] 
**margin_level_status** | **str** |  | [optional] 
**margin_ratio** | **str** |  | [optional] 
**quote_asset** | [**GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset**](GetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**trade_enabled** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_account_v1_resp_assets_inner import GetMarginIsolatedAccountV1RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedAccountV1RespAssetsInner from a JSON string
get_margin_isolated_account_v1_resp_assets_inner_instance = GetMarginIsolatedAccountV1RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedAccountV1RespAssetsInner.to_json())

# convert the object into a dict
get_margin_isolated_account_v1_resp_assets_inner_dict = get_margin_isolated_account_v1_resp_assets_inner_instance.to_dict()
# create an instance of GetMarginIsolatedAccountV1RespAssetsInner from a dict
get_margin_isolated_account_v1_resp_assets_inner_from_dict = GetMarginIsolatedAccountV1RespAssetsInner.from_dict(get_margin_isolated_account_v1_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


