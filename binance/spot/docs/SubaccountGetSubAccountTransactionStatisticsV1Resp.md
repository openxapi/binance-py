# SubaccountGetSubAccountTransactionStatisticsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recent30_btc_futures_total** | **str** |  | [optional] 
**recent30_btc_margin_total** | **str** |  | [optional] 
**recent30_btc_total** | **str** |  | [optional] 
**recent30_busd_futures_total** | **str** |  | [optional] 
**recent30_busd_margin_total** | **str** |  | [optional] 
**recent30_busd_total** | **str** |  | [optional] 
**trade_info_vos** | [**List[SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner]**](SubaccountGetSubAccountTransactionStatisticsV1RespTradeInfoVosInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.subaccount_get_sub_account_transaction_statistics_v1_resp import SubaccountGetSubAccountTransactionStatisticsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountTransactionStatisticsV1Resp from a JSON string
subaccount_get_sub_account_transaction_statistics_v1_resp_instance = SubaccountGetSubAccountTransactionStatisticsV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountTransactionStatisticsV1Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_transaction_statistics_v1_resp_dict = subaccount_get_sub_account_transaction_statistics_v1_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountTransactionStatisticsV1Resp from a dict
subaccount_get_sub_account_transaction_statistics_v1_resp_from_dict = SubaccountGetSubAccountTransactionStatisticsV1Resp.from_dict(subaccount_get_sub_account_transaction_statistics_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


