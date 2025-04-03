# SubaccountGetSubAccountSubTransferHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**to** | **str** |  | [optional] 
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_sub_transfer_history_v1_resp_item import SubaccountGetSubAccountSubTransferHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountSubTransferHistoryV1RespItem from a JSON string
subaccount_get_sub_account_sub_transfer_history_v1_resp_item_instance = SubaccountGetSubAccountSubTransferHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountSubTransferHistoryV1RespItem.to_json())

# convert the object into a dict
subaccount_get_sub_account_sub_transfer_history_v1_resp_item_dict = subaccount_get_sub_account_sub_transfer_history_v1_resp_item_instance.to_dict()
# create an instance of SubaccountGetSubAccountSubTransferHistoryV1RespItem from a dict
subaccount_get_sub_account_sub_transfer_history_v1_resp_item_from_dict = SubaccountGetSubAccountSubTransferHistoryV1RespItem.from_dict(subaccount_get_sub_account_sub_transfer_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


