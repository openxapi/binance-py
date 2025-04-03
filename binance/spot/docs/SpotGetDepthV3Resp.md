# SpotGetDepthV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asks** | **List[List[str]]** |  | [optional] 
**bids** | **List[List[str]]** |  | [optional] 
**last_update_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_depth_v3_resp import SpotGetDepthV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetDepthV3Resp from a JSON string
spot_get_depth_v3_resp_instance = SpotGetDepthV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetDepthV3Resp.to_json())

# convert the object into a dict
spot_get_depth_v3_resp_dict = spot_get_depth_v3_resp_instance.to_dict()
# create an instance of SpotGetDepthV3Resp from a dict
spot_get_depth_v3_resp_from_dict = SpotGetDepthV3Resp.from_dict(spot_get_depth_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


