# GetLoanFlexibleRepayRateV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_coin** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**rate** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_repay_rate_v2_resp import GetLoanFlexibleRepayRateV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleRepayRateV2Resp from a JSON string
get_loan_flexible_repay_rate_v2_resp_instance = GetLoanFlexibleRepayRateV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleRepayRateV2Resp.to_json())

# convert the object into a dict
get_loan_flexible_repay_rate_v2_resp_dict = get_loan_flexible_repay_rate_v2_resp_instance.to_dict()
# create an instance of GetLoanFlexibleRepayRateV2Resp from a dict
get_loan_flexible_repay_rate_v2_resp_from_dict = GetLoanFlexibleRepayRateV2Resp.from_dict(get_loan_flexible_repay_rate_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


