# SpotDeleteOrderListV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[SpotDeleteOrderListV3RespOrderReportsInner]**](SpotDeleteOrderListV3RespOrderReportsInner.md) |  | [optional] 
**orders** | [**List[SpotCreateOrderListOcoV3RespOrdersInner]**](SpotCreateOrderListOcoV3RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_delete_order_list_v3_resp import SpotDeleteOrderListV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotDeleteOrderListV3Resp from a JSON string
spot_delete_order_list_v3_resp_instance = SpotDeleteOrderListV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotDeleteOrderListV3Resp.to_json())

# convert the object into a dict
spot_delete_order_list_v3_resp_dict = spot_delete_order_list_v3_resp_instance.to_dict()
# create an instance of SpotDeleteOrderListV3Resp from a dict
spot_delete_order_list_v3_resp_from_dict = SpotDeleteOrderListV3Resp.from_dict(spot_delete_order_list_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


