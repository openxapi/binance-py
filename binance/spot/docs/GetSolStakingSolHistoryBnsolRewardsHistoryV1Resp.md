# GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**est_rewards_in_sol** | **str** |  | [optional] 
**rows** | [**List[GetSolStakingSolHistoryBnsolRewardsHistoryV1RespRowsInner]**](GetSolStakingSolHistoryBnsolRewardsHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_sol_history_bnsol_rewards_history_v1_resp import GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp from a JSON string
get_sol_staking_sol_history_bnsol_rewards_history_v1_resp_instance = GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp.to_json())

# convert the object into a dict
get_sol_staking_sol_history_bnsol_rewards_history_v1_resp_dict = get_sol_staking_sol_history_bnsol_rewards_history_v1_resp_instance.to_dict()
# create an instance of GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp from a dict
get_sol_staking_sol_history_bnsol_rewards_history_v1_resp_from_dict = GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp.from_dict(get_sol_staking_sol_history_bnsol_rewards_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


