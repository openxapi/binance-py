# GetSolStakingSolQuotaV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculating** | **bool** |  | [optional] 
**commission_fee** | **str** |  | [optional] 
**left_redemption_personal_quota** | **str** |  | [optional] 
**left_staking_personal_quota** | **str** |  | [optional] 
**min_redeem_amount** | **str** |  | [optional] 
**min_stake_amount** | **str** |  | [optional] 
**next_epoch_time** | **int** |  | [optional] 
**redeem_period** | **int** |  | [optional] 
**redeemable** | **bool** |  | [optional] 
**sold_out** | **bool** |  | [optional] 
**stakeable** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_sol_staking_sol_quota_v1_resp import GetSolStakingSolQuotaV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolStakingSolQuotaV1Resp from a JSON string
get_sol_staking_sol_quota_v1_resp_instance = GetSolStakingSolQuotaV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSolStakingSolQuotaV1Resp.to_json())

# convert the object into a dict
get_sol_staking_sol_quota_v1_resp_dict = get_sol_staking_sol_quota_v1_resp_instance.to_dict()
# create an instance of GetSolStakingSolQuotaV1Resp from a dict
get_sol_staking_sol_quota_v1_resp_from_dict = GetSolStakingSolQuotaV1Resp.from_dict(get_sol_staking_sol_quota_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


