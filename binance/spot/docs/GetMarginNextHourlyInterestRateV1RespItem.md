# GetMarginNextHourlyInterestRateV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**next_hourly_interest_rate** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_next_hourly_interest_rate_v1_resp_item import GetMarginNextHourlyInterestRateV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginNextHourlyInterestRateV1RespItem from a JSON string
get_margin_next_hourly_interest_rate_v1_resp_item_instance = GetMarginNextHourlyInterestRateV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginNextHourlyInterestRateV1RespItem.to_json())

# convert the object into a dict
get_margin_next_hourly_interest_rate_v1_resp_item_dict = get_margin_next_hourly_interest_rate_v1_resp_item_instance.to_dict()
# create an instance of GetMarginNextHourlyInterestRateV1RespItem from a dict
get_margin_next_hourly_interest_rate_v1_resp_item_from_dict = GetMarginNextHourlyInterestRateV1RespItem.from_dict(get_margin_next_hourly_interest_rate_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


