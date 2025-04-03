# SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloc_id** | **object** |  | [optional] 
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**trade_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_cancel_replace_v3_new_order_resp_fills_inner import SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner from a JSON string
spot_create_order_cancel_replace_v3_new_order_resp_fills_inner_instance = SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner.to_json())

# convert the object into a dict
spot_create_order_cancel_replace_v3_new_order_resp_fills_inner_dict = spot_create_order_cancel_replace_v3_new_order_resp_fills_inner_instance.to_dict()
# create an instance of SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner from a dict
spot_create_order_cancel_replace_v3_new_order_resp_fills_inner_from_dict = SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner.from_dict(spot_create_order_cancel_replace_v3_new_order_resp_fills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


