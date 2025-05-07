# GetLoanFlexibleLoanableDataV2RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flexible_interest_rate** | **str** |  | [optional] 
**flexible_max_limit** | **str** |  | [optional] 
**flexible_min_limit** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_loanable_data_v2_resp_rows_inner import GetLoanFlexibleLoanableDataV2RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleLoanableDataV2RespRowsInner from a JSON string
get_loan_flexible_loanable_data_v2_resp_rows_inner_instance = GetLoanFlexibleLoanableDataV2RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleLoanableDataV2RespRowsInner.to_json())

# convert the object into a dict
get_loan_flexible_loanable_data_v2_resp_rows_inner_dict = get_loan_flexible_loanable_data_v2_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanFlexibleLoanableDataV2RespRowsInner from a dict
get_loan_flexible_loanable_data_v2_resp_rows_inner_from_dict = GetLoanFlexibleLoanableDataV2RespRowsInner.from_dict(get_loan_flexible_loanable_data_v2_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


