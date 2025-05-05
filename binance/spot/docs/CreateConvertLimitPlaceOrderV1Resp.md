# CreateConvertLimitPlaceOrderV1Resp


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
from binance.spot.models.create_convert_limit_place_order_v1_resp import CreateConvertLimitPlaceOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConvertLimitPlaceOrderV1Resp from a JSON string
create_convert_limit_place_order_v1_resp_instance = CreateConvertLimitPlaceOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateConvertLimitPlaceOrderV1Resp.to_json())

# convert the object into a dict
create_convert_limit_place_order_v1_resp_dict = create_convert_limit_place_order_v1_resp_instance.to_dict()
# create an instance of CreateConvertLimitPlaceOrderV1Resp from a dict
create_convert_limit_place_order_v1_resp_from_dict = CreateConvertLimitPlaceOrderV1Resp.from_dict(create_convert_limit_place_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


