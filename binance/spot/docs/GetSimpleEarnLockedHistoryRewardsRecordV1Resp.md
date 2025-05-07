# GetSimpleEarnLockedHistoryRewardsRecordV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner]**](GetSimpleEarnLockedHistoryRewardsRecordV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_history_rewards_record_v1_resp import GetSimpleEarnLockedHistoryRewardsRecordV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedHistoryRewardsRecordV1Resp from a JSON string
get_simple_earn_locked_history_rewards_record_v1_resp_instance = GetSimpleEarnLockedHistoryRewardsRecordV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedHistoryRewardsRecordV1Resp.to_json())

# convert the object into a dict
get_simple_earn_locked_history_rewards_record_v1_resp_dict = get_simple_earn_locked_history_rewards_record_v1_resp_instance.to_dict()
# create an instance of GetSimpleEarnLockedHistoryRewardsRecordV1Resp from a dict
get_simple_earn_locked_history_rewards_record_v1_resp_from_dict = GetSimpleEarnLockedHistoryRewardsRecordV1Resp.from_dict(get_simple_earn_locked_history_rewards_record_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


