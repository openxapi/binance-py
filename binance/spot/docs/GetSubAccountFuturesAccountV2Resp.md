# GetSubAccountFuturesAccountV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_account_resp** | [**GetSubAccountFuturesAccountV2RespFutureAccountResp**](GetSubAccountFuturesAccountV2RespFutureAccountResp.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_account_v2_resp import GetSubAccountFuturesAccountV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesAccountV2Resp from a JSON string
get_sub_account_futures_account_v2_resp_instance = GetSubAccountFuturesAccountV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesAccountV2Resp.to_json())

# convert the object into a dict
get_sub_account_futures_account_v2_resp_dict = get_sub_account_futures_account_v2_resp_instance.to_dict()
# create an instance of GetSubAccountFuturesAccountV2Resp from a dict
get_sub_account_futures_account_v2_resp_from_dict = GetSubAccountFuturesAccountV2Resp.from_dict(get_sub_account_futures_account_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


