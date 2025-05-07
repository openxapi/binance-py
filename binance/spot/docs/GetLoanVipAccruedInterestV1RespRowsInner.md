# GetLoanVipAccruedInterestV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrual_time** | **int** |  | [optional] 
**annual_interest_rate** | **str** |  | [optional] 
**interest_amount** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**principal_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_accrued_interest_v1_resp_rows_inner import GetLoanVipAccruedInterestV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipAccruedInterestV1RespRowsInner from a JSON string
get_loan_vip_accrued_interest_v1_resp_rows_inner_instance = GetLoanVipAccruedInterestV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipAccruedInterestV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_vip_accrued_interest_v1_resp_rows_inner_dict = get_loan_vip_accrued_interest_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanVipAccruedInterestV1RespRowsInner from a dict
get_loan_vip_accrued_interest_v1_resp_rows_inner_from_dict = GetLoanVipAccruedInterestV1RespRowsInner.from_dict(get_loan_vip_accrued_interest_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


