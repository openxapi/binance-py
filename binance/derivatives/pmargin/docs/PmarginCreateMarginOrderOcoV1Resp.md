# PmarginCreateMarginOrderOcoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**margin_buy_borrow_amount** | **str** |  | [optional] 
**margin_buy_borrow_asset** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[PmarginCreateMarginOrderOcoV1RespOrderReportsInner]**](PmarginCreateMarginOrderOcoV1RespOrderReportsInner.md) |  | [optional] 
**orders** | [**List[PmarginCreateMarginOrderOcoV1RespOrdersInner]**](PmarginCreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_margin_order_oco_v1_resp import PmarginCreateMarginOrderOcoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateMarginOrderOcoV1Resp from a JSON string
pmargin_create_margin_order_oco_v1_resp_instance = PmarginCreateMarginOrderOcoV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateMarginOrderOcoV1Resp.to_json())

# convert the object into a dict
pmargin_create_margin_order_oco_v1_resp_dict = pmargin_create_margin_order_oco_v1_resp_instance.to_dict()
# create an instance of PmarginCreateMarginOrderOcoV1Resp from a dict
pmargin_create_margin_order_oco_v1_resp_from_dict = PmarginCreateMarginOrderOcoV1Resp.from_dict(pmargin_create_margin_order_oco_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


