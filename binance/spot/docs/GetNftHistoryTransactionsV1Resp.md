# GetNftHistoryTransactionsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GetNftHistoryTransactionsV1RespListInner]**](GetNftHistoryTransactionsV1RespListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_nft_history_transactions_v1_resp import GetNftHistoryTransactionsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetNftHistoryTransactionsV1Resp from a JSON string
get_nft_history_transactions_v1_resp_instance = GetNftHistoryTransactionsV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetNftHistoryTransactionsV1Resp.to_json())

# convert the object into a dict
get_nft_history_transactions_v1_resp_dict = get_nft_history_transactions_v1_resp_instance.to_dict()
# create an instance of GetNftHistoryTransactionsV1Resp from a dict
get_nft_history_transactions_v1_resp_from_dict = GetNftHistoryTransactionsV1Resp.from_dict(get_nft_history_transactions_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


