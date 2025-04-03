# SubaccountGetSubAccountAssetsV4Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[SubaccountGetSubAccountAssetsV4RespBalancesInner]**](SubaccountGetSubAccountAssetsV4RespBalancesInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_assets_v4_resp import SubaccountGetSubAccountAssetsV4Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountAssetsV4Resp from a JSON string
subaccount_get_sub_account_assets_v4_resp_instance = SubaccountGetSubAccountAssetsV4Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountAssetsV4Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_assets_v4_resp_dict = subaccount_get_sub_account_assets_v4_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountAssetsV4Resp from a dict
subaccount_get_sub_account_assets_v4_resp_from_dict = SubaccountGetSubAccountAssetsV4Resp.from_dict(subaccount_get_sub_account_assets_v4_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


