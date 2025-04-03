# WalletGetAccountApiRestrictionsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**enable_fix_api_trade** | **bool** |  | [optional] 
**enable_fix_read_only** | **bool** |  | [optional] 
**enable_futures** | **bool** |  | [optional] 
**enable_internal_transfer** | **bool** |  | [optional] 
**enable_margin** | **bool** |  | [optional] 
**enable_portfolio_margin_trading** | **bool** |  | [optional] 
**enable_reading** | **bool** |  | [optional] 
**enable_spot_and_margin_trading** | **bool** |  | [optional] 
**enable_vanilla_options** | **bool** |  | [optional] 
**enable_withdrawals** | **bool** |  | [optional] 
**ip_restrict** | **bool** |  | [optional] 
**permits_universal_transfer** | **bool** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_account_api_restrictions_v1_resp import WalletGetAccountApiRestrictionsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAccountApiRestrictionsV1Resp from a JSON string
wallet_get_account_api_restrictions_v1_resp_instance = WalletGetAccountApiRestrictionsV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletGetAccountApiRestrictionsV1Resp.to_json())

# convert the object into a dict
wallet_get_account_api_restrictions_v1_resp_dict = wallet_get_account_api_restrictions_v1_resp_instance.to_dict()
# create an instance of WalletGetAccountApiRestrictionsV1Resp from a dict
wallet_get_account_api_restrictions_v1_resp_from_dict = WalletGetAccountApiRestrictionsV1Resp.from_dict(wallet_get_account_api_restrictions_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


