# CmfuturesCreateLeverageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **int** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_create_leverage_v1_resp import CmfuturesCreateLeverageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesCreateLeverageV1Resp from a JSON string
cmfutures_create_leverage_v1_resp_instance = CmfuturesCreateLeverageV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesCreateLeverageV1Resp.to_json())

# convert the object into a dict
cmfutures_create_leverage_v1_resp_dict = cmfutures_create_leverage_v1_resp_instance.to_dict()
# create an instance of CmfuturesCreateLeverageV1Resp from a dict
cmfutures_create_leverage_v1_resp_from_dict = CmfuturesCreateLeverageV1Resp.from_dict(cmfutures_create_leverage_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


