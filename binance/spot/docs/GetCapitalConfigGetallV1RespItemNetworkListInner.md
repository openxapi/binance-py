# GetCapitalConfigGetallV1RespItemNetworkListInner


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
from binance.spot.models.get_capital_config_getall_v1_resp_item_network_list_inner import GetCapitalConfigGetallV1RespItemNetworkListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCapitalConfigGetallV1RespItemNetworkListInner from a JSON string
get_capital_config_getall_v1_resp_item_network_list_inner_instance = GetCapitalConfigGetallV1RespItemNetworkListInner.from_json(json)
# print the JSON string representation of the object
print(GetCapitalConfigGetallV1RespItemNetworkListInner.to_json())

# convert the object into a dict
get_capital_config_getall_v1_resp_item_network_list_inner_dict = get_capital_config_getall_v1_resp_item_network_list_inner_instance.to_dict()
# create an instance of GetCapitalConfigGetallV1RespItemNetworkListInner from a dict
get_capital_config_getall_v1_resp_item_network_list_inner_from_dict = GetCapitalConfigGetallV1RespItemNetworkListInner.from_dict(get_capital_config_getall_v1_resp_item_network_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


