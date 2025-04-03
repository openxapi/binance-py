# PmarginGetUmApiTradingStatusV1RespIndicators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btcusdt** | [**List[PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner]**](PmarginGetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.md) |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_api_trading_status_v1_resp_indicators import PmarginGetUmApiTradingStatusV1RespIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmApiTradingStatusV1RespIndicators from a JSON string
pmargin_get_um_api_trading_status_v1_resp_indicators_instance = PmarginGetUmApiTradingStatusV1RespIndicators.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmApiTradingStatusV1RespIndicators.to_json())

# convert the object into a dict
pmargin_get_um_api_trading_status_v1_resp_indicators_dict = pmargin_get_um_api_trading_status_v1_resp_indicators_instance.to_dict()
# create an instance of PmarginGetUmApiTradingStatusV1RespIndicators from a dict
pmargin_get_um_api_trading_status_v1_resp_indicators_from_dict = PmarginGetUmApiTradingStatusV1RespIndicators.from_dict(pmargin_get_um_api_trading_status_v1_resp_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


