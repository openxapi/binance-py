# SpotCreateOrderCancelReplaceV3NewOrderResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fills** | [**List[SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner]**](SpotCreateOrderCancelReplaceV3NewOrderRespFillsInner.md) |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_quote_order_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**working_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_cancel_replace_v3_new_order_resp import SpotCreateOrderCancelReplaceV3NewOrderResp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderCancelReplaceV3NewOrderResp from a JSON string
spot_create_order_cancel_replace_v3_new_order_resp_instance = SpotCreateOrderCancelReplaceV3NewOrderResp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderCancelReplaceV3NewOrderResp.to_json())

# convert the object into a dict
spot_create_order_cancel_replace_v3_new_order_resp_dict = spot_create_order_cancel_replace_v3_new_order_resp_instance.to_dict()
# create an instance of SpotCreateOrderCancelReplaceV3NewOrderResp from a dict
spot_create_order_cancel_replace_v3_new_order_resp_from_dict = SpotCreateOrderCancelReplaceV3NewOrderResp.from_dict(spot_create_order_cancel_replace_v3_new_order_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


