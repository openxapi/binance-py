# GetCapitalWithdrawHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**apply_time** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**complete_time** | **str** |  | [optional] 
**confirm_no** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**transaction_fee** | **str** |  | [optional] 
**transfer_type** | **int** |  | [optional] 
**tx_id** | **str** |  | [optional] 
**tx_key** | **str** |  | [optional] 
**wallet_type** | **int** |  | [optional] 
**withdraw_order_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_capital_withdraw_history_v1_resp_item import GetCapitalWithdrawHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCapitalWithdrawHistoryV1RespItem from a JSON string
get_capital_withdraw_history_v1_resp_item_instance = GetCapitalWithdrawHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetCapitalWithdrawHistoryV1RespItem.to_json())

# convert the object into a dict
get_capital_withdraw_history_v1_resp_item_dict = get_capital_withdraw_history_v1_resp_item_instance.to_dict()
# create an instance of GetCapitalWithdrawHistoryV1RespItem from a dict
get_capital_withdraw_history_v1_resp_item_from_dict = GetCapitalWithdrawHistoryV1RespItem.from_dict(get_capital_withdraw_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


