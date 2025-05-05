# GetUmApiTradingStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicators** | [**GetUmApiTradingStatusV1RespIndicators**](GetUmApiTradingStatusV1RespIndicators.md) |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_api_trading_status_v1_resp import GetUmApiTradingStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmApiTradingStatusV1Resp from a JSON string
get_um_api_trading_status_v1_resp_instance = GetUmApiTradingStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetUmApiTradingStatusV1Resp.to_json())

# convert the object into a dict
get_um_api_trading_status_v1_resp_dict = get_um_api_trading_status_v1_resp_instance.to_dict()
# create an instance of GetUmApiTradingStatusV1Resp from a dict
get_um_api_trading_status_v1_resp_from_dict = GetUmApiTradingStatusV1Resp.from_dict(get_um_api_trading_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


