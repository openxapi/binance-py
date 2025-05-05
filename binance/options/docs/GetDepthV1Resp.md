# GetDepthV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t** | **int** |  | [optional] 
**asks** | **List[List[str]]** |  | [optional] 
**bids** | **List[List[str]]** |  | [optional] 
**u** | **int** |  | [optional] 

## Example

```python
from binance.options.models.get_depth_v1_resp import GetDepthV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepthV1Resp from a JSON string
get_depth_v1_resp_instance = GetDepthV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetDepthV1Resp.to_json())

# convert the object into a dict
get_depth_v1_resp_dict = get_depth_v1_resp_instance.to_dict()
# create an instance of GetDepthV1Resp from a dict
get_depth_v1_resp_from_dict = GetDepthV1Resp.from_dict(get_depth_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


