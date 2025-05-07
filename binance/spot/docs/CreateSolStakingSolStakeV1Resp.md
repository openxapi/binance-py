# CreateSolStakingSolStakeV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bnsol_amount** | **str** |  | [optional] 
**exchange_rate** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_sol_staking_sol_stake_v1_resp import CreateSolStakingSolStakeV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSolStakingSolStakeV1Resp from a JSON string
create_sol_staking_sol_stake_v1_resp_instance = CreateSolStakingSolStakeV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSolStakingSolStakeV1Resp.to_json())

# convert the object into a dict
create_sol_staking_sol_stake_v1_resp_dict = create_sol_staking_sol_stake_v1_resp_instance.to_dict()
# create an instance of CreateSolStakingSolStakeV1Resp from a dict
create_sol_staking_sol_stake_v1_resp_from_dict = CreateSolStakingSolStakeV1Resp.from_dict(create_sol_staking_sol_stake_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


