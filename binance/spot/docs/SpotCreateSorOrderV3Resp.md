# SpotCreateSorOrderV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fills** | [**List[SpotCreateSorOrderV3RespFillsInner]**](SpotCreateSorOrderV3RespFillsInner.md) |  | [optional] 
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
**used_sor** | **bool** |  | [optional] 
**working_floor** | **str** |  | [optional] 
**working_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_sor_order_v3_resp import SpotCreateSorOrderV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateSorOrderV3Resp from a JSON string
spot_create_sor_order_v3_resp_instance = SpotCreateSorOrderV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateSorOrderV3Resp.to_json())

# convert the object into a dict
spot_create_sor_order_v3_resp_dict = spot_create_sor_order_v3_resp_instance.to_dict()
# create an instance of SpotCreateSorOrderV3Resp from a dict
spot_create_sor_order_v3_resp_from_dict = SpotCreateSorOrderV3Resp.from_dict(spot_create_sor_order_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


