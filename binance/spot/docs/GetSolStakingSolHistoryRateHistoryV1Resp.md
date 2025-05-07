# GetSolStakingSolHistoryRateHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetSolStakingSolHistoryRateHistoryV1RespRowsInner]**](GetSolStakingSolHistoryRateHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_sol_history_rate_history_v1_resp import GetSolStakingSolHistoryRateHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingSolHistoryRateHistoryV1Resp from a JSON string
get_sol_staking_sol_history_rate_history_v1_resp_instance = GetSolStakingSolHistoryRateHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingSolHistoryRateHistoryV1Resp.to_json())

# convert the object into a dict
get_sol_staking_sol_history_rate_history_v1_resp_dict = get_sol_staking_sol_history_rate_history_v1_resp_instance.to_dict()
# create an instance of GetSolStakingSolHistoryRateHistoryV1Resp from a dict
get_sol_staking_sol_history_rate_history_v1_resp_from_dict = GetSolStakingSolHistoryRateHistoryV1Resp.from_dict(get_sol_staking_sol_history_rate_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


