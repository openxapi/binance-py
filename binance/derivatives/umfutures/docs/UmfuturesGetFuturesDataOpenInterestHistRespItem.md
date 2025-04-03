# UmfuturesGetFuturesDataOpenInterestHistRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum_open_interest** | **str** |  | [optional] 
**sum_open_interest_value** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_futures_data_open_interest_hist_resp_item import UmfuturesGetFuturesDataOpenInterestHistRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetFuturesDataOpenInterestHistRespItem from a JSON string
umfutures_get_futures_data_open_interest_hist_resp_item_instance = UmfuturesGetFuturesDataOpenInterestHistRespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetFuturesDataOpenInterestHistRespItem.to_json())

# convert the object into a dict
umfutures_get_futures_data_open_interest_hist_resp_item_dict = umfutures_get_futures_data_open_interest_hist_resp_item_instance.to_dict()
# create an instance of UmfuturesGetFuturesDataOpenInterestHistRespItem from a dict
umfutures_get_futures_data_open_interest_hist_resp_item_from_dict = UmfuturesGetFuturesDataOpenInterestHistRespItem.from_dict(umfutures_get_futures_data_open_interest_hist_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


