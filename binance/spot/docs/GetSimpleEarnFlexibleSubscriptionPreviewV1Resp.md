# GetSimpleEarnFlexibleSubscriptionPreviewV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_drop_asset** | **str** |  | [optional] 
**est_daily_airdrop_rewards** | **str** |  | [optional] 
**est_daily_bonus_rewards** | **str** |  | [optional] 
**est_daily_real_time_rewards** | **str** |  | [optional] 
**reward_asset** | **str** |  | [optional] 
**total_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_flexible_subscription_preview_v1_resp import GetSimpleEarnFlexibleSubscriptionPreviewV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnFlexibleSubscriptionPreviewV1Resp from a JSON string
get_simple_earn_flexible_subscription_preview_v1_resp_instance = GetSimpleEarnFlexibleSubscriptionPreviewV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnFlexibleSubscriptionPreviewV1Resp.to_json())

# convert the object into a dict
get_simple_earn_flexible_subscription_preview_v1_resp_dict = get_simple_earn_flexible_subscription_preview_v1_resp_instance.to_dict()
# create an instance of GetSimpleEarnFlexibleSubscriptionPreviewV1Resp from a dict
get_simple_earn_flexible_subscription_preview_v1_resp_from_dict = GetSimpleEarnFlexibleSubscriptionPreviewV1Resp.from_dict(get_simple_earn_flexible_subscription_preview_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


