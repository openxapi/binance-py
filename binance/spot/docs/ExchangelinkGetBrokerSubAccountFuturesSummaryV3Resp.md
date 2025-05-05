# ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner]**](ExchangelinkGetBrokerSubAccountFuturesSummaryV3RespDataInner.md) |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.exchangelink_get_broker_sub_account_futures_summary_v3_resp import ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp from a JSON string
exchangelink_get_broker_sub_account_futures_summary_v3_resp_instance = ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp.from_json(json)
# print the JSON string representation of the object
print(ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp.to_json())

# convert the object into a dict
exchangelink_get_broker_sub_account_futures_summary_v3_resp_dict = exchangelink_get_broker_sub_account_futures_summary_v3_resp_instance.to_dict()
# create an instance of ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp from a dict
exchangelink_get_broker_sub_account_futures_summary_v3_resp_from_dict = ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp.from_dict(exchangelink_get_broker_sub_account_futures_summary_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


