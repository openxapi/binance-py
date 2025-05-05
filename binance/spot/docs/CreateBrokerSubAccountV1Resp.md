# CreateBrokerSubAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**subaccount_id** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_broker_sub_account_v1_resp import CreateBrokerSubAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrokerSubAccountV1Resp from a JSON string
create_broker_sub_account_v1_resp_instance = CreateBrokerSubAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBrokerSubAccountV1Resp.to_json())

# convert the object into a dict
create_broker_sub_account_v1_resp_dict = create_broker_sub_account_v1_resp_instance.to_dict()
# create an instance of CreateBrokerSubAccountV1Resp from a dict
create_broker_sub_account_v1_resp_from_dict = CreateBrokerSubAccountV1Resp.from_dict(create_broker_sub_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


