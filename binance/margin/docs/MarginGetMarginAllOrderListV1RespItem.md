# MarginGetMarginAllOrderListV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orders** | [**List[MarginCreateMarginOrderOcoV1RespOrdersInner]**](MarginCreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_all_order_list_v1_resp_item import MarginGetMarginAllOrderListV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginAllOrderListV1RespItem from a JSON string
margin_get_margin_all_order_list_v1_resp_item_instance = MarginGetMarginAllOrderListV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginAllOrderListV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_all_order_list_v1_resp_item_dict = margin_get_margin_all_order_list_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginAllOrderListV1RespItem from a dict
margin_get_margin_all_order_list_v1_resp_item_from_dict = MarginGetMarginAllOrderListV1RespItem.from_dict(margin_get_margin_all_order_list_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


