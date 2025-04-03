# WalletCreateAssetDustBtcV1RespDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_free** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**asset_full_name** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**to_bnb** | **str** |  | [optional] 
**to_bnb_off_exchange** | **str** |  | [optional] 
**to_btc** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_create_asset_dust_btc_v1_resp_details_inner import WalletCreateAssetDustBtcV1RespDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateAssetDustBtcV1RespDetailsInner from a JSON string
wallet_create_asset_dust_btc_v1_resp_details_inner_instance = WalletCreateAssetDustBtcV1RespDetailsInner.from_json(json)
# print the JSON string representation of the object
print(WalletCreateAssetDustBtcV1RespDetailsInner.to_json())

# convert the object into a dict
wallet_create_asset_dust_btc_v1_resp_details_inner_dict = wallet_create_asset_dust_btc_v1_resp_details_inner_instance.to_dict()
# create an instance of WalletCreateAssetDustBtcV1RespDetailsInner from a dict
wallet_create_asset_dust_btc_v1_resp_details_inner_from_dict = WalletCreateAssetDustBtcV1RespDetailsInner.from_dict(wallet_create_asset_dust_btc_v1_resp_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


