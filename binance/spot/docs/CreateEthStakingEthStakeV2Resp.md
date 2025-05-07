# CreateEthStakingEthStakeV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_ratio** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**wbeth_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_eth_staking_eth_stake_v2_resp import CreateEthStakingEthStakeV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEthStakingEthStakeV2Resp from a JSON string
create_eth_staking_eth_stake_v2_resp_instance = CreateEthStakingEthStakeV2Resp.from_json(json)
# print the JSON string representation of the object
print(CreateEthStakingEthStakeV2Resp.to_json())

# convert the object into a dict
create_eth_staking_eth_stake_v2_resp_dict = create_eth_staking_eth_stake_v2_resp_instance.to_dict()
# create an instance of CreateEthStakingEthStakeV2Resp from a dict
create_eth_staking_eth_stake_v2_resp_from_dict = CreateEthStakingEthStakeV2Resp.from_dict(create_eth_staking_eth_stake_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


