# GetSolStakingSolHistoryRedemptionHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetSolStakingSolHistoryRedemptionHistoryV1RespRowsInner]**](GetSolStakingSolHistoryRedemptionHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_sol_history_redemption_history_v1_resp import GetSolStakingSolHistoryRedemptionHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingSolHistoryRedemptionHistoryV1Resp from a JSON string
get_sol_staking_sol_history_redemption_history_v1_resp_instance = GetSolStakingSolHistoryRedemptionHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingSolHistoryRedemptionHistoryV1Resp.to_json())

# convert the object into a dict
get_sol_staking_sol_history_redemption_history_v1_resp_dict = get_sol_staking_sol_history_redemption_history_v1_resp_instance.to_dict()
# create an instance of GetSolStakingSolHistoryRedemptionHistoryV1Resp from a dict
get_sol_staking_sol_history_redemption_history_v1_resp_from_dict = GetSolStakingSolHistoryRedemptionHistoryV1Resp.from_dict(get_sol_staking_sol_history_redemption_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


