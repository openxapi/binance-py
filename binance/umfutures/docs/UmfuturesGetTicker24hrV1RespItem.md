# UmfuturesGetTicker24hrV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_time** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**first_id** | **int** |  | [optional] 
**high_price** | **str** |  | [optional] 
**last_id** | **int** |  | [optional] 
**last_price** | **str** |  | [optional] 
**last_qty** | **str** |  | [optional] 
**low_price** | **str** |  | [optional] 
**open_price** | **str** |  | [optional] 
**open_time** | **int** |  | [optional] 
**price_change** | **str** |  | [optional] 
**price_change_percent** | **str** |  | [optional] 
**quote_volume** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**weighted_avg_price** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_ticker24hr_v1_resp_item import UmfuturesGetTicker24hrV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetTicker24hrV1RespItem from a JSON string
umfutures_get_ticker24hr_v1_resp_item_instance = UmfuturesGetTicker24hrV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetTicker24hrV1RespItem.to_json())

# convert the object into a dict
umfutures_get_ticker24hr_v1_resp_item_dict = umfutures_get_ticker24hr_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetTicker24hrV1RespItem from a dict
umfutures_get_ticker24hr_v1_resp_item_from_dict = UmfuturesGetTicker24hrV1RespItem.from_dict(umfutures_get_ticker24hr_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


