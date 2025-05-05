# CreateBrokerTransferFuturesV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_tran_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**txn_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_broker_transfer_futures_v1_resp import CreateBrokerTransferFuturesV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrokerTransferFuturesV1Resp from a JSON string
create_broker_transfer_futures_v1_resp_instance = CreateBrokerTransferFuturesV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBrokerTransferFuturesV1Resp.to_json())

# convert the object into a dict
create_broker_transfer_futures_v1_resp_dict = create_broker_transfer_futures_v1_resp_instance.to_dict()
# create an instance of CreateBrokerTransferFuturesV1Resp from a dict
create_broker_transfer_futures_v1_resp_from_dict = CreateBrokerTransferFuturesV1Resp.from_dict(create_broker_transfer_futures_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


