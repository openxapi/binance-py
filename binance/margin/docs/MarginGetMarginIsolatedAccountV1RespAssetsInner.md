# MarginGetMarginIsolatedAccountV1RespAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset** | [**MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset**](MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**index_price** | **str** |  | [optional] 
**isolated_created** | **bool** |  | [optional] 
**liquidate_price** | **str** |  | [optional] 
**liquidate_rate** | **str** |  | [optional] 
**margin_level** | **str** |  | [optional] 
**margin_level_status** | **str** |  | [optional] 
**margin_ratio** | **str** |  | [optional] 
**quote_asset** | [**MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset**](MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**trade_enabled** | **bool** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_isolated_account_v1_resp_assets_inner import MarginGetMarginIsolatedAccountV1RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginIsolatedAccountV1RespAssetsInner from a JSON string
margin_get_margin_isolated_account_v1_resp_assets_inner_instance = MarginGetMarginIsolatedAccountV1RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginIsolatedAccountV1RespAssetsInner.to_json())

# convert the object into a dict
margin_get_margin_isolated_account_v1_resp_assets_inner_dict = margin_get_margin_isolated_account_v1_resp_assets_inner_instance.to_dict()
# create an instance of MarginGetMarginIsolatedAccountV1RespAssetsInner from a dict
margin_get_margin_isolated_account_v1_resp_assets_inner_from_dict = MarginGetMarginIsolatedAccountV1RespAssetsInner.from_dict(margin_get_margin_isolated_account_v1_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


