# GetSolStakingAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bnsol_amount** | **str** |  | [optional] 
**holding_in_sol** | **str** |  | [optional] 
**thirty_days_profit_in_sol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_account_v1_resp import GetSolStakingAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingAccountV1Resp from a JSON string
get_sol_staking_account_v1_resp_instance = GetSolStakingAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingAccountV1Resp.to_json())

# convert the object into a dict
get_sol_staking_account_v1_resp_dict = get_sol_staking_account_v1_resp_instance.to_dict()
# create an instance of GetSolStakingAccountV1Resp from a dict
get_sol_staking_account_v1_resp_from_dict = GetSolStakingAccountV1Resp.from_dict(get_sol_staking_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


