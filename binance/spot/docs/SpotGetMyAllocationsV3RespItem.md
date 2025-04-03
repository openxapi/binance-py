# SpotGetMyAllocationsV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_id** | **int** |  | [optional] 
**allocation_type** | **str** |  | [optional] 
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**is_allocator** | **bool** |  | [optional] 
**is_buyer** | **bool** |  | [optional] 
**is_maker** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_my_allocations_v3_resp_item import SpotGetMyAllocationsV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetMyAllocationsV3RespItem from a JSON string
spot_get_my_allocations_v3_resp_item_instance = SpotGetMyAllocationsV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetMyAllocationsV3RespItem.to_json())

# convert the object into a dict
spot_get_my_allocations_v3_resp_item_dict = spot_get_my_allocations_v3_resp_item_instance.to_dict()
# create an instance of SpotGetMyAllocationsV3RespItem from a dict
spot_get_my_allocations_v3_resp_item_from_dict = SpotGetMyAllocationsV3RespItem.from_dict(spot_get_my_allocations_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


