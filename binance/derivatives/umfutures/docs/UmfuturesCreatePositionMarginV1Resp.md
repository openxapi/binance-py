# UmfuturesCreatePositionMarginV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_create_position_margin_v1_resp import UmfuturesCreatePositionMarginV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesCreatePositionMarginV1Resp from a JSON string
umfutures_create_position_margin_v1_resp_instance = UmfuturesCreatePositionMarginV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesCreatePositionMarginV1Resp.to_json())

# convert the object into a dict
umfutures_create_position_margin_v1_resp_dict = umfutures_create_position_margin_v1_resp_instance.to_dict()
# create an instance of UmfuturesCreatePositionMarginV1Resp from a dict
umfutures_create_position_margin_v1_resp_from_dict = UmfuturesCreatePositionMarginV1Resp.from_dict(umfutures_create_position_margin_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


