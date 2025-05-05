# GetFuturesDataTopLongShortAccountRatioRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_account** | **str** |  | [optional] 
**long_short_ratio** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**short_account** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_futures_data_top_long_short_account_ratio_resp_item import GetFuturesDataTopLongShortAccountRatioRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetFuturesDataTopLongShortAccountRatioRespItem from a JSON string
get_futures_data_top_long_short_account_ratio_resp_item_instance = GetFuturesDataTopLongShortAccountRatioRespItem.from_json(json)
# print the JSON string representation of the object
print(GetFuturesDataTopLongShortAccountRatioRespItem.to_json())

# convert the object into a dict
get_futures_data_top_long_short_account_ratio_resp_item_dict = get_futures_data_top_long_short_account_ratio_resp_item_instance.to_dict()
# create an instance of GetFuturesDataTopLongShortAccountRatioRespItem from a dict
get_futures_data_top_long_short_account_ratio_resp_item_from_dict = GetFuturesDataTopLongShortAccountRatioRespItem.from_dict(get_futures_data_top_long_short_account_ratio_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


