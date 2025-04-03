# PmarginGetMarginOpenOrderListV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orders** | [**List[PmarginCreateMarginOrderOcoV1RespOrdersInner]**](PmarginCreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_margin_open_order_list_v1_resp_item import PmarginGetMarginOpenOrderListV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetMarginOpenOrderListV1RespItem from a JSON string
pmargin_get_margin_open_order_list_v1_resp_item_instance = PmarginGetMarginOpenOrderListV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetMarginOpenOrderListV1RespItem.to_json())

# convert the object into a dict
pmargin_get_margin_open_order_list_v1_resp_item_dict = pmargin_get_margin_open_order_list_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetMarginOpenOrderListV1RespItem from a dict
pmargin_get_margin_open_order_list_v1_resp_item_from_dict = PmarginGetMarginOpenOrderListV1RespItem.from_dict(pmargin_get_margin_open_order_list_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


