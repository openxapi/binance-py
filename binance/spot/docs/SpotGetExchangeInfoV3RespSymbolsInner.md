# SpotGetExchangeInfoV3RespSymbolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_trailing_stop** | **bool** |  | [optional] 
**allowed_self_trade_prevention_modes** | **List[str]** |  | [optional] 
**base_asset** | **str** |  | [optional] 
**base_asset_precision** | **int** |  | [optional] 
**base_commission_precision** | **int** |  | [optional] 
**cancel_replace_allowed** | **bool** |  | [optional] 
**default_self_trade_prevention_mode** | **str** |  | [optional] 
**filters** | [**List[SpotSymbolFilter]**](SpotSymbolFilter.md) |  | [optional] 
**iceberg_allowed** | **bool** |  | [optional] 
**is_margin_trading_allowed** | **bool** |  | [optional] 
**is_spot_trading_allowed** | **bool** |  | [optional] 
**oco_allowed** | **bool** |  | [optional] 
**order_types** | **List[str]** |  | [optional] 
**oto_allowed** | **bool** |  | [optional] 
**permission_sets** | **List[List[str]]** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**quote_asset_precision** | **int** |  | [optional] 
**quote_commission_precision** | **int** |  | [optional] 
**quote_order_qty_market_allowed** | **bool** |  | [optional] 
**quote_precision** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_exchange_info_v3_resp_symbols_inner import SpotGetExchangeInfoV3RespSymbolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetExchangeInfoV3RespSymbolsInner from a JSON string
spot_get_exchange_info_v3_resp_symbols_inner_instance = SpotGetExchangeInfoV3RespSymbolsInner.from_json(json)
# print the JSON string representation of the object
print(SpotGetExchangeInfoV3RespSymbolsInner.to_json())

# convert the object into a dict
spot_get_exchange_info_v3_resp_symbols_inner_dict = spot_get_exchange_info_v3_resp_symbols_inner_instance.to_dict()
# create an instance of SpotGetExchangeInfoV3RespSymbolsInner from a dict
spot_get_exchange_info_v3_resp_symbols_inner_from_dict = SpotGetExchangeInfoV3RespSymbolsInner.from_dict(spot_get_exchange_info_v3_resp_symbols_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


