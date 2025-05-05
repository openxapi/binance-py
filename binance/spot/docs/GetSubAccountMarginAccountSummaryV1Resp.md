# GetSubAccountMarginAccountSummaryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_account_list** | [**List[GetSubAccountMarginAccountSummaryV1RespSubAccountListInner]**](GetSubAccountMarginAccountSummaryV1RespSubAccountListInner.md) |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_margin_account_summary_v1_resp import GetSubAccountMarginAccountSummaryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountMarginAccountSummaryV1Resp from a JSON string
get_sub_account_margin_account_summary_v1_resp_instance = GetSubAccountMarginAccountSummaryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountMarginAccountSummaryV1Resp.to_json())

# convert the object into a dict
get_sub_account_margin_account_summary_v1_resp_dict = get_sub_account_margin_account_summary_v1_resp_instance.to_dict()
# create an instance of GetSubAccountMarginAccountSummaryV1Resp from a dict
get_sub_account_margin_account_summary_v1_resp_from_dict = GetSubAccountMarginAccountSummaryV1Resp.from_dict(get_sub_account_margin_account_summary_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


