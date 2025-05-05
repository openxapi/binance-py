# GetTradesV3RespItem


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
from binance.spot.models.get_trades_v3_resp_item import GetTradesV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetTradesV3RespItem from a JSON string
get_trades_v3_resp_item_instance = GetTradesV3RespItem.from_json(json)
# print the JSON string representation of the object
print(GetTradesV3RespItem.to_json())

# convert the object into a dict
get_trades_v3_resp_item_dict = get_trades_v3_resp_item_instance.to_dict()
# create an instance of GetTradesV3RespItem from a dict
get_trades_v3_resp_item_from_dict = GetTradesV3RespItem.from_dict(get_trades_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


