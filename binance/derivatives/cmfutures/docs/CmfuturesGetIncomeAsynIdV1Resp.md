# CmfuturesGetIncomeAsynIdV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_id** | **str** |  | [optional] 
**expiration_timestamp** | **int** |  | [optional] 
**is_expired** | **object** |  | [optional] 
**notified** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_income_asyn_id_v1_resp import CmfuturesGetIncomeAsynIdV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetIncomeAsynIdV1Resp from a JSON string
cmfutures_get_income_asyn_id_v1_resp_instance = CmfuturesGetIncomeAsynIdV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetIncomeAsynIdV1Resp.to_json())

# convert the object into a dict
cmfutures_get_income_asyn_id_v1_resp_dict = cmfutures_get_income_asyn_id_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetIncomeAsynIdV1Resp from a dict
cmfutures_get_income_asyn_id_v1_resp_from_dict = CmfuturesGetIncomeAsynIdV1Resp.from_dict(cmfutures_get_income_asyn_id_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


