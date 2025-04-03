# WalletCreateAssetGetFundingAssetV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**btc_valuation** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**freeze** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**withdrawing** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_create_asset_get_funding_asset_v1_resp_item import WalletCreateAssetGetFundingAssetV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateAssetGetFundingAssetV1RespItem from a JSON string
wallet_create_asset_get_funding_asset_v1_resp_item_instance = WalletCreateAssetGetFundingAssetV1RespItem.from_json(json)
# print the JSON string representation of the object
print(WalletCreateAssetGetFundingAssetV1RespItem.to_json())

# convert the object into a dict
wallet_create_asset_get_funding_asset_v1_resp_item_dict = wallet_create_asset_get_funding_asset_v1_resp_item_instance.to_dict()
# create an instance of WalletCreateAssetGetFundingAssetV1RespItem from a dict
wallet_create_asset_get_funding_asset_v1_resp_item_from_dict = WalletCreateAssetGetFundingAssetV1RespItem.from_dict(wallet_create_asset_get_funding_asset_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


