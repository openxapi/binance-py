# MarginCreateMarginOrderV1RespFillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**trade_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.margin_create_margin_order_v1_resp_fills_inner import MarginCreateMarginOrderV1RespFillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginCreateMarginOrderV1RespFillsInner from a JSON string
margin_create_margin_order_v1_resp_fills_inner_instance = MarginCreateMarginOrderV1RespFillsInner.from_json(json)
# print the JSON string representation of the object
print(MarginCreateMarginOrderV1RespFillsInner.to_json())

# convert the object into a dict
margin_create_margin_order_v1_resp_fills_inner_dict = margin_create_margin_order_v1_resp_fills_inner_instance.to_dict()
# create an instance of MarginCreateMarginOrderV1RespFillsInner from a dict
margin_create_margin_order_v1_resp_fills_inner_from_dict = MarginCreateMarginOrderV1RespFillsInner.from_dict(margin_create_margin_order_v1_resp_fills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


