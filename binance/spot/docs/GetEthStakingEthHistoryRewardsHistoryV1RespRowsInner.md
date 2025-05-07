# GetEthStakingEthHistoryRewardsHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**annual_percentage_rate** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**holding** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_eth_staking_eth_history_rewards_history_v1_resp_rows_inner import GetEthStakingEthHistoryRewardsHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthStakingEthHistoryRewardsHistoryV1RespRowsInner from a JSON string
get_eth_staking_eth_history_rewards_history_v1_resp_rows_inner_instance = GetEthStakingEthHistoryRewardsHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetEthStakingEthHistoryRewardsHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_eth_staking_eth_history_rewards_history_v1_resp_rows_inner_dict = get_eth_staking_eth_history_rewards_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetEthStakingEthHistoryRewardsHistoryV1RespRowsInner from a dict
get_eth_staking_eth_history_rewards_history_v1_resp_rows_inner_from_dict = GetEthStakingEthHistoryRewardsHistoryV1RespRowsInner.from_dict(get_eth_staking_eth_history_rewards_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


