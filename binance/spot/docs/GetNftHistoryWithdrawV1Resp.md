# GetNftHistoryWithdrawV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GetNftHistoryWithdrawV1RespListInner]**](GetNftHistoryWithdrawV1RespListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_nft_history_withdraw_v1_resp import GetNftHistoryWithdrawV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetNftHistoryWithdrawV1Resp from a JSON string
get_nft_history_withdraw_v1_resp_instance = GetNftHistoryWithdrawV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetNftHistoryWithdrawV1Resp.to_json())

# convert the object into a dict
get_nft_history_withdraw_v1_resp_dict = get_nft_history_withdraw_v1_resp_instance.to_dict()
# create an instance of GetNftHistoryWithdrawV1Resp from a dict
get_nft_history_withdraw_v1_resp_from_dict = GetNftHistoryWithdrawV1Resp.from_dict(get_nft_history_withdraw_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


