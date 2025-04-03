# SubaccountGetSubAccountFuturesAccountSummaryV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_account_summary_resp** | [**SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp**](SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_futures_account_summary_v2_resp import SubaccountGetSubAccountFuturesAccountSummaryV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountFuturesAccountSummaryV2Resp from a JSON string
subaccount_get_sub_account_futures_account_summary_v2_resp_instance = SubaccountGetSubAccountFuturesAccountSummaryV2Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountFuturesAccountSummaryV2Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_futures_account_summary_v2_resp_dict = subaccount_get_sub_account_futures_account_summary_v2_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountFuturesAccountSummaryV2Resp from a dict
subaccount_get_sub_account_futures_account_summary_v2_resp_from_dict = SubaccountGetSubAccountFuturesAccountSummaryV2Resp.from_dict(subaccount_get_sub_account_futures_account_summary_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


