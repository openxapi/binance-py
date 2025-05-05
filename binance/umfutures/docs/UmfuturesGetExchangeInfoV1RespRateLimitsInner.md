# UmfuturesGetExchangeInfoV1RespRateLimitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**interval_num** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**rate_limit_type** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_exchange_info_v1_resp_rate_limits_inner import UmfuturesGetExchangeInfoV1RespRateLimitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetExchangeInfoV1RespRateLimitsInner from a JSON string
umfutures_get_exchange_info_v1_resp_rate_limits_inner_instance = UmfuturesGetExchangeInfoV1RespRateLimitsInner.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetExchangeInfoV1RespRateLimitsInner.to_json())

# convert the object into a dict
umfutures_get_exchange_info_v1_resp_rate_limits_inner_dict = umfutures_get_exchange_info_v1_resp_rate_limits_inner_instance.to_dict()
# create an instance of UmfuturesGetExchangeInfoV1RespRateLimitsInner from a dict
umfutures_get_exchange_info_v1_resp_rate_limits_inner_from_dict = UmfuturesGetExchangeInfoV1RespRateLimitsInner.from_dict(umfutures_get_exchange_info_v1_resp_rate_limits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


