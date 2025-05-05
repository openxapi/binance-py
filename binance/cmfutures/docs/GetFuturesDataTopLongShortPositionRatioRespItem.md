# GetFuturesDataTopLongShortPositionRatioRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_position** | **str** |  | [optional] 
**long_short_ratio** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**short_position** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_futures_data_top_long_short_position_ratio_resp_item import GetFuturesDataTopLongShortPositionRatioRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetFuturesDataTopLongShortPositionRatioRespItem from a JSON string
get_futures_data_top_long_short_position_ratio_resp_item_instance = GetFuturesDataTopLongShortPositionRatioRespItem.from_json(json)
# print the JSON string representation of the object
print(GetFuturesDataTopLongShortPositionRatioRespItem.to_json())

# convert the object into a dict
get_futures_data_top_long_short_position_ratio_resp_item_dict = get_futures_data_top_long_short_position_ratio_resp_item_instance.to_dict()
# create an instance of GetFuturesDataTopLongShortPositionRatioRespItem from a dict
get_futures_data_top_long_short_position_ratio_resp_item_from_dict = GetFuturesDataTopLongShortPositionRatioRespItem.from_dict(get_futures_data_top_long_short_position_ratio_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


