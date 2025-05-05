# GetOpenOrderListV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orders** | [**List[CreateMarginOrderOcoV1RespOrdersInner]**](CreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_open_order_list_v3_resp_item import GetOpenOrderListV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenOrderListV3RespItem from a JSON string
get_open_order_list_v3_resp_item_instance = GetOpenOrderListV3RespItem.from_json(json)
# print the JSON string representation of the object
print(GetOpenOrderListV3RespItem.to_json())

# convert the object into a dict
get_open_order_list_v3_resp_item_dict = get_open_order_list_v3_resp_item_instance.to_dict()
# create an instance of GetOpenOrderListV3RespItem from a dict
get_open_order_list_v3_resp_item_from_dict = GetOpenOrderListV3RespItem.from_dict(get_open_order_list_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


