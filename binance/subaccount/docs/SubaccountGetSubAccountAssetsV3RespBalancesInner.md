# SubaccountGetSubAccountAssetsV3RespBalancesInner


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
from binance.subaccount.models.subaccount_get_sub_account_assets_v3_resp_balances_inner import SubaccountGetSubAccountAssetsV3RespBalancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountAssetsV3RespBalancesInner from a JSON string
subaccount_get_sub_account_assets_v3_resp_balances_inner_instance = SubaccountGetSubAccountAssetsV3RespBalancesInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountAssetsV3RespBalancesInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_assets_v3_resp_balances_inner_dict = subaccount_get_sub_account_assets_v3_resp_balances_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountAssetsV3RespBalancesInner from a dict
subaccount_get_sub_account_assets_v3_resp_balances_inner_from_dict = SubaccountGetSubAccountAssetsV3RespBalancesInner.from_dict(subaccount_get_sub_account_assets_v3_resp_balances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


