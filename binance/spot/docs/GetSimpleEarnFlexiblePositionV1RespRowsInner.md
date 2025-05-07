# GetSimpleEarnFlexiblePositionV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_drop_asset** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**auto_subscribe** | **bool** |  | [optional] 
**can_redeem** | **bool** |  | [optional] 
**collateral_amount** | **str** |  | [optional] 
**cumulative_bonus_rewards** | **str** |  | [optional] 
**cumulative_real_time_rewards** | **str** |  | [optional] 
**cumulative_total_rewards** | **str** |  | [optional] 
**latest_annual_percentage_rate** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**tier_annual_percentage_rate** | [**GetSimpleEarnFlexibleListV1RespRowsInnerTierAnnualPercentageRate**](GetSimpleEarnFlexibleListV1RespRowsInnerTierAnnualPercentageRate.md) |  | [optional] 
**total_amount** | **str** |  | [optional] 
**yesterday_airdrop_percentage_rate** | **str** |  | [optional] 
**yesterday_real_time_rewards** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_flexible_position_v1_resp_rows_inner import GetSimpleEarnFlexiblePositionV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnFlexiblePositionV1RespRowsInner from a JSON string
get_simple_earn_flexible_position_v1_resp_rows_inner_instance = GetSimpleEarnFlexiblePositionV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnFlexiblePositionV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_flexible_position_v1_resp_rows_inner_dict = get_simple_earn_flexible_position_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnFlexiblePositionV1RespRowsInner from a dict
get_simple_earn_flexible_position_v1_resp_rows_inner_from_dict = GetSimpleEarnFlexiblePositionV1RespRowsInner.from_dict(get_simple_earn_flexible_position_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


