# CreatePositionMarginV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.create_position_margin_v1_resp import CreatePositionMarginV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePositionMarginV1Resp from a JSON string
create_position_margin_v1_resp_instance = CreatePositionMarginV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreatePositionMarginV1Resp.to_json())

# convert the object into a dict
create_position_margin_v1_resp_dict = create_position_margin_v1_resp_instance.to_dict()
# create an instance of CreatePositionMarginV1Resp from a dict
create_position_margin_v1_resp_from_dict = CreatePositionMarginV1Resp.from_dict(create_position_margin_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


