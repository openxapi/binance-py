# DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apikey** | **str** |  | [optional] 
**ip_list** | **List[str]** |  | [optional] 
**subaccount_id** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.delete_broker_sub_account_api_ip_restriction_ip_list_v1_resp import DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp from a JSON string
delete_broker_sub_account_api_ip_restriction_ip_list_v1_resp_instance = DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp.to_json())

# convert the object into a dict
delete_broker_sub_account_api_ip_restriction_ip_list_v1_resp_dict = delete_broker_sub_account_api_ip_restriction_ip_list_v1_resp_instance.to_dict()
# create an instance of DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp from a dict
delete_broker_sub_account_api_ip_restriction_ip_list_v1_resp_from_dict = DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp.from_dict(delete_broker_sub_account_api_ip_restriction_ip_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


