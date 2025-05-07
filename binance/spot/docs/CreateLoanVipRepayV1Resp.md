# CreateLoanVipRepayV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_coin** | **str** |  | [optional] 
**current_ltv** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**remaining_interest** | **str** |  | [optional] 
**remaining_principal** | **str** |  | [optional] 
**repay_amount** | **str** |  | [optional] 
**repay_status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_loan_vip_repay_v1_resp import CreateLoanVipRepayV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLoanVipRepayV1Resp from a JSON string
create_loan_vip_repay_v1_resp_instance = CreateLoanVipRepayV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateLoanVipRepayV1Resp.to_json())

# convert the object into a dict
create_loan_vip_repay_v1_resp_dict = create_loan_vip_repay_v1_resp_instance.to_dict()
# create an instance of CreateLoanVipRepayV1Resp from a dict
create_loan_vip_repay_v1_resp_from_dict = CreateLoanVipRepayV1Resp.from_dict(create_loan_vip_repay_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


