# GetMiningStatisticsUserListV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GetMiningStatisticsUserListV1RespDataInnerListInner]**](GetMiningStatisticsUserListV1RespDataInnerListInner.md) |  | [optional] 
**type** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_statistics_user_list_v1_resp_data_inner import GetMiningStatisticsUserListV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningStatisticsUserListV1RespDataInner from a JSON string
get_mining_statistics_user_list_v1_resp_data_inner_instance = GetMiningStatisticsUserListV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningStatisticsUserListV1RespDataInner.to_json())

# convert the object into a dict
get_mining_statistics_user_list_v1_resp_data_inner_dict = get_mining_statistics_user_list_v1_resp_data_inner_instance.to_dict()
# create an instance of GetMiningStatisticsUserListV1RespDataInner from a dict
get_mining_statistics_user_list_v1_resp_data_inner_from_dict = GetMiningStatisticsUserListV1RespDataInner.from_dict(get_mining_statistics_user_list_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


