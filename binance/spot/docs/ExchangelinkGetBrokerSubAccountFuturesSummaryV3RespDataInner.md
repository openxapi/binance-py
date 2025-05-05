# ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**futures_enable** | **bool** |  | [optional] 
**sub_account_id** | **str** |  | [optional] 
**total_initial_margin** | **str** |  | [optional] 
**total_maintenance_margin** | **str** |  | [optional] 
**total_margin_balance** | **str** |  | [optional] 
**total_margin_balance_of_usdt** | **str** |  | [optional] 
**total_open_order_initial_margin** | **str** |  | [optional] 
**total_position_initial_margin** | **str** |  | [optional] 
**total_unrealized_profit** | **str** |  | [optional] 
**total_unrealized_profit_of_usdt** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 
**total_wallet_balance_of_usdt** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.exchangelink_get_broker_sub_account_futures_summary_v3_resp_data_inner import ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner from a JSON string
exchangelink_get_broker_sub_account_futures_summary_v3_resp_data_inner_instance = ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner.from_json(json)
# print the JSON string representation of the object
print(ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner.to_json())

# convert the object into a dict
exchangelink_get_broker_sub_account_futures_summary_v3_resp_data_inner_dict = exchangelink_get_broker_sub_account_futures_summary_v3_resp_data_inner_instance.to_dict()
# create an instance of ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner from a dict
exchangelink_get_broker_sub_account_futures_summary_v3_resp_data_inner_from_dict = ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner.from_dict(exchangelink_get_broker_sub_account_futures_summary_v3_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


