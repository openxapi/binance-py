# WalletGetCapitalConfigGetallV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coin** | **str** |  | [optional] 
**deposit_all_enable** | **bool** |  | [optional] 
**free** | **str** |  | [optional] 
**freeze** | **str** |  | [optional] 
**ipoable** | **str** |  | [optional] 
**ipoing** | **str** |  | [optional] 
**is_legal_money** | **bool** |  | [optional] 
**locked** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**network_list** | [**List[WalletGetCapitalConfigGetallV1RespItemNetworkListInner]**](WalletGetCapitalConfigGetallV1RespItemNetworkListInner.md) |  | [optional] 
**storage** | **str** |  | [optional] 
**trading** | **bool** |  | [optional] 
**withdraw_all_enable** | **bool** |  | [optional] 
**withdrawing** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_capital_config_getall_v1_resp_item import WalletGetCapitalConfigGetallV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetCapitalConfigGetallV1RespItem from a JSON string
wallet_get_capital_config_getall_v1_resp_item_instance = WalletGetCapitalConfigGetallV1RespItem.from_json(json)
# print the JSON string representation of the object
print(WalletGetCapitalConfigGetallV1RespItem.to_json())

# convert the object into a dict
wallet_get_capital_config_getall_v1_resp_item_dict = wallet_get_capital_config_getall_v1_resp_item_instance.to_dict()
# create an instance of WalletGetCapitalConfigGetallV1RespItem from a dict
wallet_get_capital_config_getall_v1_resp_item_from_dict = WalletGetCapitalConfigGetallV1RespItem.from_dict(wallet_get_capital_config_getall_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


