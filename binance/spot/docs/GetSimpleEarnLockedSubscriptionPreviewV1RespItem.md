# GetSimpleEarnLockedSubscriptionPreviewV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boost_reward_asset** | **str** |  | [optional] 
**deliver_date** | **str** |  | [optional] 
**est_daily_reward_amt** | **str** |  | [optional] 
**est_total_extra_reward_amt** | **str** |  | [optional] 
**extra_reward_asset** | **str** |  | [optional] 
**next_pay** | **str** |  | [optional] 
**next_pay_date** | **str** |  | [optional] 
**next_subscription_date** | **str** |  | [optional] 
**reward_asset** | **str** |  | [optional] 
**rewards_end_date** | **str** |  | [optional] 
**total_reward_amt** | **str** |  | [optional] 
**value_date** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_subscription_preview_v1_resp_item import GetSimpleEarnLockedSubscriptionPreviewV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedSubscriptionPreviewV1RespItem from a JSON string
get_simple_earn_locked_subscription_preview_v1_resp_item_instance = GetSimpleEarnLockedSubscriptionPreviewV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedSubscriptionPreviewV1RespItem.to_json())

# convert the object into a dict
get_simple_earn_locked_subscription_preview_v1_resp_item_dict = get_simple_earn_locked_subscription_preview_v1_resp_item_instance.to_dict()
# create an instance of GetSimpleEarnLockedSubscriptionPreviewV1RespItem from a dict
get_simple_earn_locked_subscription_preview_v1_resp_item_from_dict = GetSimpleEarnLockedSubscriptionPreviewV1RespItem.from_dict(get_simple_earn_locked_subscription_preview_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


