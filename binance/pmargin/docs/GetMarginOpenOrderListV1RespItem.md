# GetMarginOpenOrderListV1RespItem


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
from binance.pmargin.models.get_margin_open_order_list_v1_resp_item import GetMarginOpenOrderListV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginOpenOrderListV1RespItem from a JSON string
get_margin_open_order_list_v1_resp_item_instance = GetMarginOpenOrderListV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginOpenOrderListV1RespItem.to_json())

# convert the object into a dict
get_margin_open_order_list_v1_resp_item_dict = get_margin_open_order_list_v1_resp_item_instance.to_dict()
# create an instance of GetMarginOpenOrderListV1RespItem from a dict
get_margin_open_order_list_v1_resp_item_from_dict = GetMarginOpenOrderListV1RespItem.from_dict(get_margin_open_order_list_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


