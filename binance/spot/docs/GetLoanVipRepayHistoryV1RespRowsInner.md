# GetLoanVipRepayHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_coin** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**loan_date** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**repay_amount** | **str** |  | [optional] 
**repay_status** | **str** |  | [optional] 
**repay_time** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_repay_history_v1_resp_rows_inner import GetLoanVipRepayHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipRepayHistoryV1RespRowsInner from a JSON string
get_loan_vip_repay_history_v1_resp_rows_inner_instance = GetLoanVipRepayHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipRepayHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_vip_repay_history_v1_resp_rows_inner_dict = get_loan_vip_repay_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanVipRepayHistoryV1RespRowsInner from a dict
get_loan_vip_repay_history_v1_resp_rows_inner_from_dict = GetLoanVipRepayHistoryV1RespRowsInner.from_dict(get_loan_vip_repay_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


