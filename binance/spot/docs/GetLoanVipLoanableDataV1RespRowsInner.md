# GetLoanVipLoanableDataV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_30d_daily_interest_rate** | **str** |  | [optional] 
**var_30d_yearly_interest_rate** | **str** |  | [optional] 
**var_60d_daily_interest_rate** | **str** |  | [optional] 
**var_60d_yearly_interest_rate** | **str** |  | [optional] 
**flexible_daily_interest_rate** | **str** |  | [optional] 
**flexible_yearly_interest_rate** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**max_limit** | **str** |  | [optional] 
**min_limit** | **str** |  | [optional] 
**vip_level** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_loanable_data_v1_resp_rows_inner import GetLoanVipLoanableDataV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipLoanableDataV1RespRowsInner from a JSON string
get_loan_vip_loanable_data_v1_resp_rows_inner_instance = GetLoanVipLoanableDataV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipLoanableDataV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_vip_loanable_data_v1_resp_rows_inner_dict = get_loan_vip_loanable_data_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanVipLoanableDataV1RespRowsInner from a dict
get_loan_vip_loanable_data_v1_resp_rows_inner_from_dict = GetLoanVipLoanableDataV1RespRowsInner.from_dict(get_loan_vip_loanable_data_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


