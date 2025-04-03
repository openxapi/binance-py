# CmfuturesGetPmAccountInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**max_withdraw_amount_usd** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_pm_account_info_v1_resp import CmfuturesGetPmAccountInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetPmAccountInfoV1Resp from a JSON string
cmfutures_get_pm_account_info_v1_resp_instance = CmfuturesGetPmAccountInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetPmAccountInfoV1Resp.to_json())

# convert the object into a dict
cmfutures_get_pm_account_info_v1_resp_dict = cmfutures_get_pm_account_info_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetPmAccountInfoV1Resp from a dict
cmfutures_get_pm_account_info_v1_resp_from_dict = CmfuturesGetPmAccountInfoV1Resp.from_dict(cmfutures_get_pm_account_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


