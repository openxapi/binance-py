# GetMiningStatisticsUserStatusV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo** | **str** |  | [optional] 
**day_hash_rate** | **str** |  | [optional] 
**fifteen_min_hash_rate** | **str** |  | [optional] 
**invalid_num** | **int** |  | [optional] 
**profit_today** | [**GetMiningStatisticsUserStatusV1RespDataProfitToday**](GetMiningStatisticsUserStatusV1RespDataProfitToday.md) |  | [optional] 
**profit_yesterday** | [**GetMiningStatisticsUserStatusV1RespDataProfitToday**](GetMiningStatisticsUserStatusV1RespDataProfitToday.md) |  | [optional] 
**unit** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**valid_num** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_statistics_user_status_v1_resp_data import GetMiningStatisticsUserStatusV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningStatisticsUserStatusV1RespData from a JSON string
get_mining_statistics_user_status_v1_resp_data_instance = GetMiningStatisticsUserStatusV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetMiningStatisticsUserStatusV1RespData.to_json())

# convert the object into a dict
get_mining_statistics_user_status_v1_resp_data_dict = get_mining_statistics_user_status_v1_resp_data_instance.to_dict()
# create an instance of GetMiningStatisticsUserStatusV1RespData from a dict
get_mining_statistics_user_status_v1_resp_data_from_dict = GetMiningStatisticsUserStatusV1RespData.from_dict(get_mining_statistics_user_status_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


