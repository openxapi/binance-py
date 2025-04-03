# MarginGetMarginOrderListV1Resp


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
from binance.margin.models.margin_get_margin_order_list_v1_resp import MarginGetMarginOrderListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginOrderListV1Resp from a JSON string
margin_get_margin_order_list_v1_resp_instance = MarginGetMarginOrderListV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginOrderListV1Resp.to_json())

# convert the object into a dict
margin_get_margin_order_list_v1_resp_dict = margin_get_margin_order_list_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginOrderListV1Resp from a dict
margin_get_margin_order_list_v1_resp_from_dict = MarginGetMarginOrderListV1Resp.from_dict(margin_get_margin_order_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


