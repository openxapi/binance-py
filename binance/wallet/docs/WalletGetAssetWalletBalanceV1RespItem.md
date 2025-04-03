# WalletGetAssetWalletBalanceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | **bool** |  | [optional] 
**balance** | **str** |  | [optional] 
**wallet_name** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_wallet_balance_v1_resp_item import WalletGetAssetWalletBalanceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetWalletBalanceV1RespItem from a JSON string
wallet_get_asset_wallet_balance_v1_resp_item_instance = WalletGetAssetWalletBalanceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetWalletBalanceV1RespItem.to_json())

# convert the object into a dict
wallet_get_asset_wallet_balance_v1_resp_item_dict = wallet_get_asset_wallet_balance_v1_resp_item_instance.to_dict()
# create an instance of WalletGetAssetWalletBalanceV1RespItem from a dict
wallet_get_asset_wallet_balance_v1_resp_item_from_dict = WalletGetAssetWalletBalanceV1RespItem.from_dict(wallet_get_asset_wallet_balance_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


