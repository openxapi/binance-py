# OptionsGetExchangeInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_assets** | [**List[OptionsGetExchangeInfoV1RespOptionAssetsInner]**](OptionsGetExchangeInfoV1RespOptionAssetsInner.md) |  | [optional] 
**option_contracts** | [**List[OptionsGetExchangeInfoV1RespOptionContractsInner]**](OptionsGetExchangeInfoV1RespOptionContractsInner.md) |  | [optional] 
**option_symbols** | [**List[OptionsGetExchangeInfoV1RespOptionSymbolsInner]**](OptionsGetExchangeInfoV1RespOptionSymbolsInner.md) |  | [optional] 
**rate_limits** | [**List[OptionsGetExchangeInfoV1RespRateLimitsInner]**](OptionsGetExchangeInfoV1RespRateLimitsInner.md) |  | [optional] 
**server_time** | **int** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_exchange_info_v1_resp import OptionsGetExchangeInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetExchangeInfoV1Resp from a JSON string
options_get_exchange_info_v1_resp_instance = OptionsGetExchangeInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetExchangeInfoV1Resp.to_json())

# convert the object into a dict
options_get_exchange_info_v1_resp_dict = options_get_exchange_info_v1_resp_instance.to_dict()
# create an instance of OptionsGetExchangeInfoV1Resp from a dict
options_get_exchange_info_v1_resp_from_dict = OptionsGetExchangeInfoV1Resp.from_dict(options_get_exchange_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


