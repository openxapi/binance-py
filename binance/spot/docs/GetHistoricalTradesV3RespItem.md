# GetHistoricalTradesV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_best_match** | **bool** |  | [optional] 
**is_buyer_maker** | **bool** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_historical_trades_v3_resp_item import GetHistoricalTradesV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistoricalTradesV3RespItem from a JSON string
get_historical_trades_v3_resp_item_instance = GetHistoricalTradesV3RespItem.from_json(json)
# print the JSON string representation of the object
print(GetHistoricalTradesV3RespItem.to_json())

# convert the object into a dict
get_historical_trades_v3_resp_item_dict = get_historical_trades_v3_resp_item_instance.to_dict()
# create an instance of GetHistoricalTradesV3RespItem from a dict
get_historical_trades_v3_resp_item_from_dict = GetHistoricalTradesV3RespItem.from_dict(get_historical_trades_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


