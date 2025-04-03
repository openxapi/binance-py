# SpotGetTicker24hrV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_price** | **str** |  | [optional] 
**ask_qty** | **str** |  | [optional] 
**bid_price** | **str** |  | [optional] 
**bid_qty** | **str** |  | [optional] 
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
**prev_close_price** | **str** |  | [optional] 
**price_change** | **str** |  | [optional] 
**price_change_percent** | **str** |  | [optional] 
**quote_volume** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**weighted_avg_price** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_ticker24hr_v3_resp_item import SpotGetTicker24hrV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetTicker24hrV3RespItem from a JSON string
spot_get_ticker24hr_v3_resp_item_instance = SpotGetTicker24hrV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetTicker24hrV3RespItem.to_json())

# convert the object into a dict
spot_get_ticker24hr_v3_resp_item_dict = spot_get_ticker24hr_v3_resp_item_instance.to_dict()
# create an instance of SpotGetTicker24hrV3RespItem from a dict
spot_get_ticker24hr_v3_resp_item_from_dict = SpotGetTicker24hrV3RespItem.from_dict(spot_get_ticker24hr_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


