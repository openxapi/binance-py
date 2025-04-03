# WalletCreateAssetDustV1RespTransferResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**from_asset** | **str** |  | [optional] 
**operate_time** | **int** |  | [optional] 
**service_charge_amount** | **str** |  | [optional] 
**tran_id** | **int** |  | [optional] 
**transfered_amount** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_create_asset_dust_v1_resp_transfer_result_inner import WalletCreateAssetDustV1RespTransferResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateAssetDustV1RespTransferResultInner from a JSON string
wallet_create_asset_dust_v1_resp_transfer_result_inner_instance = WalletCreateAssetDustV1RespTransferResultInner.from_json(json)
# print the JSON string representation of the object
print(WalletCreateAssetDustV1RespTransferResultInner.to_json())

# convert the object into a dict
wallet_create_asset_dust_v1_resp_transfer_result_inner_dict = wallet_create_asset_dust_v1_resp_transfer_result_inner_instance.to_dict()
# create an instance of WalletCreateAssetDustV1RespTransferResultInner from a dict
wallet_create_asset_dust_v1_resp_transfer_result_inner_from_dict = WalletCreateAssetDustV1RespTransferResultInner.from_dict(wallet_create_asset_dust_v1_resp_transfer_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


