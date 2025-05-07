# CreateLoanFlexibleBorrowV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_amount** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**loan_amount** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_loan_flexible_borrow_v2_resp import CreateLoanFlexibleBorrowV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLoanFlexibleBorrowV2Resp from a JSON string
create_loan_flexible_borrow_v2_resp_instance = CreateLoanFlexibleBorrowV2Resp.from_json(json)
# print the JSON string representation of the object
print(CreateLoanFlexibleBorrowV2Resp.to_json())

# convert the object into a dict
create_loan_flexible_borrow_v2_resp_dict = create_loan_flexible_borrow_v2_resp_instance.to_dict()
# create an instance of CreateLoanFlexibleBorrowV2Resp from a dict
create_loan_flexible_borrow_v2_resp_from_dict = CreateLoanFlexibleBorrowV2Resp.from_dict(create_loan_flexible_borrow_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


