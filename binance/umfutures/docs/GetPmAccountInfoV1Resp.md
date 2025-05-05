# GetPmAccountInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**max_withdraw_amount_usd** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_pm_account_info_v1_resp import GetPmAccountInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetPmAccountInfoV1Resp from a JSON string
get_pm_account_info_v1_resp_instance = GetPmAccountInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetPmAccountInfoV1Resp.to_json())

# convert the object into a dict
get_pm_account_info_v1_resp_dict = get_pm_account_info_v1_resp_instance.to_dict()
# create an instance of GetPmAccountInfoV1Resp from a dict
get_pm_account_info_v1_resp_from_dict = GetPmAccountInfoV1Resp.from_dict(get_pm_account_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


