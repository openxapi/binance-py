# GetDepthV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asks** | **List[List[str]]** |  | [optional] 
**bids** | **List[List[str]]** |  | [optional] 
**last_update_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_depth_v3_resp import GetDepthV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepthV3Resp from a JSON string
get_depth_v3_resp_instance = GetDepthV3Resp.from_json(json)
# print the JSON string representation of the object
print(GetDepthV3Resp.to_json())

# convert the object into a dict
get_depth_v3_resp_dict = get_depth_v3_resp_instance.to_dict()
# create an instance of GetDepthV3Resp from a dict
get_depth_v3_resp_from_dict = GetDepthV3Resp.from_dict(get_depth_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


