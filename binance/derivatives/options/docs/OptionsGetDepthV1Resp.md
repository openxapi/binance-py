# OptionsGetDepthV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t** | **int** |  | [optional] 
**asks** | **List[List[str]]** |  | [optional] 
**bids** | **List[List[str]]** |  | [optional] 
**u** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_depth_v1_resp import OptionsGetDepthV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetDepthV1Resp from a JSON string
options_get_depth_v1_resp_instance = OptionsGetDepthV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetDepthV1Resp.to_json())

# convert the object into a dict
options_get_depth_v1_resp_dict = options_get_depth_v1_resp_instance.to_dict()
# create an instance of OptionsGetDepthV1Resp from a dict
options_get_depth_v1_resp_from_dict = OptionsGetDepthV1Resp.from_dict(options_get_depth_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


