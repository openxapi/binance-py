# CreateBrokerTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_tran_id** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_broker_transfer_v1_resp import CreateBrokerTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrokerTransferV1Resp from a JSON string
create_broker_transfer_v1_resp_instance = CreateBrokerTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBrokerTransferV1Resp.to_json())

# convert the object into a dict
create_broker_transfer_v1_resp_dict = create_broker_transfer_v1_resp_instance.to_dict()
# create an instance of CreateBrokerTransferV1Resp from a dict
create_broker_transfer_v1_resp_from_dict = CreateBrokerTransferV1Resp.from_dict(create_broker_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


