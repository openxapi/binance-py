# DeleteMarginOrderListV1RespOrderReportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.delete_margin_order_list_v1_resp_order_reports_inner import DeleteMarginOrderListV1RespOrderReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMarginOrderListV1RespOrderReportsInner from a JSON string
delete_margin_order_list_v1_resp_order_reports_inner_instance = DeleteMarginOrderListV1RespOrderReportsInner.from_json(json)
# print the JSON string representation of the object
print(DeleteMarginOrderListV1RespOrderReportsInner.to_json())

# convert the object into a dict
delete_margin_order_list_v1_resp_order_reports_inner_dict = delete_margin_order_list_v1_resp_order_reports_inner_instance.to_dict()
# create an instance of DeleteMarginOrderListV1RespOrderReportsInner from a dict
delete_margin_order_list_v1_resp_order_reports_inner_from_dict = DeleteMarginOrderListV1RespOrderReportsInner.from_dict(delete_margin_order_list_v1_resp_order_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


