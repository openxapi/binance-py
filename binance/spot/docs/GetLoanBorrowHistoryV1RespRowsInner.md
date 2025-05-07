# GetLoanBorrowHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrow_time** | **int** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**hourly_interest_rate** | **str** |  | [optional] 
**initial_collateral_amount** | **str** |  | [optional] 
**initial_loan_amount** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**loan_term** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_borrow_history_v1_resp_rows_inner import GetLoanBorrowHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanBorrowHistoryV1RespRowsInner from a JSON string
get_loan_borrow_history_v1_resp_rows_inner_instance = GetLoanBorrowHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanBorrowHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_borrow_history_v1_resp_rows_inner_dict = get_loan_borrow_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanBorrowHistoryV1RespRowsInner from a dict
get_loan_borrow_history_v1_resp_rows_inner_from_dict = GetLoanBorrowHistoryV1RespRowsInner.from_dict(get_loan_borrow_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


