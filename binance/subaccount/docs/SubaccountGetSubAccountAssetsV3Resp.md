# SubaccountGetSubAccountAssetsV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[SubaccountGetSubAccountAssetsV3RespBalancesInner]**](SubaccountGetSubAccountAssetsV3RespBalancesInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_assets_v3_resp import SubaccountGetSubAccountAssetsV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountAssetsV3Resp from a JSON string
subaccount_get_sub_account_assets_v3_resp_instance = SubaccountGetSubAccountAssetsV3Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountAssetsV3Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_assets_v3_resp_dict = subaccount_get_sub_account_assets_v3_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountAssetsV3Resp from a dict
subaccount_get_sub_account_assets_v3_resp_from_dict = SubaccountGetSubAccountAssetsV3Resp.from_dict(subaccount_get_sub_account_assets_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


