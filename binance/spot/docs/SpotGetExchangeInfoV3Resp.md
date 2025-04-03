# SpotGetExchangeInfoV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_filters** | [**List[SpotGetExchangeInfoV3RespExchangeFiltersInner]**](SpotGetExchangeInfoV3RespExchangeFiltersInner.md) |  | [optional] 
**rate_limits** | [**List[SpotRateLimit]**](SpotRateLimit.md) |  | [optional] 
**server_time** | **int** |  | [optional] 
**sors** | [**List[SpotGetExchangeInfoV3RespSorsInner]**](SpotGetExchangeInfoV3RespSorsInner.md) |  | [optional] 
**symbols** | [**List[SpotGetExchangeInfoV3RespSymbolsInner]**](SpotGetExchangeInfoV3RespSymbolsInner.md) |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_exchange_info_v3_resp import SpotGetExchangeInfoV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetExchangeInfoV3Resp from a JSON string
spot_get_exchange_info_v3_resp_instance = SpotGetExchangeInfoV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetExchangeInfoV3Resp.to_json())

# convert the object into a dict
spot_get_exchange_info_v3_resp_dict = spot_get_exchange_info_v3_resp_instance.to_dict()
# create an instance of SpotGetExchangeInfoV3Resp from a dict
spot_get_exchange_info_v3_resp_from_dict = SpotGetExchangeInfoV3Resp.from_dict(spot_get_exchange_info_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


