# GetOpenOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_price** | **str** |  | [optional] 
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**close_position** | **bool** |  | [optional] 
**cum_base** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_type** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_match** | **str** |  | [optional] 
**price_protect** | **bool** |  | [optional] 
**price_rate** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**working_type** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_open_order_v1_resp import GetOpenOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenOrderV1Resp from a JSON string
get_open_order_v1_resp_instance = GetOpenOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetOpenOrderV1Resp.to_json())

# convert the object into a dict
get_open_order_v1_resp_dict = get_open_order_v1_resp_instance.to_dict()
# create an instance of GetOpenOrderV1Resp from a dict
get_open_order_v1_resp_from_dict = GetOpenOrderV1Resp.from_dict(get_open_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


