# MarginCreateMarginOrderOcoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**margin_buy_borrow_amount** | **str** |  | [optional] 
**margin_buy_borrow_asset** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[MarginCreateMarginOrderOcoV1RespOrderReportsInner]**](MarginCreateMarginOrderOcoV1RespOrderReportsInner.md) |  | [optional] 
**orders** | [**List[MarginCreateMarginOrderOcoV1RespOrdersInner]**](MarginCreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_create_margin_order_oco_v1_resp import MarginCreateMarginOrderOcoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginCreateMarginOrderOcoV1Resp from a JSON string
margin_create_margin_order_oco_v1_resp_instance = MarginCreateMarginOrderOcoV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginCreateMarginOrderOcoV1Resp.to_json())

# convert the object into a dict
margin_create_margin_order_oco_v1_resp_dict = margin_create_margin_order_oco_v1_resp_instance.to_dict()
# create an instance of MarginCreateMarginOrderOcoV1Resp from a dict
margin_create_margin_order_oco_v1_resp_from_dict = MarginCreateMarginOrderOcoV1Resp.from_dict(margin_create_margin_order_oco_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


