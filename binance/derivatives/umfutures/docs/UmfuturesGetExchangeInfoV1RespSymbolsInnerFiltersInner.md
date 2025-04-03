# UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** |  | [optional] 
**max_price** | **str** |  | [optional] 
**min_price** | **str** |  | [optional] 
**tick_size** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner import UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner from a JSON string
umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner_instance = UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner.to_json())

# convert the object into a dict
umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner_dict = umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner_instance.to_dict()
# create an instance of UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner from a dict
umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner_from_dict = UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner.from_dict(umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


