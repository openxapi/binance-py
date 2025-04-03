# CmfuturesGetDepthV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **int** |  | [optional] 
**t** | **int** |  | [optional] 
**asks** | **List[List[str]]** |  | [optional] 
**bids** | **List[List[str]]** |  | [optional] 
**last_update_id** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_depth_v1_resp import CmfuturesGetDepthV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetDepthV1Resp from a JSON string
cmfutures_get_depth_v1_resp_instance = CmfuturesGetDepthV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetDepthV1Resp.to_json())

# convert the object into a dict
cmfutures_get_depth_v1_resp_dict = cmfutures_get_depth_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetDepthV1Resp from a dict
cmfutures_get_depth_v1_resp_from_dict = CmfuturesGetDepthV1Resp.from_dict(cmfutures_get_depth_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


