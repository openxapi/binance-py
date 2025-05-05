# GetManagedSubaccountQueryTransLogForTradeParentV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**manager_sub_transfer_history_vos** | [**List[GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner]**](GetManagedSubaccountQueryTransLogForInvestorV1RespManagerSubTransferHistoryVosInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_query_trans_log_for_trade_parent_v1_resp import GetManagedSubaccountQueryTransLogForTradeParentV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountQueryTransLogForTradeParentV1Resp from a JSON string
get_managed_subaccount_query_trans_log_for_trade_parent_v1_resp_instance = GetManagedSubaccountQueryTransLogForTradeParentV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountQueryTransLogForTradeParentV1Resp.to_json())

# convert the object into a dict
get_managed_subaccount_query_trans_log_for_trade_parent_v1_resp_dict = get_managed_subaccount_query_trans_log_for_trade_parent_v1_resp_instance.to_dict()
# create an instance of GetManagedSubaccountQueryTransLogForTradeParentV1Resp from a dict
get_managed_subaccount_query_trans_log_for_trade_parent_v1_resp_from_dict = GetManagedSubaccountQueryTransLogForTradeParentV1Resp.from_dict(get_managed_subaccount_query_trans_log_for_trade_parent_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


