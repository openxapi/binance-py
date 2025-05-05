# CreateSubAccountSubAccountApiIpRestrictionV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**ip_list** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_sub_account_sub_account_api_ip_restriction_v2_resp import CreateSubAccountSubAccountApiIpRestrictionV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountSubAccountApiIpRestrictionV2Resp from a JSON string
create_sub_account_sub_account_api_ip_restriction_v2_resp_instance = CreateSubAccountSubAccountApiIpRestrictionV2Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountSubAccountApiIpRestrictionV2Resp.to_json())

# convert the object into a dict
create_sub_account_sub_account_api_ip_restriction_v2_resp_dict = create_sub_account_sub_account_api_ip_restriction_v2_resp_instance.to_dict()
# create an instance of CreateSubAccountSubAccountApiIpRestrictionV2Resp from a dict
create_sub_account_sub_account_api_ip_restriction_v2_resp_from_dict = CreateSubAccountSubAccountApiIpRestrictionV2Resp.from_dict(create_sub_account_sub_account_api_ip_restriction_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


