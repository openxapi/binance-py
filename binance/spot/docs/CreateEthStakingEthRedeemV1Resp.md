# CreateEthStakingEthRedeemV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrival_time** | **int** |  | [optional] 
**conversion_ratio** | **str** |  | [optional] 
**eth_amount** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_eth_staking_eth_redeem_v1_resp import CreateEthStakingEthRedeemV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEthStakingEthRedeemV1Resp from a JSON string
create_eth_staking_eth_redeem_v1_resp_instance = CreateEthStakingEthRedeemV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateEthStakingEthRedeemV1Resp.to_json())

# convert the object into a dict
create_eth_staking_eth_redeem_v1_resp_dict = create_eth_staking_eth_redeem_v1_resp_instance.to_dict()
# create an instance of CreateEthStakingEthRedeemV1Resp from a dict
create_eth_staking_eth_redeem_v1_resp_from_dict = CreateEthStakingEthRedeemV1Resp.from_dict(create_eth_staking_eth_redeem_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


