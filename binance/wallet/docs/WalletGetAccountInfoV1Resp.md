# WalletGetAccountInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_future_enabled** | **bool** |  | [optional] 
**is_margin_enabled** | **bool** |  | [optional] 
**is_options_enabled** | **bool** |  | [optional] 
**is_portfolio_margin_retail_enabled** | **bool** |  | [optional] 
**vip_level** | **int** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_account_info_v1_resp import WalletGetAccountInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAccountInfoV1Resp from a JSON string
wallet_get_account_info_v1_resp_instance = WalletGetAccountInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletGetAccountInfoV1Resp.to_json())

# convert the object into a dict
wallet_get_account_info_v1_resp_dict = wallet_get_account_info_v1_resp_instance.to_dict()
# create an instance of WalletGetAccountInfoV1Resp from a dict
wallet_get_account_info_v1_resp_from_dict = WalletGetAccountInfoV1Resp.from_dict(wallet_get_account_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


