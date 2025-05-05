# CmfuturesGetExchangeInfoV1RespRateLimitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**interval_num** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**rate_limit_type** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.cmfutures_get_exchange_info_v1_resp_rate_limits_inner import CmfuturesGetExchangeInfoV1RespRateLimitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetExchangeInfoV1RespRateLimitsInner from a JSON string
cmfutures_get_exchange_info_v1_resp_rate_limits_inner_instance = CmfuturesGetExchangeInfoV1RespRateLimitsInner.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetExchangeInfoV1RespRateLimitsInner.to_json())

# convert the object into a dict
cmfutures_get_exchange_info_v1_resp_rate_limits_inner_dict = cmfutures_get_exchange_info_v1_resp_rate_limits_inner_instance.to_dict()
# create an instance of CmfuturesGetExchangeInfoV1RespRateLimitsInner from a dict
cmfutures_get_exchange_info_v1_resp_rate_limits_inner_from_dict = CmfuturesGetExchangeInfoV1RespRateLimitsInner.from_dict(cmfutures_get_exchange_info_v1_resp_rate_limits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


