# GetEthStakingAccountV2RespHoldings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beth_amount** | **str** |  | [optional] 
**wbeth_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_eth_staking_account_v2_resp_holdings import GetEthStakingAccountV2RespHoldings

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthStakingAccountV2RespHoldings from a JSON string
get_eth_staking_account_v2_resp_holdings_instance = GetEthStakingAccountV2RespHoldings.from_json(json)
# print the JSON string representation of the object
print(GetEthStakingAccountV2RespHoldings.to_json())

# convert the object into a dict
get_eth_staking_account_v2_resp_holdings_dict = get_eth_staking_account_v2_resp_holdings_instance.to_dict()
# create an instance of GetEthStakingAccountV2RespHoldings from a dict
get_eth_staking_account_v2_resp_holdings_from_dict = GetEthStakingAccountV2RespHoldings.from_dict(get_eth_staking_account_v2_resp_holdings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


