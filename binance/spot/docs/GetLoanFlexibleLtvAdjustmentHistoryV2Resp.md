# GetLoanFlexibleLtvAdjustmentHistoryV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner]**](GetLoanFlexibleLtvAdjustmentHistoryV2RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_ltv_adjustment_history_v2_resp import GetLoanFlexibleLtvAdjustmentHistoryV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleLtvAdjustmentHistoryV2Resp from a JSON string
get_loan_flexible_ltv_adjustment_history_v2_resp_instance = GetLoanFlexibleLtvAdjustmentHistoryV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleLtvAdjustmentHistoryV2Resp.to_json())

# convert the object into a dict
get_loan_flexible_ltv_adjustment_history_v2_resp_dict = get_loan_flexible_ltv_adjustment_history_v2_resp_instance.to_dict()
# create an instance of GetLoanFlexibleLtvAdjustmentHistoryV2Resp from a dict
get_loan_flexible_ltv_adjustment_history_v2_resp_from_dict = GetLoanFlexibleLtvAdjustmentHistoryV2Resp.from_dict(get_loan_flexible_ltv_adjustment_history_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


