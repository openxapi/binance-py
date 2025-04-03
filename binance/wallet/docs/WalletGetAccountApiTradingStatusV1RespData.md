# WalletGetAccountApiTradingStatusV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_locked** | **bool** |  | [optional] 
**planned_recover_time** | **int** |  | [optional] 
**trigger_condition** | [**WalletGetAccountApiTradingStatusV1RespDataTriggerCondition**](WalletGetAccountApiTradingStatusV1RespDataTriggerCondition.md) |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_account_api_trading_status_v1_resp_data import WalletGetAccountApiTradingStatusV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAccountApiTradingStatusV1RespData from a JSON string
wallet_get_account_api_trading_status_v1_resp_data_instance = WalletGetAccountApiTradingStatusV1RespData.from_json(json)
# print the JSON string representation of the object
print(WalletGetAccountApiTradingStatusV1RespData.to_json())

# convert the object into a dict
wallet_get_account_api_trading_status_v1_resp_data_dict = wallet_get_account_api_trading_status_v1_resp_data_instance.to_dict()
# create an instance of WalletGetAccountApiTradingStatusV1RespData from a dict
wallet_get_account_api_trading_status_v1_resp_data_from_dict = WalletGetAccountApiTradingStatusV1RespData.from_dict(wallet_get_account_api_trading_status_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


