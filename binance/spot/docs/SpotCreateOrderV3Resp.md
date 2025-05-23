# SpotCreateOrderV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fills** | [**List[MarginCreateMarginOrderV1RespFillsInner]**](MarginCreateMarginOrderV1RespFillsInner.md) |  | [optional] 
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
from binance.spot.models.spot_create_order_v3_resp import SpotCreateOrderV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderV3Resp from a JSON string
spot_create_order_v3_resp_instance = SpotCreateOrderV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderV3Resp.to_json())

# convert the object into a dict
spot_create_order_v3_resp_dict = spot_create_order_v3_resp_instance.to_dict()
# create an instance of SpotCreateOrderV3Resp from a dict
spot_create_order_v3_resp_from_dict = SpotCreateOrderV3Resp.from_dict(spot_create_order_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


