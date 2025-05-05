# UmfuturesGetApiTradingStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicators** | **Dict[str, object]** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_api_trading_status_v1_resp import UmfuturesGetApiTradingStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetApiTradingStatusV1Resp from a JSON string
umfutures_get_api_trading_status_v1_resp_instance = UmfuturesGetApiTradingStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetApiTradingStatusV1Resp.to_json())

# convert the object into a dict
umfutures_get_api_trading_status_v1_resp_dict = umfutures_get_api_trading_status_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetApiTradingStatusV1Resp from a dict
umfutures_get_api_trading_status_v1_resp_from_dict = UmfuturesGetApiTradingStatusV1Resp.from_dict(umfutures_get_api_trading_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


