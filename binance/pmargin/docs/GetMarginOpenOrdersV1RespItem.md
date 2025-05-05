# GetMarginOpenOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**iceberg_qty** | **str** |  | [optional] 
**is_working** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**prevented_match_id** | **object** |  | [optional] 
**prevented_quantity** | **object** |  | [optional] 
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
from binance.pmargin.models.get_margin_open_orders_v1_resp_item import GetMarginOpenOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginOpenOrdersV1RespItem from a JSON string
get_margin_open_orders_v1_resp_item_instance = GetMarginOpenOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginOpenOrdersV1RespItem.to_json())

# convert the object into a dict
get_margin_open_orders_v1_resp_item_dict = get_margin_open_orders_v1_resp_item_instance.to_dict()
# create an instance of GetMarginOpenOrdersV1RespItem from a dict
get_margin_open_orders_v1_resp_item_from_dict = GetMarginOpenOrdersV1RespItem.from_dict(get_margin_open_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


