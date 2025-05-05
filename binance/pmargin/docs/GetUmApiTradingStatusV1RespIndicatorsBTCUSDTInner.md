# GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicator** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**planned_recover_time** | **int** |  | [optional] 
**trigger_value** | **float** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_api_trading_status_v1_resp_indicators_btcusdt_inner import GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner from a JSON string
get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_instance = GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.from_json(json)
# print the JSON string representation of the object
print(GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.to_json())

# convert the object into a dict
get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_dict = get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_instance.to_dict()
# create an instance of GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner from a dict
get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_from_dict = GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.from_dict(get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


