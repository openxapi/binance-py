# SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner import SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner from a JSON string
subaccount_get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_instance = SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner.to_json())

# convert the object into a dict
subaccount_get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_dict = subaccount_get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_instance.to_dict()
# create an instance of SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner from a dict
subaccount_get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_from_dict = SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner.from_dict(subaccount_get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


