# GetLoanFlexibleCollateralDataV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetLoanFlexibleCollateralDataV2RespRowsInner]**](GetLoanFlexibleCollateralDataV2RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_collateral_data_v2_resp import GetLoanFlexibleCollateralDataV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleCollateralDataV2Resp from a JSON string
get_loan_flexible_collateral_data_v2_resp_instance = GetLoanFlexibleCollateralDataV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleCollateralDataV2Resp.to_json())

# convert the object into a dict
get_loan_flexible_collateral_data_v2_resp_dict = get_loan_flexible_collateral_data_v2_resp_instance.to_dict()
# create an instance of GetLoanFlexibleCollateralDataV2Resp from a dict
get_loan_flexible_collateral_data_v2_resp_from_dict = GetLoanFlexibleCollateralDataV2Resp.from_dict(get_loan_flexible_collateral_data_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


