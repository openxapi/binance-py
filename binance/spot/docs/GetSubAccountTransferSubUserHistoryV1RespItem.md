# GetSubAccountTransferSubUserHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**counter_party** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**from_account_type** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**to_account_type** | **str** |  | [optional] 
**tran_id** | **int** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_transfer_sub_user_history_v1_resp_item import GetSubAccountTransferSubUserHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountTransferSubUserHistoryV1RespItem from a JSON string
get_sub_account_transfer_sub_user_history_v1_resp_item_instance = GetSubAccountTransferSubUserHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountTransferSubUserHistoryV1RespItem.to_json())

# convert the object into a dict
get_sub_account_transfer_sub_user_history_v1_resp_item_dict = get_sub_account_transfer_sub_user_history_v1_resp_item_instance.to_dict()
# create an instance of GetSubAccountTransferSubUserHistoryV1RespItem from a dict
get_sub_account_transfer_sub_user_history_v1_resp_item_from_dict = GetSubAccountTransferSubUserHistoryV1RespItem.from_dict(get_sub_account_transfer_sub_user_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


