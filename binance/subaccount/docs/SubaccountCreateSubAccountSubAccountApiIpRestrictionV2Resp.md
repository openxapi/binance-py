# SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**ip_list** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_create_sub_account_sub_account_api_ip_restriction_v2_resp import SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp from a JSON string
subaccount_create_sub_account_sub_account_api_ip_restriction_v2_resp_instance = SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp.to_json())

# convert the object into a dict
subaccount_create_sub_account_sub_account_api_ip_restriction_v2_resp_dict = subaccount_create_sub_account_sub_account_api_ip_restriction_v2_resp_instance.to_dict()
# create an instance of SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp from a dict
subaccount_create_sub_account_sub_account_api_ip_restriction_v2_resp_from_dict = SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp.from_dict(subaccount_create_sub_account_sub_account_api_ip_restriction_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


