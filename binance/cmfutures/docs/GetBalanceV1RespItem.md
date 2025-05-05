# GetBalanceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_alias** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**available_balance** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 
**cross_un_pnl** | **str** |  | [optional] 
**cross_wallet_balance** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**withdraw_available** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_balance_v1_resp_item import GetBalanceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalanceV1RespItem from a JSON string
get_balance_v1_resp_item_instance = GetBalanceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBalanceV1RespItem.to_json())

# convert the object into a dict
get_balance_v1_resp_item_dict = get_balance_v1_resp_item_instance.to_dict()
# create an instance of GetBalanceV1RespItem from a dict
get_balance_v1_resp_item_from_dict = GetBalanceV1RespItem.from_dict(get_balance_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


