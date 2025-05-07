# GetLoanVipInterestRateHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annualized_interest_rate** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_interest_rate_history_v1_resp_rows_inner import GetLoanVipInterestRateHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipInterestRateHistoryV1RespRowsInner from a JSON string
get_loan_vip_interest_rate_history_v1_resp_rows_inner_instance = GetLoanVipInterestRateHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipInterestRateHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_vip_interest_rate_history_v1_resp_rows_inner_dict = get_loan_vip_interest_rate_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanVipInterestRateHistoryV1RespRowsInner from a dict
get_loan_vip_interest_rate_history_v1_resp_rows_inner_from_dict = GetLoanVipInterestRateHistoryV1RespRowsInner.from_dict(get_loan_vip_interest_rate_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


