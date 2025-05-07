# GetSimpleEarnLockedPositionV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apy** | **str** |  | [optional] 
**accrual_days** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**auto_subscribe** | **bool** |  | [optional] 
**boost_apr** | **str** |  | [optional] 
**boost_reward_asset** | **str** |  | [optional] 
**can_fast_redemption** | **bool** |  | [optional] 
**can_re_stake** | **bool** |  | [optional] 
**can_redeem_early** | **bool** |  | [optional] 
**deliver_date** | **str** |  | [optional] 
**duration** | **str** |  | [optional] 
**est_extra_reward_amt** | **str** |  | [optional] 
**extra_reward_apr** | **str** |  | [optional] 
**extra_reward_asset** | **str** |  | [optional] 
**next_pay** | **str** |  | [optional] 
**next_pay_date** | **str** |  | [optional] 
**parent_position_id** | **int** |  | [optional] 
**partial_amt_deliver_date** | **str** |  | [optional] 
**pay_period** | **str** |  | [optional] 
**position_id** | **int** |  | [optional] 
**project_id** | **str** |  | [optional] 
**purchase_time** | **str** |  | [optional] 
**redeem_amount_early** | **str** |  | [optional] 
**redeem_period** | **str** |  | [optional] 
**redeem_to** | **str** |  | [optional] 
**redeeming_amt** | **str** |  | [optional] 
**reward_amt** | **str** |  | [optional] 
**reward_asset** | **str** |  | [optional] 
**rewards_end_date** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_boost_reward_amt** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_position_v1_resp_rows_inner import GetSimpleEarnLockedPositionV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedPositionV1RespRowsInner from a JSON string
get_simple_earn_locked_position_v1_resp_rows_inner_instance = GetSimpleEarnLockedPositionV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedPositionV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_locked_position_v1_resp_rows_inner_dict = get_simple_earn_locked_position_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnLockedPositionV1RespRowsInner from a dict
get_simple_earn_locked_position_v1_resp_rows_inner_from_dict = GetSimpleEarnLockedPositionV1RespRowsInner.from_dict(get_simple_earn_locked_position_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


