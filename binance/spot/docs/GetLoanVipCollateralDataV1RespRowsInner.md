# GetLoanVipCollateralDataV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1st_collateral_range** | **str** |  | [optional] 
**var_1st_collateral_ratio** | **str** |  | [optional] 
**var_2nd_collateral_range** | **str** |  | [optional] 
**var_2nd_collateral_ratio** | **str** |  | [optional] 
**var_3rd_collateral_range** | **str** |  | [optional] 
**var_3rd_collateral_ratio** | **str** |  | [optional] 
**var_4th_collateral_range** | **str** |  | [optional] 
**var_4th_collateral_ratio** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_collateral_data_v1_resp_rows_inner import GetLoanVipCollateralDataV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipCollateralDataV1RespRowsInner from a JSON string
get_loan_vip_collateral_data_v1_resp_rows_inner_instance = GetLoanVipCollateralDataV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipCollateralDataV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_vip_collateral_data_v1_resp_rows_inner_dict = get_loan_vip_collateral_data_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanVipCollateralDataV1RespRowsInner from a dict
get_loan_vip_collateral_data_v1_resp_rows_inner_from_dict = GetLoanVipCollateralDataV1RespRowsInner.from_dict(get_loan_vip_collateral_data_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


