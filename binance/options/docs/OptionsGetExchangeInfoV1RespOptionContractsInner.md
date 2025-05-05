# OptionsGetExchangeInfoV1RespOptionContractsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset** | **str** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**settle_asset** | **str** |  | [optional] 
**underlying** | **str** |  | [optional] 

## Example

```python
from binance.options.models.options_get_exchange_info_v1_resp_option_contracts_inner import OptionsGetExchangeInfoV1RespOptionContractsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetExchangeInfoV1RespOptionContractsInner from a JSON string
options_get_exchange_info_v1_resp_option_contracts_inner_instance = OptionsGetExchangeInfoV1RespOptionContractsInner.from_json(json)
# print the JSON string representation of the object
print(OptionsGetExchangeInfoV1RespOptionContractsInner.to_json())

# convert the object into a dict
options_get_exchange_info_v1_resp_option_contracts_inner_dict = options_get_exchange_info_v1_resp_option_contracts_inner_instance.to_dict()
# create an instance of OptionsGetExchangeInfoV1RespOptionContractsInner from a dict
options_get_exchange_info_v1_resp_option_contracts_inner_from_dict = OptionsGetExchangeInfoV1RespOptionContractsInner.from_dict(options_get_exchange_info_v1_resp_option_contracts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


