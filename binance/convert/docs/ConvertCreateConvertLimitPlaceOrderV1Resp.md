# ConvertCreateConvertLimitPlaceOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_amount** | **str** |  | [optional] 
**inverse_ratio** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**ratio** | **str** |  | [optional] 
**to_amount** | **str** |  | [optional] 
**valid_timestamp** | **int** |  | [optional] 

## Example

```python
from binance.convert.models.convert_create_convert_limit_place_order_v1_resp import ConvertCreateConvertLimitPlaceOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertCreateConvertLimitPlaceOrderV1Resp from a JSON string
convert_create_convert_limit_place_order_v1_resp_instance = ConvertCreateConvertLimitPlaceOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(ConvertCreateConvertLimitPlaceOrderV1Resp.to_json())

# convert the object into a dict
convert_create_convert_limit_place_order_v1_resp_dict = convert_create_convert_limit_place_order_v1_resp_instance.to_dict()
# create an instance of ConvertCreateConvertLimitPlaceOrderV1Resp from a dict
convert_create_convert_limit_place_order_v1_resp_from_dict = ConvertCreateConvertLimitPlaceOrderV1Resp.from_dict(convert_create_convert_limit_place_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


