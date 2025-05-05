# CreateConvertLimitCancelOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_convert_limit_cancel_order_v1_resp import CreateConvertLimitCancelOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConvertLimitCancelOrderV1Resp from a JSON string
create_convert_limit_cancel_order_v1_resp_instance = CreateConvertLimitCancelOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateConvertLimitCancelOrderV1Resp.to_json())

# convert the object into a dict
create_convert_limit_cancel_order_v1_resp_dict = create_convert_limit_cancel_order_v1_resp_instance.to_dict()
# create an instance of CreateConvertLimitCancelOrderV1Resp from a dict
create_convert_limit_cancel_order_v1_resp_from_dict = CreateConvertLimitCancelOrderV1Resp.from_dict(create_convert_limit_cancel_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


