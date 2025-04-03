# SubaccountGetManagedSubaccountInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager_sub_user_info_vo_list** | [**List[SubaccountGetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner]**](SubaccountGetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_info_v1_resp import SubaccountGetManagedSubaccountInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountInfoV1Resp from a JSON string
subaccount_get_managed_subaccount_info_v1_resp_instance = SubaccountGetManagedSubaccountInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountInfoV1Resp.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_info_v1_resp_dict = subaccount_get_managed_subaccount_info_v1_resp_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountInfoV1Resp from a dict
subaccount_get_managed_subaccount_info_v1_resp_from_dict = SubaccountGetManagedSubaccountInfoV1Resp.from_dict(subaccount_get_managed_subaccount_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


