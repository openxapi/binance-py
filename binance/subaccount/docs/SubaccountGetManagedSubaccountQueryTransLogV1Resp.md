# SubaccountGetManagedSubaccountQueryTransLogV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**manager_sub_transfer_history_vos** | [**List[SubaccountGetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner]**](SubaccountGetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_query_trans_log_v1_resp import SubaccountGetManagedSubaccountQueryTransLogV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountQueryTransLogV1Resp from a JSON string
subaccount_get_managed_subaccount_query_trans_log_v1_resp_instance = SubaccountGetManagedSubaccountQueryTransLogV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountQueryTransLogV1Resp.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_query_trans_log_v1_resp_dict = subaccount_get_managed_subaccount_query_trans_log_v1_resp_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountQueryTransLogV1Resp from a dict
subaccount_get_managed_subaccount_query_trans_log_v1_resp_from_dict = SubaccountGetManagedSubaccountQueryTransLogV1Resp.from_dict(subaccount_get_managed_subaccount_query_trans_log_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


