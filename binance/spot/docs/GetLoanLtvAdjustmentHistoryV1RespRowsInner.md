# GetLoanLtvAdjustmentHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjust_time** | **int** |  | [optional] 
**after_ltv** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**pre_ltv** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_ltv_adjustment_history_v1_resp_rows_inner import GetLoanLtvAdjustmentHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanLtvAdjustmentHistoryV1RespRowsInner from a JSON string
get_loan_ltv_adjustment_history_v1_resp_rows_inner_instance = GetLoanLtvAdjustmentHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanLtvAdjustmentHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_ltv_adjustment_history_v1_resp_rows_inner_dict = get_loan_ltv_adjustment_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanLtvAdjustmentHistoryV1RespRowsInner from a dict
get_loan_ltv_adjustment_history_v1_resp_rows_inner_from_dict = GetLoanLtvAdjustmentHistoryV1RespRowsInner.from_dict(get_loan_ltv_adjustment_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


