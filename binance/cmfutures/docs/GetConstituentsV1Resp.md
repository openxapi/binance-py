# GetConstituentsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constituents** | [**List[GetConstituentsV1RespConstituentsInner]**](GetConstituentsV1RespConstituentsInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_constituents_v1_resp import GetConstituentsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetConstituentsV1Resp from a JSON string
get_constituents_v1_resp_instance = GetConstituentsV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetConstituentsV1Resp.to_json())

# convert the object into a dict
get_constituents_v1_resp_dict = get_constituents_v1_resp_instance.to_dict()
# create an instance of GetConstituentsV1Resp from a dict
get_constituents_v1_resp_from_dict = GetConstituentsV1Resp.from_dict(get_constituents_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


