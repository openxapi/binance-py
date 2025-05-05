# GetMarginInterestRateHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**daily_interest_rate** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**vip_level** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_interest_rate_history_v1_resp_item import GetMarginInterestRateHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginInterestRateHistoryV1RespItem from a JSON string
get_margin_interest_rate_history_v1_resp_item_instance = GetMarginInterestRateHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginInterestRateHistoryV1RespItem.to_json())

# convert the object into a dict
get_margin_interest_rate_history_v1_resp_item_dict = get_margin_interest_rate_history_v1_resp_item_instance.to_dict()
# create an instance of GetMarginInterestRateHistoryV1RespItem from a dict
get_margin_interest_rate_history_v1_resp_item_from_dict = GetMarginInterestRateHistoryV1RespItem.from_dict(get_margin_interest_rate_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


