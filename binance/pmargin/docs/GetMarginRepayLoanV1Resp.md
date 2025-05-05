# GetMarginRepayLoanV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetMarginRepayLoanV1RespRowsInner]**](GetMarginRepayLoanV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_margin_repay_loan_v1_resp import GetMarginRepayLoanV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginRepayLoanV1Resp from a JSON string
get_margin_repay_loan_v1_resp_instance = GetMarginRepayLoanV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginRepayLoanV1Resp.to_json())

# convert the object into a dict
get_margin_repay_loan_v1_resp_dict = get_margin_repay_loan_v1_resp_instance.to_dict()
# create an instance of GetMarginRepayLoanV1Resp from a dict
get_margin_repay_loan_v1_resp_from_dict = GetMarginRepayLoanV1Resp.from_dict(get_margin_repay_loan_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


