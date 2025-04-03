# UmfuturesGetPmAccountInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**max_withdraw_amount_usd** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_pm_account_info_v1_resp import UmfuturesGetPmAccountInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetPmAccountInfoV1Resp from a JSON string
umfutures_get_pm_account_info_v1_resp_instance = UmfuturesGetPmAccountInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetPmAccountInfoV1Resp.to_json())

# convert the object into a dict
umfutures_get_pm_account_info_v1_resp_dict = umfutures_get_pm_account_info_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetPmAccountInfoV1Resp from a dict
umfutures_get_pm_account_info_v1_resp_from_dict = UmfuturesGetPmAccountInfoV1Resp.from_dict(umfutures_get_pm_account_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


