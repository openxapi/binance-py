# GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_parent_email** | **str** |  | [optional] 
**bind_parent_user_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**insert_time_stamp** | **int** |  | [optional] 
**is_future_enabled** | **bool** |  | [optional] 
**is_margin_enabled** | **bool** |  | [optional] 
**is_signed_lvt_risk_agreement** | **bool** |  | [optional] 
**is_sub_user_enabled** | **bool** |  | [optional] 
**is_user_active** | **bool** |  | [optional] 
**managersub_user_id** | **int** |  | [optional] 
**root_user_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_info_v1_resp_manager_sub_user_info_vo_list_inner import GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner from a JSON string
get_managed_subaccount_info_v1_resp_manager_sub_user_info_vo_list_inner_instance = GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner.to_json())

# convert the object into a dict
get_managed_subaccount_info_v1_resp_manager_sub_user_info_vo_list_inner_dict = get_managed_subaccount_info_v1_resp_manager_sub_user_info_vo_list_inner_instance.to_dict()
# create an instance of GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner from a dict
get_managed_subaccount_info_v1_resp_manager_sub_user_info_vo_list_inner_from_dict = GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner.from_dict(get_managed_subaccount_info_v1_resp_manager_sub_user_info_vo_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


