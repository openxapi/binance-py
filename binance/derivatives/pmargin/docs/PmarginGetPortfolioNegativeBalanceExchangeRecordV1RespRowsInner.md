# PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner]**](PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner.md) |  | [optional] 
**end_time** | **int** |  | [optional] 
**start_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner import PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner from a JSON string
pmargin_get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_instance = PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner.to_json())

# convert the object into a dict
pmargin_get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_dict = pmargin_get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_instance.to_dict()
# create an instance of PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner from a dict
pmargin_get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_from_dict = PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner.from_dict(pmargin_get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


