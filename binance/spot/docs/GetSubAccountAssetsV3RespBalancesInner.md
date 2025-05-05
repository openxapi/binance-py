# GetSubAccountAssetsV3RespBalancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**free** | **int** |  | [optional] 
**freeze** | **int** |  | [optional] 
**locked** | **int** |  | [optional] 
**withdrawing** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_assets_v3_resp_balances_inner import GetSubAccountAssetsV3RespBalancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountAssetsV3RespBalancesInner from a JSON string
get_sub_account_assets_v3_resp_balances_inner_instance = GetSubAccountAssetsV3RespBalancesInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountAssetsV3RespBalancesInner.to_json())

# convert the object into a dict
get_sub_account_assets_v3_resp_balances_inner_dict = get_sub_account_assets_v3_resp_balances_inner_instance.to_dict()
# create an instance of GetSubAccountAssetsV3RespBalancesInner from a dict
get_sub_account_assets_v3_resp_balances_inner_from_dict = GetSubAccountAssetsV3RespBalancesInner.from_dict(get_sub_account_assets_v3_resp_balances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


