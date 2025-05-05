# GetTicker24hrV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_volume** | **str** |  | [optional] 
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
**pair** | **str** |  | [optional] 
**price_change** | **str** |  | [optional] 
**price_change_percent** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**weighted_avg_price** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_ticker24hr_v1_resp_item import GetTicker24hrV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetTicker24hrV1RespItem from a JSON string
get_ticker24hr_v1_resp_item_instance = GetTicker24hrV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetTicker24hrV1RespItem.to_json())

# convert the object into a dict
get_ticker24hr_v1_resp_item_dict = get_ticker24hr_v1_resp_item_instance.to_dict()
# create an instance of GetTicker24hrV1RespItem from a dict
get_ticker24hr_v1_resp_item_from_dict = GetTicker24hrV1RespItem.from_dict(get_ticker24hr_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


