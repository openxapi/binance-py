# GetLoanFlexibleRepayHistoryV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetLoanFlexibleRepayHistoryV2RespRowsInner]**](GetLoanFlexibleRepayHistoryV2RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_repay_history_v2_resp import GetLoanFlexibleRepayHistoryV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleRepayHistoryV2Resp from a JSON string
get_loan_flexible_repay_history_v2_resp_instance = GetLoanFlexibleRepayHistoryV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleRepayHistoryV2Resp.to_json())

# convert the object into a dict
get_loan_flexible_repay_history_v2_resp_dict = get_loan_flexible_repay_history_v2_resp_instance.to_dict()
# create an instance of GetLoanFlexibleRepayHistoryV2Resp from a dict
get_loan_flexible_repay_history_v2_resp_from_dict = GetLoanFlexibleRepayHistoryV2Resp.from_dict(get_loan_flexible_repay_history_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


