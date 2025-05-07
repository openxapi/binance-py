# GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjust_time** | **int** |  | [optional] 
**after_ltv** | **str** |  | [optional] 
**collateral_amount** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**pre_ltv** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_ltv_adjustment_history_v2_resp_rows_inner import GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner from a JSON string
get_loan_flexible_ltv_adjustment_history_v2_resp_rows_inner_instance = GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner.to_json())

# convert the object into a dict
get_loan_flexible_ltv_adjustment_history_v2_resp_rows_inner_dict = get_loan_flexible_ltv_adjustment_history_v2_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner from a dict
get_loan_flexible_ltv_adjustment_history_v2_resp_rows_inner_from_dict = GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner.from_dict(get_loan_flexible_ltv_adjustment_history_v2_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


