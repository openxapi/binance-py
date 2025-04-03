# PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner


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
from binance.derivatives.pmargin.models.pmargin_get_um_api_trading_status_v1_resp_indicators_btcusdt_inner import PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner from a JSON string
pmargin_get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_instance = PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.to_json())

# convert the object into a dict
pmargin_get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_dict = pmargin_get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_instance.to_dict()
# create an instance of PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner from a dict
pmargin_get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_from_dict = PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.from_dict(pmargin_get_um_api_trading_status_v1_resp_indicators_btcusdt_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


