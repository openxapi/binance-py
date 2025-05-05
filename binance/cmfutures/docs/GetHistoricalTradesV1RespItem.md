# GetHistoricalTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_qty** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_buyer_maker** | **bool** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_historical_trades_v1_resp_item import GetHistoricalTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistoricalTradesV1RespItem from a JSON string
get_historical_trades_v1_resp_item_instance = GetHistoricalTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetHistoricalTradesV1RespItem.to_json())

# convert the object into a dict
get_historical_trades_v1_resp_item_dict = get_historical_trades_v1_resp_item_instance.to_dict()
# create an instance of GetHistoricalTradesV1RespItem from a dict
get_historical_trades_v1_resp_item_from_dict = GetHistoricalTradesV1RespItem.from_dict(get_historical_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


