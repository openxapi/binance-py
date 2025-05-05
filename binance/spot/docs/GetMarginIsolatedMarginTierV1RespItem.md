# GetMarginIsolatedMarginTierV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset_max_borrowable** | **str** |  | [optional] 
**effective_multiple** | **str** |  | [optional] 
**initial_risk_ratio** | **str** |  | [optional] 
**liquidation_risk_ratio** | **str** |  | [optional] 
**quote_asset_max_borrowable** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**tier** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_margin_tier_v1_resp_item import GetMarginIsolatedMarginTierV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedMarginTierV1RespItem from a JSON string
get_margin_isolated_margin_tier_v1_resp_item_instance = GetMarginIsolatedMarginTierV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedMarginTierV1RespItem.to_json())

# convert the object into a dict
get_margin_isolated_margin_tier_v1_resp_item_dict = get_margin_isolated_margin_tier_v1_resp_item_instance.to_dict()
# create an instance of GetMarginIsolatedMarginTierV1RespItem from a dict
get_margin_isolated_margin_tier_v1_resp_item_from_dict = GetMarginIsolatedMarginTierV1RespItem.from_dict(get_margin_isolated_margin_tier_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


