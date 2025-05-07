# GetEthStakingEthHistoryWbethRewardsHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**est_rewards_in_eth** | **str** |  | [optional] 
**rows** | [**List[GetEthStakingEthHistoryWbethRewardsHistoryV1RespRowsInner]**](GetEthStakingEthHistoryWbethRewardsHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_eth_staking_eth_history_wbeth_rewards_history_v1_resp import GetEthStakingEthHistoryWbethRewardsHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthStakingEthHistoryWbethRewardsHistoryV1Resp from a JSON string
get_eth_staking_eth_history_wbeth_rewards_history_v1_resp_instance = GetEthStakingEthHistoryWbethRewardsHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetEthStakingEthHistoryWbethRewardsHistoryV1Resp.to_json())

# convert the object into a dict
get_eth_staking_eth_history_wbeth_rewards_history_v1_resp_dict = get_eth_staking_eth_history_wbeth_rewards_history_v1_resp_instance.to_dict()
# create an instance of GetEthStakingEthHistoryWbethRewardsHistoryV1Resp from a dict
get_eth_staking_eth_history_wbeth_rewards_history_v1_resp_from_dict = GetEthStakingEthHistoryWbethRewardsHistoryV1Resp.from_dict(get_eth_staking_eth_history_wbeth_rewards_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


