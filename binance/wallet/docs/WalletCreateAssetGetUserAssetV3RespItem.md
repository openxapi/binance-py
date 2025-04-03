# WalletCreateAssetGetUserAssetV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**btc_valuation** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**freeze** | **str** |  | [optional] 
**ipoable** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**withdrawing** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_create_asset_get_user_asset_v3_resp_item import WalletCreateAssetGetUserAssetV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateAssetGetUserAssetV3RespItem from a JSON string
wallet_create_asset_get_user_asset_v3_resp_item_instance = WalletCreateAssetGetUserAssetV3RespItem.from_json(json)
# print the JSON string representation of the object
print(WalletCreateAssetGetUserAssetV3RespItem.to_json())

# convert the object into a dict
wallet_create_asset_get_user_asset_v3_resp_item_dict = wallet_create_asset_get_user_asset_v3_resp_item_instance.to_dict()
# create an instance of WalletCreateAssetGetUserAssetV3RespItem from a dict
wallet_create_asset_get_user_asset_v3_resp_item_from_dict = WalletCreateAssetGetUserAssetV3RespItem.from_dict(wallet_create_asset_get_user_asset_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


