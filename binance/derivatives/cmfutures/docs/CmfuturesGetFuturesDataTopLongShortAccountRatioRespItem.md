# CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem


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
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_top_long_short_account_ratio_resp_item import CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem from a JSON string
cmfutures_get_futures_data_top_long_short_account_ratio_resp_item_instance = CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.to_json())

# convert the object into a dict
cmfutures_get_futures_data_top_long_short_account_ratio_resp_item_dict = cmfutures_get_futures_data_top_long_short_account_ratio_resp_item_instance.to_dict()
# create an instance of CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem from a dict
cmfutures_get_futures_data_top_long_short_account_ratio_resp_item_from_dict = CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.from_dict(cmfutures_get_futures_data_top_long_short_account_ratio_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


