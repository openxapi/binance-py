# CmfuturesGetFuturesDataOpenInterestHistRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**sum_open_interest** | **str** |  | [optional] 
**sum_open_interest_value** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_open_interest_hist_resp_item import CmfuturesGetFuturesDataOpenInterestHistRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetFuturesDataOpenInterestHistRespItem from a JSON string
cmfutures_get_futures_data_open_interest_hist_resp_item_instance = CmfuturesGetFuturesDataOpenInterestHistRespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetFuturesDataOpenInterestHistRespItem.to_json())

# convert the object into a dict
cmfutures_get_futures_data_open_interest_hist_resp_item_dict = cmfutures_get_futures_data_open_interest_hist_resp_item_instance.to_dict()
# create an instance of CmfuturesGetFuturesDataOpenInterestHistRespItem from a dict
cmfutures_get_futures_data_open_interest_hist_resp_item_from_dict = CmfuturesGetFuturesDataOpenInterestHistRespItem.from_dict(cmfutures_get_futures_data_open_interest_hist_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


