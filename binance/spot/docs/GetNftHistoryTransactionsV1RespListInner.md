# GetNftHistoryTransactionsV1RespListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **str** |  | [optional] 
**tokens** | [**List[GetNftHistoryTransactionsV1RespListInnerTokensInner]**](GetNftHistoryTransactionsV1RespListInnerTokensInner.md) |  | [optional] 
**trade_amount** | **str** |  | [optional] 
**trade_currency** | **str** |  | [optional] 
**trade_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_nft_history_transactions_v1_resp_list_inner import GetNftHistoryTransactionsV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNftHistoryTransactionsV1RespListInner from a JSON string
get_nft_history_transactions_v1_resp_list_inner_instance = GetNftHistoryTransactionsV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(GetNftHistoryTransactionsV1RespListInner.to_json())

# convert the object into a dict
get_nft_history_transactions_v1_resp_list_inner_dict = get_nft_history_transactions_v1_resp_list_inner_instance.to_dict()
# create an instance of GetNftHistoryTransactionsV1RespListInner from a dict
get_nft_history_transactions_v1_resp_list_inner_from_dict = GetNftHistoryTransactionsV1RespListInner.from_dict(get_nft_history_transactions_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


