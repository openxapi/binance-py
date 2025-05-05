# CreateOrderListOtocoV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[CreateOrderListOtoV3RespOrderReportsInner]**](CreateOrderListOtoV3RespOrderReportsInner.md) |  | [optional] 
**orders** | [**List[CreateMarginOrderOcoV1RespOrdersInner]**](CreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_order_list_otoco_v3_resp import CreateOrderListOtocoV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderListOtocoV3Resp from a JSON string
create_order_list_otoco_v3_resp_instance = CreateOrderListOtocoV3Resp.from_json(json)
# print the JSON string representation of the object
print(CreateOrderListOtocoV3Resp.to_json())

# convert the object into a dict
create_order_list_otoco_v3_resp_dict = create_order_list_otoco_v3_resp_instance.to_dict()
# create an instance of CreateOrderListOtocoV3Resp from a dict
create_order_list_otoco_v3_resp_from_dict = CreateOrderListOtocoV3Resp.from_dict(create_order_list_otoco_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


