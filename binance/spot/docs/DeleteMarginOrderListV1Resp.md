# DeleteMarginOrderListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[DeleteMarginOrderListV1RespOrderReportsInner]**](DeleteMarginOrderListV1RespOrderReportsInner.md) |  | [optional] 
**orders** | [**List[CreateMarginOrderOcoV1RespOrdersInner]**](CreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.delete_margin_order_list_v1_resp import DeleteMarginOrderListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMarginOrderListV1Resp from a JSON string
delete_margin_order_list_v1_resp_instance = DeleteMarginOrderListV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteMarginOrderListV1Resp.to_json())

# convert the object into a dict
delete_margin_order_list_v1_resp_dict = delete_margin_order_list_v1_resp_instance.to_dict()
# create an instance of DeleteMarginOrderListV1Resp from a dict
delete_margin_order_list_v1_resp_from_dict = DeleteMarginOrderListV1Resp.from_dict(delete_margin_order_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


