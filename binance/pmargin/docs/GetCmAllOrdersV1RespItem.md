# GetCmAllOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**cum_base** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_type** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_cm_all_orders_v1_resp_item import GetCmAllOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCmAllOrdersV1RespItem from a JSON string
get_cm_all_orders_v1_resp_item_instance = GetCmAllOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetCmAllOrdersV1RespItem.to_json())

# convert the object into a dict
get_cm_all_orders_v1_resp_item_dict = get_cm_all_orders_v1_resp_item_instance.to_dict()
# create an instance of GetCmAllOrdersV1RespItem from a dict
get_cm_all_orders_v1_resp_item_from_dict = GetCmAllOrdersV1RespItem.from_dict(get_cm_all_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


