# UmfuturesGetExchangeInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[UmfuturesGetExchangeInfoV1RespAssetsInner]**](UmfuturesGetExchangeInfoV1RespAssetsInner.md) |  | [optional] 
**exchange_filters** | **List[str]** |  | [optional] 
**rate_limits** | [**List[UmfuturesGetExchangeInfoV1RespRateLimitsInner]**](UmfuturesGetExchangeInfoV1RespRateLimitsInner.md) |  | [optional] 
**server_time** | **int** |  | [optional] 
**symbols** | [**List[UmfuturesGetExchangeInfoV1RespSymbolsInner]**](UmfuturesGetExchangeInfoV1RespSymbolsInner.md) |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_exchange_info_v1_resp import UmfuturesGetExchangeInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetExchangeInfoV1Resp from a JSON string
umfutures_get_exchange_info_v1_resp_instance = UmfuturesGetExchangeInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetExchangeInfoV1Resp.to_json())

# convert the object into a dict
umfutures_get_exchange_info_v1_resp_dict = umfutures_get_exchange_info_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetExchangeInfoV1Resp from a dict
umfutures_get_exchange_info_v1_resp_from_dict = UmfuturesGetExchangeInfoV1Resp.from_dict(umfutures_get_exchange_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


