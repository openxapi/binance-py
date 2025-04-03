# OptionsCreateMmpSetV1Resp


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
from binance.derivatives.options.models.options_create_mmp_set_v1_resp import OptionsCreateMmpSetV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCreateMmpSetV1Resp from a JSON string
options_create_mmp_set_v1_resp_instance = OptionsCreateMmpSetV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsCreateMmpSetV1Resp.to_json())

# convert the object into a dict
options_create_mmp_set_v1_resp_dict = options_create_mmp_set_v1_resp_instance.to_dict()
# create an instance of OptionsCreateMmpSetV1Resp from a dict
options_create_mmp_set_v1_resp_from_dict = OptionsCreateMmpSetV1Resp.from_dict(options_create_mmp_set_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


