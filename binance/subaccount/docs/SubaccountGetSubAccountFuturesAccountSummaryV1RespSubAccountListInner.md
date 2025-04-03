# SubaccountGetSubAccountFuturesAccountSummaryV1RespSubAccountListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**total_initial_margin** | **str** |  | [optional] 
**total_maintenance_margin** | **str** |  | [optional] 
**total_margin_balance** | **str** |  | [optional] 
**total_open_order_initial_margin** | **str** |  | [optional] 
**total_position_initial_margin** | **str** |  | [optional] 
**total_unrealized_profit** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_futures_account_summary_v1_resp_sub_account_list_inner import SubaccountGetSubAccountFuturesAccountSummaryV1RespSubAccountListInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountFuturesAccountSummaryV1RespSubAccountListInner from a JSON string
subaccount_get_sub_account_futures_account_summary_v1_resp_sub_account_list_inner_instance = SubaccountGetSubAccountFuturesAccountSummaryV1RespSubAccountListInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountFuturesAccountSummaryV1RespSubAccountListInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_futures_account_summary_v1_resp_sub_account_list_inner_dict = subaccount_get_sub_account_futures_account_summary_v1_resp_sub_account_list_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountFuturesAccountSummaryV1RespSubAccountListInner from a dict
subaccount_get_sub_account_futures_account_summary_v1_resp_sub_account_list_inner_from_dict = SubaccountGetSubAccountFuturesAccountSummaryV1RespSubAccountListInner.from_dict(subaccount_get_sub_account_futures_account_summary_v1_resp_sub_account_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


