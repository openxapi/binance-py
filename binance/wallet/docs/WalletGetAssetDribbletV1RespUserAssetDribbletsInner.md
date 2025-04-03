# WalletGetAssetDribbletV1RespUserAssetDribbletsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operate_time** | **int** |  | [optional] 
**total_service_charge_amount** | **str** |  | [optional] 
**total_transfered_amount** | **str** |  | [optional] 
**trans_id** | **int** |  | [optional] 
**user_asset_dribblet_details** | [**List[WalletGetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner]**](WalletGetAssetDribbletV1RespUserAssetDribbletsInnerUserAssetDribbletDetailsInner.md) |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_dribblet_v1_resp_user_asset_dribblets_inner import WalletGetAssetDribbletV1RespUserAssetDribbletsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetDribbletV1RespUserAssetDribbletsInner from a JSON string
wallet_get_asset_dribblet_v1_resp_user_asset_dribblets_inner_instance = WalletGetAssetDribbletV1RespUserAssetDribbletsInner.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetDribbletV1RespUserAssetDribbletsInner.to_json())

# convert the object into a dict
wallet_get_asset_dribblet_v1_resp_user_asset_dribblets_inner_dict = wallet_get_asset_dribblet_v1_resp_user_asset_dribblets_inner_instance.to_dict()
# create an instance of WalletGetAssetDribbletV1RespUserAssetDribbletsInner from a dict
wallet_get_asset_dribblet_v1_resp_user_asset_dribblets_inner_from_dict = WalletGetAssetDribbletV1RespUserAssetDribbletsInner.from_dict(wallet_get_asset_dribblet_v1_resp_user_asset_dribblets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


