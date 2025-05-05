# OptionsGetExchangeInfoV1RespRateLimitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**interval_num** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**rate_limit_type** | **str** |  | [optional] 

## Example

```python
from binance.options.models.options_get_exchange_info_v1_resp_rate_limits_inner import OptionsGetExchangeInfoV1RespRateLimitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetExchangeInfoV1RespRateLimitsInner from a JSON string
options_get_exchange_info_v1_resp_rate_limits_inner_instance = OptionsGetExchangeInfoV1RespRateLimitsInner.from_json(json)
# print the JSON string representation of the object
print(OptionsGetExchangeInfoV1RespRateLimitsInner.to_json())

# convert the object into a dict
options_get_exchange_info_v1_resp_rate_limits_inner_dict = options_get_exchange_info_v1_resp_rate_limits_inner_instance.to_dict()
# create an instance of OptionsGetExchangeInfoV1RespRateLimitsInner from a dict
options_get_exchange_info_v1_resp_rate_limits_inner_from_dict = OptionsGetExchangeInfoV1RespRateLimitsInner.from_dict(options_get_exchange_info_v1_resp_rate_limits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


