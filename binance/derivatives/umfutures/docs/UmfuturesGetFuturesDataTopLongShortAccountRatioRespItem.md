# UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_account** | **str** |  | [optional] 
**long_short_ratio** | **str** |  | [optional] 
**short_account** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_futures_data_top_long_short_account_ratio_resp_item import UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem from a JSON string
umfutures_get_futures_data_top_long_short_account_ratio_resp_item_instance = UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.to_json())

# convert the object into a dict
umfutures_get_futures_data_top_long_short_account_ratio_resp_item_dict = umfutures_get_futures_data_top_long_short_account_ratio_resp_item_instance.to_dict()
# create an instance of UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem from a dict
umfutures_get_futures_data_top_long_short_account_ratio_resp_item_from_dict = UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.from_dict(umfutures_get_futures_data_top_long_short_account_ratio_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


