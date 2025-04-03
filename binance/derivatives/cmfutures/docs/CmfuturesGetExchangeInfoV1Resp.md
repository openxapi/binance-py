# CmfuturesGetExchangeInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_filters** | **List[object]** |  | [optional] 
**rate_limits** | [**List[CmfuturesGetExchangeInfoV1RespRateLimitsInner]**](CmfuturesGetExchangeInfoV1RespRateLimitsInner.md) |  | [optional] 
**server_time** | **int** |  | [optional] 
**symbols** | [**List[CmfuturesGetExchangeInfoV1RespSymbolsInner]**](CmfuturesGetExchangeInfoV1RespSymbolsInner.md) |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_exchange_info_v1_resp import CmfuturesGetExchangeInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetExchangeInfoV1Resp from a JSON string
cmfutures_get_exchange_info_v1_resp_instance = CmfuturesGetExchangeInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetExchangeInfoV1Resp.to_json())

# convert the object into a dict
cmfutures_get_exchange_info_v1_resp_dict = cmfutures_get_exchange_info_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetExchangeInfoV1Resp from a dict
cmfutures_get_exchange_info_v1_resp_from_dict = CmfuturesGetExchangeInfoV1Resp.from_dict(cmfutures_get_exchange_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


