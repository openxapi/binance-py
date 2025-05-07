# GetSolStakingSolHistoryStakingHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**distribute_amount** | **str** |  | [optional] 
**distribute_asset** | **str** |  | [optional] 
**exchange_rate** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_sol_history_staking_history_v1_resp_rows_inner import GetSolStakingSolHistoryStakingHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingSolHistoryStakingHistoryV1RespRowsInner from a JSON string
get_sol_staking_sol_history_staking_history_v1_resp_rows_inner_instance = GetSolStakingSolHistoryStakingHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingSolHistoryStakingHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_sol_staking_sol_history_staking_history_v1_resp_rows_inner_dict = get_sol_staking_sol_history_staking_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSolStakingSolHistoryStakingHistoryV1RespRowsInner from a dict
get_sol_staking_sol_history_staking_history_v1_resp_rows_inner_from_dict = GetSolStakingSolHistoryStakingHistoryV1RespRowsInner.from_dict(get_sol_staking_sol_history_staking_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


