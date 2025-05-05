# GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**negative_balance** | **int** |  | [optional] 
**negative_max_threshold** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner import GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner from a JSON string
get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner_instance = GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner.to_json())

# convert the object into a dict
get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner_dict = get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner_instance.to_dict()
# create an instance of GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner from a dict
get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner_from_dict = GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner.from_dict(get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


