# GetSubAccountFuturesAccountSummaryV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_account_summary_resp** | [**GetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp**](GetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_account_summary_v2_resp import GetSubAccountFuturesAccountSummaryV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesAccountSummaryV2Resp from a JSON string
get_sub_account_futures_account_summary_v2_resp_instance = GetSubAccountFuturesAccountSummaryV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesAccountSummaryV2Resp.to_json())

# convert the object into a dict
get_sub_account_futures_account_summary_v2_resp_dict = get_sub_account_futures_account_summary_v2_resp_instance.to_dict()
# create an instance of GetSubAccountFuturesAccountSummaryV2Resp from a dict
get_sub_account_futures_account_summary_v2_resp_from_dict = GetSubAccountFuturesAccountSummaryV2Resp.from_dict(get_sub_account_futures_account_summary_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


