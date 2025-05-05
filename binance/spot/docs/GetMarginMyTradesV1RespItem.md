# GetMarginMyTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_best_match** | **bool** |  | [optional] 
**is_buyer** | **bool** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**is_maker** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_my_trades_v1_resp_item import GetMarginMyTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginMyTradesV1RespItem from a JSON string
get_margin_my_trades_v1_resp_item_instance = GetMarginMyTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginMyTradesV1RespItem.to_json())

# convert the object into a dict
get_margin_my_trades_v1_resp_item_dict = get_margin_my_trades_v1_resp_item_instance.to_dict()
# create an instance of GetMarginMyTradesV1RespItem from a dict
get_margin_my_trades_v1_resp_item_from_dict = GetMarginMyTradesV1RespItem.from_dict(get_margin_my_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


