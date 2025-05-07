# GetSimpleEarnLockedPositionV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetSimpleEarnLockedPositionV1RespRowsInner]**](GetSimpleEarnLockedPositionV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_position_v1_resp import GetSimpleEarnLockedPositionV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedPositionV1Resp from a JSON string
get_simple_earn_locked_position_v1_resp_instance = GetSimpleEarnLockedPositionV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedPositionV1Resp.to_json())

# convert the object into a dict
get_simple_earn_locked_position_v1_resp_dict = get_simple_earn_locked_position_v1_resp_instance.to_dict()
# create an instance of GetSimpleEarnLockedPositionV1Resp from a dict
get_simple_earn_locked_position_v1_resp_from_dict = GetSimpleEarnLockedPositionV1Resp.from_dict(get_simple_earn_locked_position_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


