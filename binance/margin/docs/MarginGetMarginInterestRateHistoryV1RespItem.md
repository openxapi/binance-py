# MarginGetMarginInterestRateHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**daily_interest_rate** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**vip_level** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_interest_rate_history_v1_resp_item import MarginGetMarginInterestRateHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginInterestRateHistoryV1RespItem from a JSON string
margin_get_margin_interest_rate_history_v1_resp_item_instance = MarginGetMarginInterestRateHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginInterestRateHistoryV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_interest_rate_history_v1_resp_item_dict = margin_get_margin_interest_rate_history_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginInterestRateHistoryV1RespItem from a dict
margin_get_margin_interest_rate_history_v1_resp_item_from_dict = MarginGetMarginInterestRateHistoryV1RespItem.from_dict(margin_get_margin_interest_rate_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


