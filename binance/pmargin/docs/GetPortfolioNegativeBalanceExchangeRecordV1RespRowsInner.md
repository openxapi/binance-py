# GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner]**](GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner.md) |  | [optional] 
**end_time** | **int** |  | [optional] 
**start_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner import GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner from a JSON string
get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_instance = GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner.to_json())

# convert the object into a dict
get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_dict = get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner from a dict
get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_from_dict = GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner.from_dict(get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


