# WalletGetLocalentityDepositHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address_tag** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**confirm_times** | **str** |  | [optional] 
**deposit_status** | **int** |  | [optional] 
**insert_time** | **int** |  | [optional] 
**network** | **str** |  | [optional] 
**questionnaire** | **object** |  | [optional] 
**require_questionnaire** | **bool** |  | [optional] 
**tr_id** | **int** |  | [optional] 
**tran_id** | **int** |  | [optional] 
**transfer_type** | **int** |  | [optional] 
**travel_rule_status** | **int** |  | [optional] 
**tx_id** | **str** |  | [optional] 
**unlock_confirm** | **int** |  | [optional] 
**wallet_type** | **int** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_localentity_deposit_history_v1_resp_item import WalletGetLocalentityDepositHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetLocalentityDepositHistoryV1RespItem from a JSON string
wallet_get_localentity_deposit_history_v1_resp_item_instance = WalletGetLocalentityDepositHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(WalletGetLocalentityDepositHistoryV1RespItem.to_json())

# convert the object into a dict
wallet_get_localentity_deposit_history_v1_resp_item_dict = wallet_get_localentity_deposit_history_v1_resp_item_instance.to_dict()
# create an instance of WalletGetLocalentityDepositHistoryV1RespItem from a dict
wallet_get_localentity_deposit_history_v1_resp_item_from_dict = WalletGetLocalentityDepositHistoryV1RespItem.from_dict(wallet_get_localentity_deposit_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


