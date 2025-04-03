# CmfuturesCreatePositionMarginV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_create_position_margin_v1_resp import CmfuturesCreatePositionMarginV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesCreatePositionMarginV1Resp from a JSON string
cmfutures_create_position_margin_v1_resp_instance = CmfuturesCreatePositionMarginV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesCreatePositionMarginV1Resp.to_json())

# convert the object into a dict
cmfutures_create_position_margin_v1_resp_dict = cmfutures_create_position_margin_v1_resp_instance.to_dict()
# create an instance of CmfuturesCreatePositionMarginV1Resp from a dict
cmfutures_create_position_margin_v1_resp_from_dict = CmfuturesCreatePositionMarginV1Resp.from_dict(cmfutures_create_position_margin_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


