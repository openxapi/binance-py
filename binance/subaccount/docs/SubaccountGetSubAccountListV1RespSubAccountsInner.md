# SubaccountGetSubAccountListV1RespSubAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**is_asset_management_sub_account** | **bool** |  | [optional] 
**is_freeze** | **bool** |  | [optional] 
**is_managed_sub_account** | **bool** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_list_v1_resp_sub_accounts_inner import SubaccountGetSubAccountListV1RespSubAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountListV1RespSubAccountsInner from a JSON string
subaccount_get_sub_account_list_v1_resp_sub_accounts_inner_instance = SubaccountGetSubAccountListV1RespSubAccountsInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountListV1RespSubAccountsInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_list_v1_resp_sub_accounts_inner_dict = subaccount_get_sub_account_list_v1_resp_sub_accounts_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountListV1RespSubAccountsInner from a dict
subaccount_get_sub_account_list_v1_resp_sub_accounts_inner_from_dict = SubaccountGetSubAccountListV1RespSubAccountsInner.from_dict(subaccount_get_sub_account_list_v1_resp_sub_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


