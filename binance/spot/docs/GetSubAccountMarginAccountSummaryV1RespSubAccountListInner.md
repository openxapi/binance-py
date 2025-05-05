# GetSubAccountMarginAccountSummaryV1RespSubAccountListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner import GetSubAccountMarginAccountSummaryV1RespSubAccountListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountMarginAccountSummaryV1RespSubAccountListInner from a JSON string
get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_instance = GetSubAccountMarginAccountSummaryV1RespSubAccountListInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountMarginAccountSummaryV1RespSubAccountListInner.to_json())

# convert the object into a dict
get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_dict = get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_instance.to_dict()
# create an instance of GetSubAccountMarginAccountSummaryV1RespSubAccountListInner from a dict
get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_from_dict = GetSubAccountMarginAccountSummaryV1RespSubAccountListInner.from_dict(get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


