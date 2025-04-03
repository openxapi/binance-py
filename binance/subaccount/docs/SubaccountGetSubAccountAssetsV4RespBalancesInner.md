# SubaccountGetSubAccountAssetsV4RespBalancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**freeze** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**withdrawing** | **str** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_assets_v4_resp_balances_inner import SubaccountGetSubAccountAssetsV4RespBalancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountAssetsV4RespBalancesInner from a JSON string
subaccount_get_sub_account_assets_v4_resp_balances_inner_instance = SubaccountGetSubAccountAssetsV4RespBalancesInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountAssetsV4RespBalancesInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_assets_v4_resp_balances_inner_dict = subaccount_get_sub_account_assets_v4_resp_balances_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountAssetsV4RespBalancesInner from a dict
subaccount_get_sub_account_assets_v4_resp_balances_inner_from_dict = SubaccountGetSubAccountAssetsV4RespBalancesInner.from_dict(subaccount_get_sub_account_assets_v4_resp_balances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


