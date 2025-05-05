# GetFuturesDataOpenInterestHistRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum_open_interest** | **str** |  | [optional] 
**sum_open_interest_value** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_futures_data_open_interest_hist_resp_item import GetFuturesDataOpenInterestHistRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetFuturesDataOpenInterestHistRespItem from a JSON string
get_futures_data_open_interest_hist_resp_item_instance = GetFuturesDataOpenInterestHistRespItem.from_json(json)
# print the JSON string representation of the object
print(GetFuturesDataOpenInterestHistRespItem.to_json())

# convert the object into a dict
get_futures_data_open_interest_hist_resp_item_dict = get_futures_data_open_interest_hist_resp_item_instance.to_dict()
# create an instance of GetFuturesDataOpenInterestHistRespItem from a dict
get_futures_data_open_interest_hist_resp_item_from_dict = GetFuturesDataOpenInterestHistRespItem.from_dict(get_futures_data_open_interest_hist_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


