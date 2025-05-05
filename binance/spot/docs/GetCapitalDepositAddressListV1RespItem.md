# GetCapitalDepositAddressListV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**is_default** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_capital_deposit_address_list_v1_resp_item import GetCapitalDepositAddressListV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCapitalDepositAddressListV1RespItem from a JSON string
get_capital_deposit_address_list_v1_resp_item_instance = GetCapitalDepositAddressListV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetCapitalDepositAddressListV1RespItem.to_json())

# convert the object into a dict
get_capital_deposit_address_list_v1_resp_item_dict = get_capital_deposit_address_list_v1_resp_item_instance.to_dict()
# create an instance of GetCapitalDepositAddressListV1RespItem from a dict
get_capital_deposit_address_list_v1_resp_item_from_dict = GetCapitalDepositAddressListV1RespItem.from_dict(get_capital_deposit_address_list_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


