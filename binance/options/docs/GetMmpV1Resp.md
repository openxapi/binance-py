# GetMmpV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_limit** | **str** |  | [optional] 
**frozen_time_in_milliseconds** | **int** |  | [optional] 
**last_trigger_time** | **int** |  | [optional] 
**qty_limit** | **str** |  | [optional] 
**underlying** | **str** |  | [optional] 
**underlying_id** | **int** |  | [optional] 
**window_time_in_milliseconds** | **int** |  | [optional] 

## Example

```python
from binance.options.models.get_mmp_v1_resp import GetMmpV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMmpV1Resp from a JSON string
get_mmp_v1_resp_instance = GetMmpV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMmpV1Resp.to_json())

# convert the object into a dict
get_mmp_v1_resp_dict = get_mmp_v1_resp_instance.to_dict()
# create an instance of GetMmpV1Resp from a dict
get_mmp_v1_resp_from_dict = GetMmpV1Resp.from_dict(get_mmp_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


