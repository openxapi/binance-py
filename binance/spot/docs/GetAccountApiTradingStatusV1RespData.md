# GetAccountApiTradingStatusV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_locked** | **bool** |  | [optional] 
**planned_recover_time** | **int** |  | [optional] 
**trigger_condition** | [**GetAccountApiTradingStatusV1RespDataTriggerCondition**](GetAccountApiTradingStatusV1RespDataTriggerCondition.md) |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_account_api_trading_status_v1_resp_data import GetAccountApiTradingStatusV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountApiTradingStatusV1RespData from a JSON string
get_account_api_trading_status_v1_resp_data_instance = GetAccountApiTradingStatusV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetAccountApiTradingStatusV1RespData.to_json())

# convert the object into a dict
get_account_api_trading_status_v1_resp_data_dict = get_account_api_trading_status_v1_resp_data_instance.to_dict()
# create an instance of GetAccountApiTradingStatusV1RespData from a dict
get_account_api_trading_status_v1_resp_data_from_dict = GetAccountApiTradingStatusV1RespData.from_dict(get_account_api_trading_status_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


