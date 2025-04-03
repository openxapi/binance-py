# OptionsGetTimeV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_time_v1_resp import OptionsGetTimeV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetTimeV1Resp from a JSON string
options_get_time_v1_resp_instance = OptionsGetTimeV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetTimeV1Resp.to_json())

# convert the object into a dict
options_get_time_v1_resp_dict = options_get_time_v1_resp_instance.to_dict()
# create an instance of OptionsGetTimeV1Resp from a dict
options_get_time_v1_resp_from_dict = OptionsGetTimeV1Resp.from_dict(options_get_time_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


