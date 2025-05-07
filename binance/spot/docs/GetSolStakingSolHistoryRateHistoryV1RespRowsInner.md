# GetSolStakingSolHistoryRateHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_percentage_rate** | **str** |  | [optional] 
**boost_rewards** | [**List[GetSolStakingSolHistoryRateHistoryV1RespRowsInnerBoostRewardsInner]**](GetSolStakingSolHistoryRateHistoryV1RespRowsInnerBoostRewardsInner.md) |  | [optional] 
**exchange_rate** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_sol_history_rate_history_v1_resp_rows_inner import GetSolStakingSolHistoryRateHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingSolHistoryRateHistoryV1RespRowsInner from a JSON string
get_sol_staking_sol_history_rate_history_v1_resp_rows_inner_instance = GetSolStakingSolHistoryRateHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingSolHistoryRateHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_sol_staking_sol_history_rate_history_v1_resp_rows_inner_dict = get_sol_staking_sol_history_rate_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSolStakingSolHistoryRateHistoryV1RespRowsInner from a dict
get_sol_staking_sol_history_rate_history_v1_resp_rows_inner_from_dict = GetSolStakingSolHistoryRateHistoryV1RespRowsInner.from_dict(get_sol_staking_sol_history_rate_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


