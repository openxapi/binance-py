# GetBrokerSubAccountApiIpRestrictionV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apikey** | **str** |  | [optional] 
**ip_list** | **List[str]** |  | [optional] 
**ip_restrict** | **bool** |  | [optional] 
**subaccount_id** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_api_ip_restriction_v1_resp import GetBrokerSubAccountApiIpRestrictionV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountApiIpRestrictionV1Resp from a JSON string
get_broker_sub_account_api_ip_restriction_v1_resp_instance = GetBrokerSubAccountApiIpRestrictionV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountApiIpRestrictionV1Resp.to_json())

# convert the object into a dict
get_broker_sub_account_api_ip_restriction_v1_resp_dict = get_broker_sub_account_api_ip_restriction_v1_resp_instance.to_dict()
# create an instance of GetBrokerSubAccountApiIpRestrictionV1Resp from a dict
get_broker_sub_account_api_ip_restriction_v1_resp_from_dict = GetBrokerSubAccountApiIpRestrictionV1Resp.from_dict(get_broker_sub_account_api_ip_restriction_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


