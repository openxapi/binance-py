# CreateLoanFlexibleRepayCollateralV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_coin** | **str** |  | [optional] 
**current_ltv** | **str** |  | [optional] 
**full_repayment** | **bool** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**remaining_collateral** | **str** |  | [optional] 
**remaining_debt** | **str** |  | [optional] 
**repay_status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_loan_flexible_repay_collateral_v2_resp import CreateLoanFlexibleRepayCollateralV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLoanFlexibleRepayCollateralV2Resp from a JSON string
create_loan_flexible_repay_collateral_v2_resp_instance = CreateLoanFlexibleRepayCollateralV2Resp.from_json(json)
# print the JSON string representation of the object
print(CreateLoanFlexibleRepayCollateralV2Resp.to_json())

# convert the object into a dict
create_loan_flexible_repay_collateral_v2_resp_dict = create_loan_flexible_repay_collateral_v2_resp_instance.to_dict()
# create an instance of CreateLoanFlexibleRepayCollateralV2Resp from a dict
create_loan_flexible_repay_collateral_v2_resp_from_dict = CreateLoanFlexibleRepayCollateralV2Resp.from_dict(create_loan_flexible_repay_collateral_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


