# GetCopyTradingFuturesUserStatusV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_lead_trader** | **bool** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_copy_trading_futures_user_status_v1_resp_data import GetCopyTradingFuturesUserStatusV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetCopyTradingFuturesUserStatusV1RespData from a JSON string
get_copy_trading_futures_user_status_v1_resp_data_instance = GetCopyTradingFuturesUserStatusV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetCopyTradingFuturesUserStatusV1RespData.to_json())

# convert the object into a dict
get_copy_trading_futures_user_status_v1_resp_data_dict = get_copy_trading_futures_user_status_v1_resp_data_instance.to_dict()
# create an instance of GetCopyTradingFuturesUserStatusV1RespData from a dict
get_copy_trading_futures_user_status_v1_resp_data_from_dict = GetCopyTradingFuturesUserStatusV1RespData.from_dict(get_copy_trading_futures_user_status_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


