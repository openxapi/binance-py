# UmfuturesGetExchangeInfoV1RespSymbolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_type** | **List[str]** |  | [optional] 
**base_asset** | **str** |  | [optional] 
**base_asset_precision** | **int** |  | [optional] 
**contract_type** | **str** |  | [optional] 
**delivery_date** | **int** |  | [optional] 
**filters** | [**List[UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner]**](UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner.md) |  | [optional] 
**liquidation_fee** | **str** |  | [optional] 
**maint_margin_percent** | **str** |  | [optional] 
**margin_asset** | **str** |  | [optional] 
**market_take_bound** | **str** |  | [optional] 
**onboard_date** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**price_precision** | **int** |  | [optional] 
**quantity_precision** | **int** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**quote_precision** | **int** |  | [optional] 
**required_margin_percent** | **str** |  | [optional] 
**settle_plan** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **List[str]** |  | [optional] 
**trigger_protect** | **str** |  | [optional] 
**underlying_sub_type** | **List[str]** |  | [optional] 
**underlying_type** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_exchange_info_v1_resp_symbols_inner import UmfuturesGetExchangeInfoV1RespSymbolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetExchangeInfoV1RespSymbolsInner from a JSON string
umfutures_get_exchange_info_v1_resp_symbols_inner_instance = UmfuturesGetExchangeInfoV1RespSymbolsInner.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetExchangeInfoV1RespSymbolsInner.to_json())

# convert the object into a dict
umfutures_get_exchange_info_v1_resp_symbols_inner_dict = umfutures_get_exchange_info_v1_resp_symbols_inner_instance.to_dict()
# create an instance of UmfuturesGetExchangeInfoV1RespSymbolsInner from a dict
umfutures_get_exchange_info_v1_resp_symbols_inner_from_dict = UmfuturesGetExchangeInfoV1RespSymbolsInner.from_dict(umfutures_get_exchange_info_v1_resp_symbols_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


