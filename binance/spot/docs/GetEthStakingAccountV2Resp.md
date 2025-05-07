# GetEthStakingAccountV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_in_eth** | **str** |  | [optional] 
**holdings** | [**GetEthStakingAccountV2RespHoldings**](GetEthStakingAccountV2RespHoldings.md) |  | [optional] 
**profit** | [**GetEthStakingAccountV2RespProfit**](GetEthStakingAccountV2RespProfit.md) |  | [optional] 
**thirty_days_profit_in_eth** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_eth_staking_account_v2_resp import GetEthStakingAccountV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthStakingAccountV2Resp from a JSON string
get_eth_staking_account_v2_resp_instance = GetEthStakingAccountV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetEthStakingAccountV2Resp.to_json())

# convert the object into a dict
get_eth_staking_account_v2_resp_dict = get_eth_staking_account_v2_resp_instance.to_dict()
# create an instance of GetEthStakingAccountV2Resp from a dict
get_eth_staking_account_v2_resp_from_dict = GetEthStakingAccountV2Resp.from_dict(get_eth_staking_account_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


