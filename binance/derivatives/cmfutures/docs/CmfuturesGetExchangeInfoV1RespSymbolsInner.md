# CmfuturesGetExchangeInfoV1RespSymbolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_type** | **List[str]** |  | [optional] 
**base_asset** | **str** |  | [optional] 
**base_asset_precision** | **int** |  | [optional] 
**contract_size** | **int** |  | [optional] 
**contract_status** | **str** |  | [optional] 
**contract_type** | **str** |  | [optional] 
**delivery_date** | **int** |  | [optional] 
**equal_qty_precision** | **int** |  | [optional] 
**filters** | [**List[CmfuturesSymbolFilter]**](CmfuturesSymbolFilter.md) |  | [optional] 
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
**symbol** | **str** |  | [optional] 
**time_in_force** | **List[str]** |  | [optional] 
**trigger_protect** | **str** |  | [optional] 
**underlying_sub_type** | **List[str]** |  | [optional] 
**underlying_type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_exchange_info_v1_resp_symbols_inner import CmfuturesGetExchangeInfoV1RespSymbolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetExchangeInfoV1RespSymbolsInner from a JSON string
cmfutures_get_exchange_info_v1_resp_symbols_inner_instance = CmfuturesGetExchangeInfoV1RespSymbolsInner.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetExchangeInfoV1RespSymbolsInner.to_json())

# convert the object into a dict
cmfutures_get_exchange_info_v1_resp_symbols_inner_dict = cmfutures_get_exchange_info_v1_resp_symbols_inner_instance.to_dict()
# create an instance of CmfuturesGetExchangeInfoV1RespSymbolsInner from a dict
cmfutures_get_exchange_info_v1_resp_symbols_inner_from_dict = CmfuturesGetExchangeInfoV1RespSymbolsInner.from_dict(cmfutures_get_exchange_info_v1_resp_symbols_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


