# SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc** | **int** |  | [optional] 
**btc_futures** | **int** |  | [optional] 
**btc_margin** | **int** |  | [optional] 
**busd** | **int** |  | [optional] 
**busd_futures** | **int** |  | [optional] 
**busd_margin** | **int** |  | [optional] 
**var_date** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_transaction_statistics_v1_resp_trade_info_vos_inner import SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner from a JSON string
subaccount_get_sub_account_transaction_statistics_v1_resp_trade_info_vos_inner_instance = SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_transaction_statistics_v1_resp_trade_info_vos_inner_dict = subaccount_get_sub_account_transaction_statistics_v1_resp_trade_info_vos_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner from a dict
subaccount_get_sub_account_transaction_statistics_v1_resp_trade_info_vos_inner_from_dict = SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner.from_dict(subaccount_get_sub_account_transaction_statistics_v1_resp_trade_info_vos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


