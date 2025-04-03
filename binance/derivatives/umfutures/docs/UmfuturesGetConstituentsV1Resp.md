# UmfuturesGetConstituentsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constituents** | [**List[UmfuturesGetConstituentsV1RespConstituentsInner]**](UmfuturesGetConstituentsV1RespConstituentsInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_constituents_v1_resp import UmfuturesGetConstituentsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetConstituentsV1Resp from a JSON string
umfutures_get_constituents_v1_resp_instance = UmfuturesGetConstituentsV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetConstituentsV1Resp.to_json())

# convert the object into a dict
umfutures_get_constituents_v1_resp_dict = umfutures_get_constituents_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetConstituentsV1Resp from a dict
umfutures_get_constituents_v1_resp_from_dict = UmfuturesGetConstituentsV1Resp.from_dict(umfutures_get_constituents_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


