# CmfuturesGetConstituentsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constituents** | [**List[CmfuturesGetConstituentsV1RespConstituentsInner]**](CmfuturesGetConstituentsV1RespConstituentsInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_constituents_v1_resp import CmfuturesGetConstituentsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetConstituentsV1Resp from a JSON string
cmfutures_get_constituents_v1_resp_instance = CmfuturesGetConstituentsV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetConstituentsV1Resp.to_json())

# convert the object into a dict
cmfutures_get_constituents_v1_resp_dict = cmfutures_get_constituents_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetConstituentsV1Resp from a dict
cmfutures_get_constituents_v1_resp_from_dict = CmfuturesGetConstituentsV1Resp.from_dict(cmfutures_get_constituents_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


