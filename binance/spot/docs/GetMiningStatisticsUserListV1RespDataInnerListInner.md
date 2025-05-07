# GetMiningStatisticsUserListV1RespDataInnerListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashrate** | **str** |  | [optional] 
**reject** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_statistics_user_list_v1_resp_data_inner_list_inner import GetMiningStatisticsUserListV1RespDataInnerListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningStatisticsUserListV1RespDataInnerListInner from a JSON string
get_mining_statistics_user_list_v1_resp_data_inner_list_inner_instance = GetMiningStatisticsUserListV1RespDataInnerListInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningStatisticsUserListV1RespDataInnerListInner.to_json())

# convert the object into a dict
get_mining_statistics_user_list_v1_resp_data_inner_list_inner_dict = get_mining_statistics_user_list_v1_resp_data_inner_list_inner_instance.to_dict()
# create an instance of GetMiningStatisticsUserListV1RespDataInnerListInner from a dict
get_mining_statistics_user_list_v1_resp_data_inner_list_inner_from_dict = GetMiningStatisticsUserListV1RespDataInnerListInner.from_dict(get_mining_statistics_user_list_v1_resp_data_inner_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


