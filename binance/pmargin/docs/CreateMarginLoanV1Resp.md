# CreateMarginLoanV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.create_margin_loan_v1_resp import CreateMarginLoanV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginLoanV1Resp from a JSON string
create_margin_loan_v1_resp_instance = CreateMarginLoanV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateMarginLoanV1Resp.to_json())

# convert the object into a dict
create_margin_loan_v1_resp_dict = create_margin_loan_v1_resp_instance.to_dict()
# create an instance of CreateMarginLoanV1Resp from a dict
create_margin_loan_v1_resp_from_dict = CreateMarginLoanV1Resp.from_dict(create_margin_loan_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


