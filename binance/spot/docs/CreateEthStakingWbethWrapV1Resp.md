# CreateEthStakingWbethWrapV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_rate** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**wbeth_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_eth_staking_wbeth_wrap_v1_resp import CreateEthStakingWbethWrapV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEthStakingWbethWrapV1Resp from a JSON string
create_eth_staking_wbeth_wrap_v1_resp_instance = CreateEthStakingWbethWrapV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateEthStakingWbethWrapV1Resp.to_json())

# convert the object into a dict
create_eth_staking_wbeth_wrap_v1_resp_dict = create_eth_staking_wbeth_wrap_v1_resp_instance.to_dict()
# create an instance of CreateEthStakingWbethWrapV1Resp from a dict
create_eth_staking_wbeth_wrap_v1_resp_from_dict = CreateEthStakingWbethWrapV1Resp.from_dict(create_eth_staking_wbeth_wrap_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


