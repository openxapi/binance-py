# GetOrderListV3Resp


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
from binance.spot.models.get_order_list_v3_resp import GetOrderListV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderListV3Resp from a JSON string
get_order_list_v3_resp_instance = GetOrderListV3Resp.from_json(json)
# print the JSON string representation of the object
print(GetOrderListV3Resp.to_json())

# convert the object into a dict
get_order_list_v3_resp_dict = get_order_list_v3_resp_instance.to_dict()
# create an instance of GetOrderListV3Resp from a dict
get_order_list_v3_resp_from_dict = GetOrderListV3Resp.from_dict(get_order_list_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


