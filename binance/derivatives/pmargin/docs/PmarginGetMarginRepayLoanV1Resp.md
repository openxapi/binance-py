# PmarginGetMarginRepayLoanV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[PmarginGetMarginRepayLoanV1RespRowsInner]**](PmarginGetMarginRepayLoanV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_margin_repay_loan_v1_resp import PmarginGetMarginRepayLoanV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetMarginRepayLoanV1Resp from a JSON string
pmargin_get_margin_repay_loan_v1_resp_instance = PmarginGetMarginRepayLoanV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetMarginRepayLoanV1Resp.to_json())

# convert the object into a dict
pmargin_get_margin_repay_loan_v1_resp_dict = pmargin_get_margin_repay_loan_v1_resp_instance.to_dict()
# create an instance of PmarginGetMarginRepayLoanV1Resp from a dict
pmargin_get_margin_repay_loan_v1_resp_from_dict = PmarginGetMarginRepayLoanV1Resp.from_dict(pmargin_get_margin_repay_loan_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


