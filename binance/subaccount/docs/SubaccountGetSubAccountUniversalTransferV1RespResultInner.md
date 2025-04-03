# SubaccountGetSubAccountUniversalTransferV1RespResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**client_tran_id** | **str** |  | [optional] 
**create_time_stamp** | **int** |  | [optional] 
**from_account_type** | **str** |  | [optional] 
**from_email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**to_account_type** | **str** |  | [optional] 
**to_email** | **str** |  | [optional] 
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_universal_transfer_v1_resp_result_inner import SubaccountGetSubAccountUniversalTransferV1RespResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountUniversalTransferV1RespResultInner from a JSON string
subaccount_get_sub_account_universal_transfer_v1_resp_result_inner_instance = SubaccountGetSubAccountUniversalTransferV1RespResultInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountUniversalTransferV1RespResultInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_universal_transfer_v1_resp_result_inner_dict = subaccount_get_sub_account_universal_transfer_v1_resp_result_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountUniversalTransferV1RespResultInner from a dict
subaccount_get_sub_account_universal_transfer_v1_resp_result_inner_from_dict = SubaccountGetSubAccountUniversalTransferV1RespResultInner.from_dict(subaccount_get_sub_account_universal_transfer_v1_resp_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


