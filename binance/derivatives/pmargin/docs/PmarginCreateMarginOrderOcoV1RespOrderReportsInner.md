# PmarginCreateMarginOrderOcoV1RespOrderReportsInner


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
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_margin_order_oco_v1_resp_order_reports_inner import PmarginCreateMarginOrderOcoV1RespOrderReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateMarginOrderOcoV1RespOrderReportsInner from a JSON string
pmargin_create_margin_order_oco_v1_resp_order_reports_inner_instance = PmarginCreateMarginOrderOcoV1RespOrderReportsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateMarginOrderOcoV1RespOrderReportsInner.to_json())

# convert the object into a dict
pmargin_create_margin_order_oco_v1_resp_order_reports_inner_dict = pmargin_create_margin_order_oco_v1_resp_order_reports_inner_instance.to_dict()
# create an instance of PmarginCreateMarginOrderOcoV1RespOrderReportsInner from a dict
pmargin_create_margin_order_oco_v1_resp_order_reports_inner_from_dict = PmarginCreateMarginOrderOcoV1RespOrderReportsInner.from_dict(pmargin_create_margin_order_oco_v1_resp_order_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


