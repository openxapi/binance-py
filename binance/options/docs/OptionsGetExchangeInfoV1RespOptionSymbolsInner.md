# OptionsGetExchangeInfoV1RespOptionSymbolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **int** |  | [optional] 
**filters** | [**List[OptionsSymbolFilter]**](OptionsSymbolFilter.md) |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**maintenance_margin** | **str** |  | [optional] 
**maker_fee_rate** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**min_initial_margin** | **str** |  | [optional] 
**min_maintenance_margin** | **str** |  | [optional] 
**min_qty** | **str** |  | [optional] 
**price_scale** | **int** |  | [optional] 
**quantity_scale** | **int** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**strike_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_fee_rate** | **str** |  | [optional] 
**underlying** | **str** |  | [optional] 
**unit** | **int** |  | [optional] 

## Example

```python
from binance.options.models.options_get_exchange_info_v1_resp_option_symbols_inner import OptionsGetExchangeInfoV1RespOptionSymbolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetExchangeInfoV1RespOptionSymbolsInner from a JSON string
options_get_exchange_info_v1_resp_option_symbols_inner_instance = OptionsGetExchangeInfoV1RespOptionSymbolsInner.from_json(json)
# print the JSON string representation of the object
print(OptionsGetExchangeInfoV1RespOptionSymbolsInner.to_json())

# convert the object into a dict
options_get_exchange_info_v1_resp_option_symbols_inner_dict = options_get_exchange_info_v1_resp_option_symbols_inner_instance.to_dict()
# create an instance of OptionsGetExchangeInfoV1RespOptionSymbolsInner from a dict
options_get_exchange_info_v1_resp_option_symbols_inner_from_dict = OptionsGetExchangeInfoV1RespOptionSymbolsInner.from_dict(options_get_exchange_info_v1_resp_option_symbols_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


