# WalletGetAssetDribbletV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**user_asset_dribblets** | [**List[WalletGetAssetDribbletV1RespUserAssetDribbletsInner]**](WalletGetAssetDribbletV1RespUserAssetDribbletsInner.md) |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_dribblet_v1_resp import WalletGetAssetDribbletV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetDribbletV1Resp from a JSON string
wallet_get_asset_dribblet_v1_resp_instance = WalletGetAssetDribbletV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetDribbletV1Resp.to_json())

# convert the object into a dict
wallet_get_asset_dribblet_v1_resp_dict = wallet_get_asset_dribblet_v1_resp_instance.to_dict()
# create an instance of WalletGetAssetDribbletV1Resp from a dict
wallet_get_asset_dribblet_v1_resp_from_dict = WalletGetAssetDribbletV1Resp.from_dict(wallet_get_asset_dribblet_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


