# GetConvertOrderStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**from_amount** | **str** |  | [optional] 
**from_asset** | **str** |  | [optional] 
**inverse_ratio** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_status** | **str** |  | [optional] 
**ratio** | **str** |  | [optional] 
**to_amount** | **str** |  | [optional] 
**to_asset** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_convert_order_status_v1_resp import GetConvertOrderStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetConvertOrderStatusV1Resp from a JSON string
get_convert_order_status_v1_resp_instance = GetConvertOrderStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetConvertOrderStatusV1Resp.to_json())

# convert the object into a dict
get_convert_order_status_v1_resp_dict = get_convert_order_status_v1_resp_instance.to_dict()
# create an instance of GetConvertOrderStatusV1Resp from a dict
get_convert_order_status_v1_resp_from_dict = GetConvertOrderStatusV1Resp.from_dict(get_convert_order_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


