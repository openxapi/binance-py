# GetSimpleEarnLockedHistorySubscriptionRecordV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**amt_from_funding** | **str** |  | [optional] 
**amt_from_spot** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**lock_period** | **str** |  | [optional] 
**position_id** | **int** |  | [optional] 
**project_id** | **str** |  | [optional] 
**purchase_id** | **str** |  | [optional] 
**source_account** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_history_subscription_record_v1_resp_rows_inner import GetSimpleEarnLockedHistorySubscriptionRecordV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedHistorySubscriptionRecordV1RespRowsInner from a JSON string
get_simple_earn_locked_history_subscription_record_v1_resp_rows_inner_instance = GetSimpleEarnLockedHistorySubscriptionRecordV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedHistorySubscriptionRecordV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_locked_history_subscription_record_v1_resp_rows_inner_dict = get_simple_earn_locked_history_subscription_record_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnLockedHistorySubscriptionRecordV1RespRowsInner from a dict
get_simple_earn_locked_history_subscription_record_v1_resp_rows_inner_from_dict = GetSimpleEarnLockedHistorySubscriptionRecordV1RespRowsInner.from_dict(get_simple_earn_locked_history_subscription_record_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


