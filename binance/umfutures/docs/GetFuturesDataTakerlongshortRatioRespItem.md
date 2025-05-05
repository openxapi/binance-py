# GetFuturesDataTakerlongshortRatioRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buy_sell_ratio** | **str** |  | [optional] 
**buy_vol** | **str** |  | [optional] 
**sell_vol** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_futures_data_takerlongshort_ratio_resp_item import GetFuturesDataTakerlongshortRatioRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetFuturesDataTakerlongshortRatioRespItem from a JSON string
get_futures_data_takerlongshort_ratio_resp_item_instance = GetFuturesDataTakerlongshortRatioRespItem.from_json(json)
# print the JSON string representation of the object
print(GetFuturesDataTakerlongshortRatioRespItem.to_json())

# convert the object into a dict
get_futures_data_takerlongshort_ratio_resp_item_dict = get_futures_data_takerlongshort_ratio_resp_item_instance.to_dict()
# create an instance of GetFuturesDataTakerlongshortRatioRespItem from a dict
get_futures_data_takerlongshort_ratio_resp_item_from_dict = GetFuturesDataTakerlongshortRatioRespItem.from_dict(get_futures_data_takerlongshort_ratio_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


