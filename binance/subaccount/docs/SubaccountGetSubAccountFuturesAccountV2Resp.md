# SubaccountGetSubAccountFuturesAccountV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_account_resp** | [**SubaccountGetSubAccountFuturesAccountV2RespFutureAccountResp**](SubaccountGetSubAccountFuturesAccountV2RespFutureAccountResp.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_futures_account_v2_resp import SubaccountGetSubAccountFuturesAccountV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountFuturesAccountV2Resp from a JSON string
subaccount_get_sub_account_futures_account_v2_resp_instance = SubaccountGetSubAccountFuturesAccountV2Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountFuturesAccountV2Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_futures_account_v2_resp_dict = subaccount_get_sub_account_futures_account_v2_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountFuturesAccountV2Resp from a dict
subaccount_get_sub_account_futures_account_v2_resp_from_dict = SubaccountGetSubAccountFuturesAccountV2Resp.from_dict(subaccount_get_sub_account_futures_account_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


