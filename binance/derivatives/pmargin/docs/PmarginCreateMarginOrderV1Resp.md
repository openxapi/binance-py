# PmarginCreateMarginOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fills** | [**List[PmarginCreateMarginOrderV1RespFillsInner]**](PmarginCreateMarginOrderV1RespFillsInner.md) |  | [optional] 
**margin_buy_borrow_amount** | **int** |  | [optional] 
**margin_buy_borrow_asset** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_margin_order_v1_resp import PmarginCreateMarginOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateMarginOrderV1Resp from a JSON string
pmargin_create_margin_order_v1_resp_instance = PmarginCreateMarginOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateMarginOrderV1Resp.to_json())

# convert the object into a dict
pmargin_create_margin_order_v1_resp_dict = pmargin_create_margin_order_v1_resp_instance.to_dict()
# create an instance of PmarginCreateMarginOrderV1Resp from a dict
pmargin_create_margin_order_v1_resp_from_dict = PmarginCreateMarginOrderV1Resp.from_dict(pmargin_create_margin_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


