# GetSubAccountListV1RespSubAccountsInner


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
from binance.spot.models.get_sub_account_list_v1_resp_sub_accounts_inner import GetSubAccountListV1RespSubAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountListV1RespSubAccountsInner from a JSON string
get_sub_account_list_v1_resp_sub_accounts_inner_instance = GetSubAccountListV1RespSubAccountsInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountListV1RespSubAccountsInner.to_json())

# convert the object into a dict
get_sub_account_list_v1_resp_sub_accounts_inner_dict = get_sub_account_list_v1_resp_sub_accounts_inner_instance.to_dict()
# create an instance of GetSubAccountListV1RespSubAccountsInner from a dict
get_sub_account_list_v1_resp_sub_accounts_inner_from_dict = GetSubAccountListV1RespSubAccountsInner.from_dict(get_sub_account_list_v1_resp_sub_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


