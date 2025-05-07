# GetNftHistoryDepositV1RespListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_adrress** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**token_id** | **str** |  | [optional] 
**tx_id** | **object** |  | [optional] 

## Example

```python
from binance.spot.models.get_nft_history_deposit_v1_resp_list_inner import GetNftHistoryDepositV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNftHistoryDepositV1RespListInner from a JSON string
get_nft_history_deposit_v1_resp_list_inner_instance = GetNftHistoryDepositV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(GetNftHistoryDepositV1RespListInner.to_json())

# convert the object into a dict
get_nft_history_deposit_v1_resp_list_inner_dict = get_nft_history_deposit_v1_resp_list_inner_instance.to_dict()
# create an instance of GetNftHistoryDepositV1RespListInner from a dict
get_nft_history_deposit_v1_resp_list_inner_from_dict = GetNftHistoryDepositV1RespListInner.from_dict(get_nft_history_deposit_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


