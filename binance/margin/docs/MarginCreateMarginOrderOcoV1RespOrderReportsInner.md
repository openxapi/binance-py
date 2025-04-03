# MarginCreateMarginOrderOcoV1RespOrderReportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_create_margin_order_oco_v1_resp_order_reports_inner import MarginCreateMarginOrderOcoV1RespOrderReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginCreateMarginOrderOcoV1RespOrderReportsInner from a JSON string
margin_create_margin_order_oco_v1_resp_order_reports_inner_instance = MarginCreateMarginOrderOcoV1RespOrderReportsInner.from_json(json)
# print the JSON string representation of the object
print(MarginCreateMarginOrderOcoV1RespOrderReportsInner.to_json())

# convert the object into a dict
margin_create_margin_order_oco_v1_resp_order_reports_inner_dict = margin_create_margin_order_oco_v1_resp_order_reports_inner_instance.to_dict()
# create an instance of MarginCreateMarginOrderOcoV1RespOrderReportsInner from a dict
margin_create_margin_order_oco_v1_resp_order_reports_inner_from_dict = MarginCreateMarginOrderOcoV1RespOrderReportsInner.from_dict(margin_create_margin_order_oco_v1_resp_order_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


