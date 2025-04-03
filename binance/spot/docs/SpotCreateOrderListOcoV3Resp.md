# SpotCreateOrderListOcoV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[SpotCreateOrderListOcoV3RespOrderReportsInner]**](SpotCreateOrderListOcoV3RespOrderReportsInner.md) |  | [optional] 
**orders** | [**List[SpotCreateOrderListOcoV3RespOrdersInner]**](SpotCreateOrderListOcoV3RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_list_oco_v3_resp import SpotCreateOrderListOcoV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderListOcoV3Resp from a JSON string
spot_create_order_list_oco_v3_resp_instance = SpotCreateOrderListOcoV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderListOcoV3Resp.to_json())

# convert the object into a dict
spot_create_order_list_oco_v3_resp_dict = spot_create_order_list_oco_v3_resp_instance.to_dict()
# create an instance of SpotCreateOrderListOcoV3Resp from a dict
spot_create_order_list_oco_v3_resp_from_dict = SpotCreateOrderListOcoV3Resp.from_dict(spot_create_order_list_oco_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


