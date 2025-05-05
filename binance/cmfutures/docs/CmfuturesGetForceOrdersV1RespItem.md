# CmfuturesGetForceOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**price_protect** | **bool** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
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
from binance.cmfutures.models.cmfutures_get_force_orders_v1_resp_item import CmfuturesGetForceOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetForceOrdersV1RespItem from a JSON string
cmfutures_get_force_orders_v1_resp_item_instance = CmfuturesGetForceOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetForceOrdersV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_force_orders_v1_resp_item_dict = cmfutures_get_force_orders_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetForceOrdersV1RespItem from a dict
cmfutures_get_force_orders_v1_resp_item_from_dict = CmfuturesGetForceOrdersV1RespItem.from_dict(cmfutures_get_force_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


