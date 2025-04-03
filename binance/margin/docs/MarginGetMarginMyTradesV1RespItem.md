# MarginGetMarginMyTradesV1RespItem


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
from binance.margin.models.margin_get_margin_my_trades_v1_resp_item import MarginGetMarginMyTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginMyTradesV1RespItem from a JSON string
margin_get_margin_my_trades_v1_resp_item_instance = MarginGetMarginMyTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginMyTradesV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_my_trades_v1_resp_item_dict = margin_get_margin_my_trades_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginMyTradesV1RespItem from a dict
margin_get_margin_my_trades_v1_resp_item_from_dict = MarginGetMarginMyTradesV1RespItem.from_dict(margin_get_margin_my_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


