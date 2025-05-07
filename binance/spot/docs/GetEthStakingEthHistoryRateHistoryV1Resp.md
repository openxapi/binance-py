# GetEthStakingEthHistoryRateHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetEthStakingEthHistoryRateHistoryV1RespRowsInner]**](GetEthStakingEthHistoryRateHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_eth_staking_eth_history_rate_history_v1_resp import GetEthStakingEthHistoryRateHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthStakingEthHistoryRateHistoryV1Resp from a JSON string
get_eth_staking_eth_history_rate_history_v1_resp_instance = GetEthStakingEthHistoryRateHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetEthStakingEthHistoryRateHistoryV1Resp.to_json())

# convert the object into a dict
get_eth_staking_eth_history_rate_history_v1_resp_dict = get_eth_staking_eth_history_rate_history_v1_resp_instance.to_dict()
# create an instance of GetEthStakingEthHistoryRateHistoryV1Resp from a dict
get_eth_staking_eth_history_rate_history_v1_resp_from_dict = GetEthStakingEthHistoryRateHistoryV1Resp.from_dict(get_eth_staking_eth_history_rate_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


