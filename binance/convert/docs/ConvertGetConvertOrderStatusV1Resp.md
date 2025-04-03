# ConvertGetConvertOrderStatusV1Resp


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
from binance.convert.models.convert_get_convert_order_status_v1_resp import ConvertGetConvertOrderStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGetConvertOrderStatusV1Resp from a JSON string
convert_get_convert_order_status_v1_resp_instance = ConvertGetConvertOrderStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(ConvertGetConvertOrderStatusV1Resp.to_json())

# convert the object into a dict
convert_get_convert_order_status_v1_resp_dict = convert_get_convert_order_status_v1_resp_instance.to_dict()
# create an instance of ConvertGetConvertOrderStatusV1Resp from a dict
convert_get_convert_order_status_v1_resp_from_dict = ConvertGetConvertOrderStatusV1Resp.from_dict(convert_get_convert_order_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


