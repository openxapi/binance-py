# SpotCreateOrderCancelReplaceV3CancelResp


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
**orig_quote_order_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_cancel_replace_v3_cancel_resp import SpotCreateOrderCancelReplaceV3CancelResp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderCancelReplaceV3CancelResp from a JSON string
spot_create_order_cancel_replace_v3_cancel_resp_instance = SpotCreateOrderCancelReplaceV3CancelResp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderCancelReplaceV3CancelResp.to_json())

# convert the object into a dict
spot_create_order_cancel_replace_v3_cancel_resp_dict = spot_create_order_cancel_replace_v3_cancel_resp_instance.to_dict()
# create an instance of SpotCreateOrderCancelReplaceV3CancelResp from a dict
spot_create_order_cancel_replace_v3_cancel_resp_from_dict = SpotCreateOrderCancelReplaceV3CancelResp.from_dict(spot_create_order_cancel_replace_v3_cancel_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


