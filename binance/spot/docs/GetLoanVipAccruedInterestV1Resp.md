# GetLoanVipAccruedInterestV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetLoanVipAccruedInterestV1RespRowsInner]**](GetLoanVipAccruedInterestV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_accrued_interest_v1_resp import GetLoanVipAccruedInterestV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipAccruedInterestV1Resp from a JSON string
get_loan_vip_accrued_interest_v1_resp_instance = GetLoanVipAccruedInterestV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipAccruedInterestV1Resp.to_json())

# convert the object into a dict
get_loan_vip_accrued_interest_v1_resp_dict = get_loan_vip_accrued_interest_v1_resp_instance.to_dict()
# create an instance of GetLoanVipAccruedInterestV1Resp from a dict
get_loan_vip_accrued_interest_v1_resp_from_dict = GetLoanVipAccruedInterestV1Resp.from_dict(get_loan_vip_accrued_interest_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


