# GetNftHistoryWithdrawV1RespListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_adrress** | **str** |  | [optional] 
**fee** | **float** |  | [optional] 
**fee_asset** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**token_id** | **str** |  | [optional] 
**tx_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_nft_history_withdraw_v1_resp_list_inner import GetNftHistoryWithdrawV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNftHistoryWithdrawV1RespListInner from a JSON string
get_nft_history_withdraw_v1_resp_list_inner_instance = GetNftHistoryWithdrawV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(GetNftHistoryWithdrawV1RespListInner.to_json())

# convert the object into a dict
get_nft_history_withdraw_v1_resp_list_inner_dict = get_nft_history_withdraw_v1_resp_list_inner_instance.to_dict()
# create an instance of GetNftHistoryWithdrawV1RespListInner from a dict
get_nft_history_withdraw_v1_resp_list_inner_from_dict = GetNftHistoryWithdrawV1RespListInner.from_dict(get_nft_history_withdraw_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


