# GetTimeV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_time_v3_resp import GetTimeV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimeV3Resp from a JSON string
get_time_v3_resp_instance = GetTimeV3Resp.from_json(json)
# print the JSON string representation of the object
print(GetTimeV3Resp.to_json())

# convert the object into a dict
get_time_v3_resp_dict = get_time_v3_resp_instance.to_dict()
# create an instance of GetTimeV3Resp from a dict
get_time_v3_resp_from_dict = GetTimeV3Resp.from_dict(get_time_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


