# WalletGetCapitalConfigGetallV1RespItemNetworkListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_regex** | **str** |  | [optional] 
**busy** | **bool** |  | [optional] 
**coin** | **str** |  | [optional] 
**contract_address** | **str** |  | [optional] 
**contract_address_url** | **str** |  | [optional] 
**deposit_desc** | **str** |  | [optional] 
**deposit_enable** | **bool** |  | [optional] 
**estimated_arrival_time** | **int** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**memo_regex** | **str** |  | [optional] 
**min_confirm** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**same_address** | **bool** |  | [optional] 
**special_tips** | **str** |  | [optional] 
**un_lock_confirm** | **int** |  | [optional] 
**withdraw_desc** | **str** |  | [optional] 
**withdraw_enable** | **bool** |  | [optional] 
**withdraw_fee** | **str** |  | [optional] 
**withdraw_integer_multiple** | **str** |  | [optional] 
**withdraw_internal_min** | **str** |  | [optional] 
**withdraw_max** | **str** |  | [optional] 
**withdraw_min** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_capital_config_getall_v1_resp_item_network_list_inner import WalletGetCapitalConfigGetallV1RespItemNetworkListInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetCapitalConfigGetallV1RespItemNetworkListInner from a JSON string
wallet_get_capital_config_getall_v1_resp_item_network_list_inner_instance = WalletGetCapitalConfigGetallV1RespItemNetworkListInner.from_json(json)
# print the JSON string representation of the object
print(WalletGetCapitalConfigGetallV1RespItemNetworkListInner.to_json())

# convert the object into a dict
wallet_get_capital_config_getall_v1_resp_item_network_list_inner_dict = wallet_get_capital_config_getall_v1_resp_item_network_list_inner_instance.to_dict()
# create an instance of WalletGetCapitalConfigGetallV1RespItemNetworkListInner from a dict
wallet_get_capital_config_getall_v1_resp_item_network_list_inner_from_dict = WalletGetCapitalConfigGetallV1RespItemNetworkListInner.from_dict(wallet_get_capital_config_getall_v1_resp_item_network_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


