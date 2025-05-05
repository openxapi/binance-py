# GetCopyTradingFuturesUserStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**GetCopyTradingFuturesUserStatusV1RespData**](GetCopyTradingFuturesUserStatusV1RespData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_copy_trading_futures_user_status_v1_resp import GetCopyTradingFuturesUserStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetCopyTradingFuturesUserStatusV1Resp from a JSON string
get_copy_trading_futures_user_status_v1_resp_instance = GetCopyTradingFuturesUserStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetCopyTradingFuturesUserStatusV1Resp.to_json())

# convert the object into a dict
get_copy_trading_futures_user_status_v1_resp_dict = get_copy_trading_futures_user_status_v1_resp_instance.to_dict()
# create an instance of GetCopyTradingFuturesUserStatusV1Resp from a dict
get_copy_trading_futures_user_status_v1_resp_from_dict = GetCopyTradingFuturesUserStatusV1Resp.from_dict(get_copy_trading_futures_user_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


