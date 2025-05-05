# GetTimeV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_time_v1_resp import GetTimeV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimeV1Resp from a JSON string
get_time_v1_resp_instance = GetTimeV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetTimeV1Resp.to_json())

# convert the object into a dict
get_time_v1_resp_dict = get_time_v1_resp_instance.to_dict()
# create an instance of GetTimeV1Resp from a dict
get_time_v1_resp_from_dict = GetTimeV1Resp.from_dict(get_time_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


