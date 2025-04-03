# SpotGetOpenOrderListV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orders** | [**List[SpotCreateOrderListOcoV3RespOrdersInner]**](SpotCreateOrderListOcoV3RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_open_order_list_v3_resp_item import SpotGetOpenOrderListV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetOpenOrderListV3RespItem from a JSON string
spot_get_open_order_list_v3_resp_item_instance = SpotGetOpenOrderListV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetOpenOrderListV3RespItem.to_json())

# convert the object into a dict
spot_get_open_order_list_v3_resp_item_dict = spot_get_open_order_list_v3_resp_item_instance.to_dict()
# create an instance of SpotGetOpenOrderListV3RespItem from a dict
spot_get_open_order_list_v3_resp_item_from_dict = SpotGetOpenOrderListV3RespItem.from_dict(spot_get_open_order_list_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


