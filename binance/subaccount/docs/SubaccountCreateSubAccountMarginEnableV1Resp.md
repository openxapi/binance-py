# SubaccountCreateSubAccountMarginEnableV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**is_margin_enabled** | **bool** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_create_sub_account_margin_enable_v1_resp import SubaccountCreateSubAccountMarginEnableV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountCreateSubAccountMarginEnableV1Resp from a JSON string
subaccount_create_sub_account_margin_enable_v1_resp_instance = SubaccountCreateSubAccountMarginEnableV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountCreateSubAccountMarginEnableV1Resp.to_json())

# convert the object into a dict
subaccount_create_sub_account_margin_enable_v1_resp_dict = subaccount_create_sub_account_margin_enable_v1_resp_instance.to_dict()
# create an instance of SubaccountCreateSubAccountMarginEnableV1Resp from a dict
subaccount_create_sub_account_margin_enable_v1_resp_from_dict = SubaccountCreateSubAccountMarginEnableV1Resp.from_dict(subaccount_create_sub_account_margin_enable_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


