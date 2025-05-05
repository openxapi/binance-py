# PmarginDeleteMarginAllOpenOrdersV1RespOrderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[PmarginDeleteMarginAllOpenOrdersV1RespOrder]**](PmarginDeleteMarginAllOpenOrdersV1RespOrder.md) |  | [optional] 
**orders** | [**List[CreateMarginOrderOcoV1RespOrdersInner]**](CreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.pmargin_delete_margin_all_open_orders_v1_resp_order_list import PmarginDeleteMarginAllOpenOrdersV1RespOrderList

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginDeleteMarginAllOpenOrdersV1RespOrderList from a JSON string
pmargin_delete_margin_all_open_orders_v1_resp_order_list_instance = PmarginDeleteMarginAllOpenOrdersV1RespOrderList.from_json(json)
# print the JSON string representation of the object
print(PmarginDeleteMarginAllOpenOrdersV1RespOrderList.to_json())

# convert the object into a dict
pmargin_delete_margin_all_open_orders_v1_resp_order_list_dict = pmargin_delete_margin_all_open_orders_v1_resp_order_list_instance.to_dict()
# create an instance of PmarginDeleteMarginAllOpenOrdersV1RespOrderList from a dict
pmargin_delete_margin_all_open_orders_v1_resp_order_list_from_dict = PmarginDeleteMarginAllOpenOrdersV1RespOrderList.from_dict(pmargin_delete_margin_all_open_orders_v1_resp_order_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


