# GetSolStakingSolHistoryStakingHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetSolStakingSolHistoryStakingHistoryV1RespRowsInner]**](GetSolStakingSolHistoryStakingHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_sol_history_staking_history_v1_resp import GetSolStakingSolHistoryStakingHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingSolHistoryStakingHistoryV1Resp from a JSON string
get_sol_staking_sol_history_staking_history_v1_resp_instance = GetSolStakingSolHistoryStakingHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingSolHistoryStakingHistoryV1Resp.to_json())

# convert the object into a dict
get_sol_staking_sol_history_staking_history_v1_resp_dict = get_sol_staking_sol_history_staking_history_v1_resp_instance.to_dict()
# create an instance of GetSolStakingSolHistoryStakingHistoryV1Resp from a dict
get_sol_staking_sol_history_staking_history_v1_resp_from_dict = GetSolStakingSolHistoryStakingHistoryV1Resp.from_dict(get_sol_staking_sol_history_staking_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


