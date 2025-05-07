# GetLoanVipRepayHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetLoanVipRepayHistoryV1RespRowsInner]**](GetLoanVipRepayHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_repay_history_v1_resp import GetLoanVipRepayHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipRepayHistoryV1Resp from a JSON string
get_loan_vip_repay_history_v1_resp_instance = GetLoanVipRepayHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipRepayHistoryV1Resp.to_json())

# convert the object into a dict
get_loan_vip_repay_history_v1_resp_dict = get_loan_vip_repay_history_v1_resp_instance.to_dict()
# create an instance of GetLoanVipRepayHistoryV1Resp from a dict
get_loan_vip_repay_history_v1_resp_from_dict = GetLoanVipRepayHistoryV1Resp.from_dict(get_loan_vip_repay_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


