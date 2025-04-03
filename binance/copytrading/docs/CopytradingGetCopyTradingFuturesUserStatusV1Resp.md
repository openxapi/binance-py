# CopytradingGetCopyTradingFuturesUserStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**CopytradingGetCopyTradingFuturesUserStatusV1RespData**](CopytradingGetCopyTradingFuturesUserStatusV1RespData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.copytrading.models.copytrading_get_copy_trading_futures_user_status_v1_resp import CopytradingGetCopyTradingFuturesUserStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CopytradingGetCopyTradingFuturesUserStatusV1Resp from a JSON string
copytrading_get_copy_trading_futures_user_status_v1_resp_instance = CopytradingGetCopyTradingFuturesUserStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(CopytradingGetCopyTradingFuturesUserStatusV1Resp.to_json())

# convert the object into a dict
copytrading_get_copy_trading_futures_user_status_v1_resp_dict = copytrading_get_copy_trading_futures_user_status_v1_resp_instance.to_dict()
# create an instance of CopytradingGetCopyTradingFuturesUserStatusV1Resp from a dict
copytrading_get_copy_trading_futures_user_status_v1_resp_from_dict = CopytradingGetCopyTradingFuturesUserStatusV1Resp.from_dict(copytrading_get_copy_trading_futures_user_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


