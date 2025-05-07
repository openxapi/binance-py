# GetSimpleEarnLockedHistoryRedemptionRecordV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**deliver_date** | **str** |  | [optional] 
**est_extra_reward_amt** | **str** |  | [optional] 
**extra_reward_asset** | **str** |  | [optional] 
**is_complete** | **bool** |  | [optional] 
**lock_period** | **str** |  | [optional] 
**loss_amount** | **str** |  | [optional] 
**original_amount** | **str** |  | [optional] 
**position_id** | **int** |  | [optional] 
**redeem_id** | **int** |  | [optional] 
**reward_amt** | **str** |  | [optional] 
**reward_asset** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_history_redemption_record_v1_resp_rows_inner import GetSimpleEarnLockedHistoryRedemptionRecordV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedHistoryRedemptionRecordV1RespRowsInner from a JSON string
get_simple_earn_locked_history_redemption_record_v1_resp_rows_inner_instance = GetSimpleEarnLockedHistoryRedemptionRecordV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedHistoryRedemptionRecordV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_locked_history_redemption_record_v1_resp_rows_inner_dict = get_simple_earn_locked_history_redemption_record_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnLockedHistoryRedemptionRecordV1RespRowsInner from a dict
get_simple_earn_locked_history_redemption_record_v1_resp_rows_inner_from_dict = GetSimpleEarnLockedHistoryRedemptionRecordV1RespRowsInner.from_dict(get_simple_earn_locked_history_redemption_record_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


