# MarginGetMarginAllOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**iceberg_qty** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**is_working** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_all_orders_v1_resp_item import MarginGetMarginAllOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginAllOrdersV1RespItem from a JSON string
margin_get_margin_all_orders_v1_resp_item_instance = MarginGetMarginAllOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginAllOrdersV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_all_orders_v1_resp_item_dict = margin_get_margin_all_orders_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginAllOrdersV1RespItem from a dict
margin_get_margin_all_orders_v1_resp_item_from_dict = MarginGetMarginAllOrdersV1RespItem.from_dict(margin_get_margin_all_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


