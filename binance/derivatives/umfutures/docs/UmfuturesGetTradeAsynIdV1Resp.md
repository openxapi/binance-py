# UmfuturesGetTradeAsynIdV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_id** | **str** |  | [optional] 
**expiration_timestamp** | **int** |  | [optional] 
**is_expired** | **object** |  | [optional] 
**notified** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_id_v1_resp import UmfuturesGetTradeAsynIdV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetTradeAsynIdV1Resp from a JSON string
umfutures_get_trade_asyn_id_v1_resp_instance = UmfuturesGetTradeAsynIdV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetTradeAsynIdV1Resp.to_json())

# convert the object into a dict
umfutures_get_trade_asyn_id_v1_resp_dict = umfutures_get_trade_asyn_id_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetTradeAsynIdV1Resp from a dict
umfutures_get_trade_asyn_id_v1_resp_from_dict = UmfuturesGetTradeAsynIdV1Resp.from_dict(umfutures_get_trade_asyn_id_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


