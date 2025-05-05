# GetAssetWalletBalanceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | **bool** |  | [optional] 
**balance** | **str** |  | [optional] 
**wallet_name** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_wallet_balance_v1_resp_item import GetAssetWalletBalanceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetWalletBalanceV1RespItem from a JSON string
get_asset_wallet_balance_v1_resp_item_instance = GetAssetWalletBalanceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetAssetWalletBalanceV1RespItem.to_json())

# convert the object into a dict
get_asset_wallet_balance_v1_resp_item_dict = get_asset_wallet_balance_v1_resp_item_instance.to_dict()
# create an instance of GetAssetWalletBalanceV1RespItem from a dict
get_asset_wallet_balance_v1_resp_item_from_dict = GetAssetWalletBalanceV1RespItem.from_dict(get_asset_wallet_balance_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


