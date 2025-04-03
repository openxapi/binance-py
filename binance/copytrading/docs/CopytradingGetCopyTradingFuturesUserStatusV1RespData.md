# CopytradingGetCopyTradingFuturesUserStatusV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_lead_trader** | **bool** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.copytrading.models.copytrading_get_copy_trading_futures_user_status_v1_resp_data import CopytradingGetCopyTradingFuturesUserStatusV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of CopytradingGetCopyTradingFuturesUserStatusV1RespData from a JSON string
copytrading_get_copy_trading_futures_user_status_v1_resp_data_instance = CopytradingGetCopyTradingFuturesUserStatusV1RespData.from_json(json)
# print the JSON string representation of the object
print(CopytradingGetCopyTradingFuturesUserStatusV1RespData.to_json())

# convert the object into a dict
copytrading_get_copy_trading_futures_user_status_v1_resp_data_dict = copytrading_get_copy_trading_futures_user_status_v1_resp_data_instance.to_dict()
# create an instance of CopytradingGetCopyTradingFuturesUserStatusV1RespData from a dict
copytrading_get_copy_trading_futures_user_status_v1_resp_data_from_dict = CopytradingGetCopyTradingFuturesUserStatusV1RespData.from_dict(copytrading_get_copy_trading_futures_user_status_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


