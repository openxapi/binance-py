# WalletCreateAssetDustBtcV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[WalletCreateAssetDustBtcV1RespDetailsInner]**](WalletCreateAssetDustBtcV1RespDetailsInner.md) |  | [optional] 
**dribblet_percentage** | **str** |  | [optional] 
**total_transfer_bnb** | **str** |  | [optional] 
**total_transfer_btc** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_create_asset_dust_btc_v1_resp import WalletCreateAssetDustBtcV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateAssetDustBtcV1Resp from a JSON string
wallet_create_asset_dust_btc_v1_resp_instance = WalletCreateAssetDustBtcV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletCreateAssetDustBtcV1Resp.to_json())

# convert the object into a dict
wallet_create_asset_dust_btc_v1_resp_dict = wallet_create_asset_dust_btc_v1_resp_instance.to_dict()
# create an instance of WalletCreateAssetDustBtcV1Resp from a dict
wallet_create_asset_dust_btc_v1_resp_from_dict = WalletCreateAssetDustBtcV1Resp.from_dict(wallet_create_asset_dust_btc_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


