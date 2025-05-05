# CreateUserDataStreamV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listen_key** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_user_data_stream_v3_resp import CreateUserDataStreamV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserDataStreamV3Resp from a JSON string
create_user_data_stream_v3_resp_instance = CreateUserDataStreamV3Resp.from_json(json)
# print the JSON string representation of the object
print(CreateUserDataStreamV3Resp.to_json())

# convert the object into a dict
create_user_data_stream_v3_resp_dict = create_user_data_stream_v3_resp_instance.to_dict()
# create an instance of CreateUserDataStreamV3Resp from a dict
create_user_data_stream_v3_resp_from_dict = CreateUserDataStreamV3Resp.from_dict(create_user_data_stream_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


