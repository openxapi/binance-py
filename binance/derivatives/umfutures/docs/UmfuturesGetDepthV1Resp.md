# UmfuturesGetDepthV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **int** |  | [optional] 
**t** | **int** |  | [optional] 
**asks** | **List[List[str]]** |  | [optional] 
**bids** | **List[List[str]]** |  | [optional] 
**last_update_id** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_depth_v1_resp import UmfuturesGetDepthV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetDepthV1Resp from a JSON string
umfutures_get_depth_v1_resp_instance = UmfuturesGetDepthV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetDepthV1Resp.to_json())

# convert the object into a dict
umfutures_get_depth_v1_resp_dict = umfutures_get_depth_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetDepthV1Resp from a dict
umfutures_get_depth_v1_resp_from_dict = UmfuturesGetDepthV1Resp.from_dict(umfutures_get_depth_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


