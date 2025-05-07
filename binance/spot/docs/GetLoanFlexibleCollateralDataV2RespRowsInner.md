# GetLoanFlexibleCollateralDataV2RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_coin** | **str** |  | [optional] 
**initial_ltv** | **str** |  | [optional] 
**liquidation_ltv** | **str** |  | [optional] 
**margin_call_ltv** | **str** |  | [optional] 
**max_limit** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_collateral_data_v2_resp_rows_inner import GetLoanFlexibleCollateralDataV2RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleCollateralDataV2RespRowsInner from a JSON string
get_loan_flexible_collateral_data_v2_resp_rows_inner_instance = GetLoanFlexibleCollateralDataV2RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleCollateralDataV2RespRowsInner.to_json())

# convert the object into a dict
get_loan_flexible_collateral_data_v2_resp_rows_inner_dict = get_loan_flexible_collateral_data_v2_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanFlexibleCollateralDataV2RespRowsInner from a dict
get_loan_flexible_collateral_data_v2_resp_rows_inner_from_dict = GetLoanFlexibleCollateralDataV2RespRowsInner.from_dict(get_loan_flexible_collateral_data_v2_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


