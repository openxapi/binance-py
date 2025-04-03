# SubaccountGetSubAccountUniversalTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[SubaccountGetSubAccountUniversalTransferV1RespResultInner]**](SubaccountGetSubAccountUniversalTransferV1RespResultInner.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_universal_transfer_v1_resp import SubaccountGetSubAccountUniversalTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountUniversalTransferV1Resp from a JSON string
subaccount_get_sub_account_universal_transfer_v1_resp_instance = SubaccountGetSubAccountUniversalTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountUniversalTransferV1Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_universal_transfer_v1_resp_dict = subaccount_get_sub_account_universal_transfer_v1_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountUniversalTransferV1Resp from a dict
subaccount_get_sub_account_universal_transfer_v1_resp_from_dict = SubaccountGetSubAccountUniversalTransferV1Resp.from_dict(subaccount_get_sub_account_universal_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


