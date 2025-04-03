# UmfuturesGetBalanceV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_alias** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**available_balance** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 
**cross_un_pnl** | **str** |  | [optional] 
**cross_wallet_balance** | **str** |  | [optional] 
**margin_available** | **bool** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_balance_v3_resp_item import UmfuturesGetBalanceV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetBalanceV3RespItem from a JSON string
umfutures_get_balance_v3_resp_item_instance = UmfuturesGetBalanceV3RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetBalanceV3RespItem.to_json())

# convert the object into a dict
umfutures_get_balance_v3_resp_item_dict = umfutures_get_balance_v3_resp_item_instance.to_dict()
# create an instance of UmfuturesGetBalanceV3RespItem from a dict
umfutures_get_balance_v3_resp_item_from_dict = UmfuturesGetBalanceV3RespItem.from_dict(umfutures_get_balance_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


