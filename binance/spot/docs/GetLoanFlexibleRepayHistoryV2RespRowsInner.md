# GetLoanFlexibleRepayHistoryV2RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_coin** | **str** |  | [optional] 
**collateral_return** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**repay_amount** | **str** |  | [optional] 
**repay_status** | **str** |  | [optional] 
**repay_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_repay_history_v2_resp_rows_inner import GetLoanFlexibleRepayHistoryV2RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleRepayHistoryV2RespRowsInner from a JSON string
get_loan_flexible_repay_history_v2_resp_rows_inner_instance = GetLoanFlexibleRepayHistoryV2RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleRepayHistoryV2RespRowsInner.to_json())

# convert the object into a dict
get_loan_flexible_repay_history_v2_resp_rows_inner_dict = get_loan_flexible_repay_history_v2_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanFlexibleRepayHistoryV2RespRowsInner from a dict
get_loan_flexible_repay_history_v2_resp_rows_inner_from_dict = GetLoanFlexibleRepayHistoryV2RespRowsInner.from_dict(get_loan_flexible_repay_history_v2_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


