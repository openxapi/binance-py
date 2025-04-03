# PmarginGetMarginRepayLoanV1RespRowsInner


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
from binance.derivatives.pmargin.models.pmargin_get_margin_repay_loan_v1_resp_rows_inner import PmarginGetMarginRepayLoanV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetMarginRepayLoanV1RespRowsInner from a JSON string
pmargin_get_margin_repay_loan_v1_resp_rows_inner_instance = PmarginGetMarginRepayLoanV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginGetMarginRepayLoanV1RespRowsInner.to_json())

# convert the object into a dict
pmargin_get_margin_repay_loan_v1_resp_rows_inner_dict = pmargin_get_margin_repay_loan_v1_resp_rows_inner_instance.to_dict()
# create an instance of PmarginGetMarginRepayLoanV1RespRowsInner from a dict
pmargin_get_margin_repay_loan_v1_resp_rows_inner_from_dict = PmarginGetMarginRepayLoanV1RespRowsInner.from_dict(pmargin_get_margin_repay_loan_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


