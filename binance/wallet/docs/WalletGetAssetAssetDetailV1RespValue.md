# WalletGetAssetAssetDetailV1RespValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_status** | **bool** |  | [optional] 
**deposit_tip** | **str** |  | [optional] 
**min_withdraw_amount** | **str** |  | [optional] 
**withdraw_fee** | **int** |  | [optional] 
**withdraw_status** | **bool** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_asset_detail_v1_resp_value import WalletGetAssetAssetDetailV1RespValue

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetAssetDetailV1RespValue from a JSON string
wallet_get_asset_asset_detail_v1_resp_value_instance = WalletGetAssetAssetDetailV1RespValue.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetAssetDetailV1RespValue.to_json())

# convert the object into a dict
wallet_get_asset_asset_detail_v1_resp_value_dict = wallet_get_asset_asset_detail_v1_resp_value_instance.to_dict()
# create an instance of WalletGetAssetAssetDetailV1RespValue from a dict
wallet_get_asset_asset_detail_v1_resp_value_from_dict = WalletGetAssetAssetDetailV1RespValue.from_dict(wallet_get_asset_asset_detail_v1_resp_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


