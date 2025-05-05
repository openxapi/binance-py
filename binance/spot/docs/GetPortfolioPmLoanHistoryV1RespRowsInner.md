# GetPortfolioPmLoanHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**repay_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_portfolio_pm_loan_history_v1_resp_rows_inner import GetPortfolioPmLoanHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioPmLoanHistoryV1RespRowsInner from a JSON string
get_portfolio_pm_loan_history_v1_resp_rows_inner_instance = GetPortfolioPmLoanHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioPmLoanHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_portfolio_pm_loan_history_v1_resp_rows_inner_dict = get_portfolio_pm_loan_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetPortfolioPmLoanHistoryV1RespRowsInner from a dict
get_portfolio_pm_loan_history_v1_resp_rows_inner_from_dict = GetPortfolioPmLoanHistoryV1RespRowsInner.from_dict(get_portfolio_pm_loan_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


