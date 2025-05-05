# GetMarginOrderListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orders** | [**List[CreateMarginOrderOcoV1RespOrdersInner]**](CreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_order_list_v1_resp import GetMarginOrderListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginOrderListV1Resp from a JSON string
get_margin_order_list_v1_resp_instance = GetMarginOrderListV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginOrderListV1Resp.to_json())

# convert the object into a dict
get_margin_order_list_v1_resp_dict = get_margin_order_list_v1_resp_instance.to_dict()
# create an instance of GetMarginOrderListV1Resp from a dict
get_margin_order_list_v1_resp_from_dict = GetMarginOrderListV1Resp.from_dict(get_margin_order_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


