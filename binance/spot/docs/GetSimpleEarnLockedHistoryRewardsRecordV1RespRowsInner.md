# GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**lock_period** | **str** |  | [optional] 
**position_id** | **int** |  | [optional] 
**time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_history_rewards_record_v1_resp_rows_inner import GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner from a JSON string
get_simple_earn_locked_history_rewards_record_v1_resp_rows_inner_instance = GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_locked_history_rewards_record_v1_resp_rows_inner_dict = get_simple_earn_locked_history_rewards_record_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner from a dict
get_simple_earn_locked_history_rewards_record_v1_resp_rows_inner_from_dict = GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner.from_dict(get_simple_earn_locked_history_rewards_record_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


