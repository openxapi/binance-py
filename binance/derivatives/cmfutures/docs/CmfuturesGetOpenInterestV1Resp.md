# CmfuturesGetOpenInterestV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | **str** |  | [optional] 
**open_interest** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_open_interest_v1_resp import CmfuturesGetOpenInterestV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetOpenInterestV1Resp from a JSON string
cmfutures_get_open_interest_v1_resp_instance = CmfuturesGetOpenInterestV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetOpenInterestV1Resp.to_json())

# convert the object into a dict
cmfutures_get_open_interest_v1_resp_dict = cmfutures_get_open_interest_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetOpenInterestV1Resp from a dict
cmfutures_get_open_interest_v1_resp_from_dict = CmfuturesGetOpenInterestV1Resp.from_dict(cmfutures_get_open_interest_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


