# GetPortfolioPmLoanV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_portfolio_pm_loan_v1_resp import GetPortfolioPmLoanV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioPmLoanV1Resp from a JSON string
get_portfolio_pm_loan_v1_resp_instance = GetPortfolioPmLoanV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioPmLoanV1Resp.to_json())

# convert the object into a dict
get_portfolio_pm_loan_v1_resp_dict = get_portfolio_pm_loan_v1_resp_instance.to_dict()
# create an instance of GetPortfolioPmLoanV1Resp from a dict
get_portfolio_pm_loan_v1_resp_from_dict = GetPortfolioPmLoanV1Resp.from_dict(get_portfolio_pm_loan_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


