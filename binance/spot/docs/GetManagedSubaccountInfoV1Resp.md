# GetManagedSubaccountInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager_sub_user_info_vo_list** | [**List[GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner]**](GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_info_v1_resp import GetManagedSubaccountInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountInfoV1Resp from a JSON string
get_managed_subaccount_info_v1_resp_instance = GetManagedSubaccountInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountInfoV1Resp.to_json())

# convert the object into a dict
get_managed_subaccount_info_v1_resp_dict = get_managed_subaccount_info_v1_resp_instance.to_dict()
# create an instance of GetManagedSubaccountInfoV1Resp from a dict
get_managed_subaccount_info_v1_resp_from_dict = GetManagedSubaccountInfoV1Resp.from_dict(get_managed_subaccount_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


