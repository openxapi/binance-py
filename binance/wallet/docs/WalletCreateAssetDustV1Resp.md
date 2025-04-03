# WalletCreateAssetDustV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_service_charge** | **str** |  | [optional] 
**total_transfered** | **str** |  | [optional] 
**transfer_result** | [**List[WalletCreateAssetDustV1RespTransferResultInner]**](WalletCreateAssetDustV1RespTransferResultInner.md) |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_create_asset_dust_v1_resp import WalletCreateAssetDustV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateAssetDustV1Resp from a JSON string
wallet_create_asset_dust_v1_resp_instance = WalletCreateAssetDustV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletCreateAssetDustV1Resp.to_json())

# convert the object into a dict
wallet_create_asset_dust_v1_resp_dict = wallet_create_asset_dust_v1_resp_instance.to_dict()
# create an instance of WalletCreateAssetDustV1Resp from a dict
wallet_create_asset_dust_v1_resp_from_dict = WalletCreateAssetDustV1Resp.from_dict(wallet_create_asset_dust_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


