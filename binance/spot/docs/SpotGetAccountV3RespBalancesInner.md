# SpotGetAccountV3RespBalancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_account_v3_resp_balances_inner import SpotGetAccountV3RespBalancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetAccountV3RespBalancesInner from a JSON string
spot_get_account_v3_resp_balances_inner_instance = SpotGetAccountV3RespBalancesInner.from_json(json)
# print the JSON string representation of the object
print(SpotGetAccountV3RespBalancesInner.to_json())

# convert the object into a dict
spot_get_account_v3_resp_balances_inner_dict = spot_get_account_v3_resp_balances_inner_instance.to_dict()
# create an instance of SpotGetAccountV3RespBalancesInner from a dict
spot_get_account_v3_resp_balances_inner_from_dict = SpotGetAccountV3RespBalancesInner.from_dict(spot_get_account_v3_resp_balances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


