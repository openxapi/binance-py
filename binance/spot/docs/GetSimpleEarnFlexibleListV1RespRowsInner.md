# GetSimpleEarnFlexibleListV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_drop_percentage_rate** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**can_purchase** | **bool** |  | [optional] 
**can_redeem** | **bool** |  | [optional] 
**hot** | **bool** |  | [optional] 
**is_sold_out** | **bool** |  | [optional] 
**latest_annual_percentage_rate** | **str** |  | [optional] 
**min_purchase_amount** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**subscription_start_time** | **str** |  | [optional] 
**tier_annual_percentage_rate** | [**GetSimpleEarnFlexibleListV1RespRowsInnerTierAnnualPercentageRate**](GetSimpleEarnFlexibleListV1RespRowsInnerTierAnnualPercentageRate.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_flexible_list_v1_resp_rows_inner import GetSimpleEarnFlexibleListV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnFlexibleListV1RespRowsInner from a JSON string
get_simple_earn_flexible_list_v1_resp_rows_inner_instance = GetSimpleEarnFlexibleListV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnFlexibleListV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_flexible_list_v1_resp_rows_inner_dict = get_simple_earn_flexible_list_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnFlexibleListV1RespRowsInner from a dict
get_simple_earn_flexible_list_v1_resp_rows_inner_from_dict = GetSimpleEarnFlexibleListV1RespRowsInner.from_dict(get_simple_earn_flexible_list_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


