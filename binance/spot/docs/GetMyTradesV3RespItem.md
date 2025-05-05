# GetMyTradesV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_best_match** | **bool** |  | [optional] 
**is_buyer** | **bool** |  | [optional] 
**is_maker** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_my_trades_v3_resp_item import GetMyTradesV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyTradesV3RespItem from a JSON string
get_my_trades_v3_resp_item_instance = GetMyTradesV3RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMyTradesV3RespItem.to_json())

# convert the object into a dict
get_my_trades_v3_resp_item_dict = get_my_trades_v3_resp_item_instance.to_dict()
# create an instance of GetMyTradesV3RespItem from a dict
get_my_trades_v3_resp_item_from_dict = GetMyTradesV3RespItem.from_dict(get_my_trades_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


