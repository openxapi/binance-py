# SubaccountGetSubAccountListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_accounts** | [**List[SubaccountGetSubAccountListV1RespSubAccountsInner]**](SubaccountGetSubAccountListV1RespSubAccountsInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_list_v1_resp import SubaccountGetSubAccountListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountListV1Resp from a JSON string
subaccount_get_sub_account_list_v1_resp_instance = SubaccountGetSubAccountListV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountListV1Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_list_v1_resp_dict = subaccount_get_sub_account_list_v1_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountListV1Resp from a dict
subaccount_get_sub_account_list_v1_resp_from_dict = SubaccountGetSubAccountListV1Resp.from_dict(subaccount_get_sub_account_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


