# SpotDeleteOpenOrdersV3RespOrderListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[SpotDeleteOpenOrdersV3RespOrderItem]**](SpotDeleteOpenOrdersV3RespOrderItem.md) |  | [optional] 
**orders** | [**List[SpotCreateOrderListOcoV3RespOrdersInner]**](SpotCreateOrderListOcoV3RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_delete_open_orders_v3_resp_order_list_item import SpotDeleteOpenOrdersV3RespOrderListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotDeleteOpenOrdersV3RespOrderListItem from a JSON string
spot_delete_open_orders_v3_resp_order_list_item_instance = SpotDeleteOpenOrdersV3RespOrderListItem.from_json(json)
# print the JSON string representation of the object
print(SpotDeleteOpenOrdersV3RespOrderListItem.to_json())

# convert the object into a dict
spot_delete_open_orders_v3_resp_order_list_item_dict = spot_delete_open_orders_v3_resp_order_list_item_instance.to_dict()
# create an instance of SpotDeleteOpenOrdersV3RespOrderListItem from a dict
spot_delete_open_orders_v3_resp_order_list_item_from_dict = SpotDeleteOpenOrdersV3RespOrderListItem.from_dict(spot_delete_open_orders_v3_resp_order_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


