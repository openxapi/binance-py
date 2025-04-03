# UmfuturesGetTradeAsynV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_cost_timestamp_of_last30d** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_v1_resp import UmfuturesGetTradeAsynV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetTradeAsynV1Resp from a JSON string
umfutures_get_trade_asyn_v1_resp_instance = UmfuturesGetTradeAsynV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetTradeAsynV1Resp.to_json())

# convert the object into a dict
umfutures_get_trade_asyn_v1_resp_dict = umfutures_get_trade_asyn_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetTradeAsynV1Resp from a dict
umfutures_get_trade_asyn_v1_resp_from_dict = UmfuturesGetTradeAsynV1Resp.from_dict(umfutures_get_trade_asyn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


