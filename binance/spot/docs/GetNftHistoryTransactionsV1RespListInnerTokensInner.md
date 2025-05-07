# GetNftHistoryTransactionsV1RespListInnerTokensInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_nft_history_transactions_v1_resp_list_inner_tokens_inner import GetNftHistoryTransactionsV1RespListInnerTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNftHistoryTransactionsV1RespListInnerTokensInner from a JSON string
get_nft_history_transactions_v1_resp_list_inner_tokens_inner_instance = GetNftHistoryTransactionsV1RespListInnerTokensInner.from_json(json)
# print the JSON string representation of the object
print(GetNftHistoryTransactionsV1RespListInnerTokensInner.to_json())

# convert the object into a dict
get_nft_history_transactions_v1_resp_list_inner_tokens_inner_dict = get_nft_history_transactions_v1_resp_list_inner_tokens_inner_instance.to_dict()
# create an instance of GetNftHistoryTransactionsV1RespListInnerTokensInner from a dict
get_nft_history_transactions_v1_resp_list_inner_tokens_inner_from_dict = GetNftHistoryTransactionsV1RespListInnerTokensInner.from_dict(get_nft_history_transactions_v1_resp_list_inner_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


