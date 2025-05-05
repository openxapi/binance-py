# GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**from_account_type** | **str** |  | [optional] 
**from_email** | **str** |  | [optional] 
**scheduled_data** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**to_account_type** | **str** |  | [optional] 
**to_email** | **str** |  | [optional] 
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_query_trans_log_for_investor_v1_resp_manager_sub_transfer_history_vos_inner import GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner from a JSON string
get_managed_subaccount_query_trans_log_for_investor_v1_resp_manager_sub_transfer_history_vos_inner_instance = GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner.to_json())

# convert the object into a dict
get_managed_subaccount_query_trans_log_for_investor_v1_resp_manager_sub_transfer_history_vos_inner_dict = get_managed_subaccount_query_trans_log_for_investor_v1_resp_manager_sub_transfer_history_vos_inner_instance.to_dict()
# create an instance of GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner from a dict
get_managed_subaccount_query_trans_log_for_investor_v1_resp_manager_sub_transfer_history_vos_inner_from_dict = GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner.from_dict(get_managed_subaccount_query_trans_log_for_investor_v1_resp_manager_sub_transfer_history_vos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


