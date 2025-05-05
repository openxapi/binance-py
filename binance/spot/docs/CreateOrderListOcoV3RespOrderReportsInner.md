# CreateOrderListOcoV3RespOrderReportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**iceberg_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_quote_order_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**working_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_order_list_oco_v3_resp_order_reports_inner import CreateOrderListOcoV3RespOrderReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderListOcoV3RespOrderReportsInner from a JSON string
create_order_list_oco_v3_resp_order_reports_inner_instance = CreateOrderListOcoV3RespOrderReportsInner.from_json(json)
# print the JSON string representation of the object
print(CreateOrderListOcoV3RespOrderReportsInner.to_json())

# convert the object into a dict
create_order_list_oco_v3_resp_order_reports_inner_dict = create_order_list_oco_v3_resp_order_reports_inner_instance.to_dict()
# create an instance of CreateOrderListOcoV3RespOrderReportsInner from a dict
create_order_list_oco_v3_resp_order_reports_inner_from_dict = CreateOrderListOcoV3RespOrderReportsInner.from_dict(create_order_list_oco_v3_resp_order_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


