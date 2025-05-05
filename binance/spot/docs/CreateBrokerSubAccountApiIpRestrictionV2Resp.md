# CreateBrokerSubAccountApiIpRestrictionV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**ip_list** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_broker_sub_account_api_ip_restriction_v2_resp import CreateBrokerSubAccountApiIpRestrictionV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrokerSubAccountApiIpRestrictionV2Resp from a JSON string
create_broker_sub_account_api_ip_restriction_v2_resp_instance = CreateBrokerSubAccountApiIpRestrictionV2Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBrokerSubAccountApiIpRestrictionV2Resp.to_json())

# convert the object into a dict
create_broker_sub_account_api_ip_restriction_v2_resp_dict = create_broker_sub_account_api_ip_restriction_v2_resp_instance.to_dict()
# create an instance of CreateBrokerSubAccountApiIpRestrictionV2Resp from a dict
create_broker_sub_account_api_ip_restriction_v2_resp_from_dict = CreateBrokerSubAccountApiIpRestrictionV2Resp.from_dict(create_broker_sub_account_api_ip_restriction_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


