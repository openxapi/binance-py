# CmfuturesGetBalanceV1RespItem


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
from binance.derivatives.cmfutures.models.cmfutures_get_balance_v1_resp_item import CmfuturesGetBalanceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetBalanceV1RespItem from a JSON string
cmfutures_get_balance_v1_resp_item_instance = CmfuturesGetBalanceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetBalanceV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_balance_v1_resp_item_dict = cmfutures_get_balance_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetBalanceV1RespItem from a dict
cmfutures_get_balance_v1_resp_item_from_dict = CmfuturesGetBalanceV1RespItem.from_dict(cmfutures_get_balance_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


