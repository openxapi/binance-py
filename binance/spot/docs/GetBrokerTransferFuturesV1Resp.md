# GetBrokerTransferFuturesV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**futures_type** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**transfers** | [**List[GetBrokerTransferFuturesV1RespTransfersInner]**](GetBrokerTransferFuturesV1RespTransfersInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_transfer_futures_v1_resp import GetBrokerTransferFuturesV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerTransferFuturesV1Resp from a JSON string
get_broker_transfer_futures_v1_resp_instance = GetBrokerTransferFuturesV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetBrokerTransferFuturesV1Resp.to_json())

# convert the object into a dict
get_broker_transfer_futures_v1_resp_dict = get_broker_transfer_futures_v1_resp_instance.to_dict()
# create an instance of GetBrokerTransferFuturesV1Resp from a dict
get_broker_transfer_futures_v1_resp_from_dict = GetBrokerTransferFuturesV1Resp.from_dict(get_broker_transfer_futures_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


