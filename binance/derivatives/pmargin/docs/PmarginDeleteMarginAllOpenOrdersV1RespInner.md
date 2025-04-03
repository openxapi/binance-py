# PmarginDeleteMarginAllOpenOrdersV1RespInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**iceberg_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_reports** | [**List[PmarginDeleteMarginAllOpenOrdersV1RespOrder]**](PmarginDeleteMarginAllOpenOrdersV1RespOrder.md) |  | [optional] 
**orders** | [**List[PmarginCreateMarginOrderOcoV1RespOrdersInner]**](PmarginCreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_delete_margin_all_open_orders_v1_resp_inner import PmarginDeleteMarginAllOpenOrdersV1RespInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginDeleteMarginAllOpenOrdersV1RespInner from a JSON string
pmargin_delete_margin_all_open_orders_v1_resp_inner_instance = PmarginDeleteMarginAllOpenOrdersV1RespInner.from_json(json)
# print the JSON string representation of the object
print(PmarginDeleteMarginAllOpenOrdersV1RespInner.to_json())

# convert the object into a dict
pmargin_delete_margin_all_open_orders_v1_resp_inner_dict = pmargin_delete_margin_all_open_orders_v1_resp_inner_instance.to_dict()
# create an instance of PmarginDeleteMarginAllOpenOrdersV1RespInner from a dict
pmargin_delete_margin_all_open_orders_v1_resp_inner_from_dict = PmarginDeleteMarginAllOpenOrdersV1RespInner.from_dict(pmargin_delete_margin_all_open_orders_v1_resp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


