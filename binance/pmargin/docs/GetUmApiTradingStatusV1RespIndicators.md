# GetUmApiTradingStatusV1RespIndicators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btcusdt** | [**List[GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner]**](GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner.md) |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_api_trading_status_v1_resp_indicators import GetUmApiTradingStatusV1RespIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmApiTradingStatusV1RespIndicators from a JSON string
get_um_api_trading_status_v1_resp_indicators_instance = GetUmApiTradingStatusV1RespIndicators.from_json(json)
# print the JSON string representation of the object
print(GetUmApiTradingStatusV1RespIndicators.to_json())

# convert the object into a dict
get_um_api_trading_status_v1_resp_indicators_dict = get_um_api_trading_status_v1_resp_indicators_instance.to_dict()
# create an instance of GetUmApiTradingStatusV1RespIndicators from a dict
get_um_api_trading_status_v1_resp_indicators_from_dict = GetUmApiTradingStatusV1RespIndicators.from_dict(get_um_api_trading_status_v1_resp_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


