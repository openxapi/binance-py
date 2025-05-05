# GetPortfolioNegativeBalanceExchangeRecordV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner]**](GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_portfolio_negative_balance_exchange_record_v1_resp import GetPortfolioNegativeBalanceExchangeRecordV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioNegativeBalanceExchangeRecordV1Resp from a JSON string
get_portfolio_negative_balance_exchange_record_v1_resp_instance = GetPortfolioNegativeBalanceExchangeRecordV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioNegativeBalanceExchangeRecordV1Resp.to_json())

# convert the object into a dict
get_portfolio_negative_balance_exchange_record_v1_resp_dict = get_portfolio_negative_balance_exchange_record_v1_resp_instance.to_dict()
# create an instance of GetPortfolioNegativeBalanceExchangeRecordV1Resp from a dict
get_portfolio_negative_balance_exchange_record_v1_resp_from_dict = GetPortfolioNegativeBalanceExchangeRecordV1Resp.from_dict(get_portfolio_negative_balance_exchange_record_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


