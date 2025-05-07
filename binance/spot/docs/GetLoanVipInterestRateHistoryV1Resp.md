# GetLoanVipInterestRateHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetLoanVipInterestRateHistoryV1RespRowsInner]**](GetLoanVipInterestRateHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_interest_rate_history_v1_resp import GetLoanVipInterestRateHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipInterestRateHistoryV1Resp from a JSON string
get_loan_vip_interest_rate_history_v1_resp_instance = GetLoanVipInterestRateHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipInterestRateHistoryV1Resp.to_json())

# convert the object into a dict
get_loan_vip_interest_rate_history_v1_resp_dict = get_loan_vip_interest_rate_history_v1_resp_instance.to_dict()
# create an instance of GetLoanVipInterestRateHistoryV1Resp from a dict
get_loan_vip_interest_rate_history_v1_resp_from_dict = GetLoanVipInterestRateHistoryV1Resp.from_dict(get_loan_vip_interest_rate_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


