# PmarginproGetPortfolioPmLoanHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner]**](PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_pm_loan_history_v1_resp import PmarginproGetPortfolioPmLoanHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginproGetPortfolioPmLoanHistoryV1Resp from a JSON string
pmarginpro_get_portfolio_pm_loan_history_v1_resp_instance = PmarginproGetPortfolioPmLoanHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginproGetPortfolioPmLoanHistoryV1Resp.to_json())

# convert the object into a dict
pmarginpro_get_portfolio_pm_loan_history_v1_resp_dict = pmarginpro_get_portfolio_pm_loan_history_v1_resp_instance.to_dict()
# create an instance of PmarginproGetPortfolioPmLoanHistoryV1Resp from a dict
pmarginpro_get_portfolio_pm_loan_history_v1_resp_from_dict = PmarginproGetPortfolioPmLoanHistoryV1Resp.from_dict(pmarginpro_get_portfolio_pm_loan_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


