# CreateLoanVipBorrowV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_account_id** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**is_flexible_rate** | **str** |  | [optional] 
**loan_account_id** | **str** |  | [optional] 
**loan_amount** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**loan_term** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_loan_vip_borrow_v1_resp import CreateLoanVipBorrowV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLoanVipBorrowV1Resp from a JSON string
create_loan_vip_borrow_v1_resp_instance = CreateLoanVipBorrowV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateLoanVipBorrowV1Resp.to_json())

# convert the object into a dict
create_loan_vip_borrow_v1_resp_dict = create_loan_vip_borrow_v1_resp_instance.to_dict()
# create an instance of CreateLoanVipBorrowV1Resp from a dict
create_loan_vip_borrow_v1_resp_from_dict = CreateLoanVipBorrowV1Resp.from_dict(create_loan_vip_borrow_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


