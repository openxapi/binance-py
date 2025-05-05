# CreateMmpResetV1Resp


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
from binance.options.models.create_mmp_reset_v1_resp import CreateMmpResetV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMmpResetV1Resp from a JSON string
create_mmp_reset_v1_resp_instance = CreateMmpResetV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateMmpResetV1Resp.to_json())

# convert the object into a dict
create_mmp_reset_v1_resp_dict = create_mmp_reset_v1_resp_instance.to_dict()
# create an instance of CreateMmpResetV1Resp from a dict
create_mmp_reset_v1_resp_from_dict = CreateMmpResetV1Resp.from_dict(create_mmp_reset_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


