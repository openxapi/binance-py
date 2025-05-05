# GetMarginRepayLoanV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**tx_id** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_margin_repay_loan_v1_resp_rows_inner import GetMarginRepayLoanV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginRepayLoanV1RespRowsInner from a JSON string
get_margin_repay_loan_v1_resp_rows_inner_instance = GetMarginRepayLoanV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetMarginRepayLoanV1RespRowsInner.to_json())

# convert the object into a dict
get_margin_repay_loan_v1_resp_rows_inner_dict = get_margin_repay_loan_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetMarginRepayLoanV1RespRowsInner from a dict
get_margin_repay_loan_v1_resp_rows_inner_from_dict = GetMarginRepayLoanV1RespRowsInner.from_dict(get_margin_repay_loan_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


