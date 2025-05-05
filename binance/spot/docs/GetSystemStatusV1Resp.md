# GetSystemStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_system_status_v1_resp import GetSystemStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSystemStatusV1Resp from a JSON string
get_system_status_v1_resp_instance = GetSystemStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSystemStatusV1Resp.to_json())

# convert the object into a dict
get_system_status_v1_resp_dict = get_system_status_v1_resp_instance.to_dict()
# create an instance of GetSystemStatusV1Resp from a dict
get_system_status_v1_resp_from_dict = GetSystemStatusV1Resp.from_dict(get_system_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


