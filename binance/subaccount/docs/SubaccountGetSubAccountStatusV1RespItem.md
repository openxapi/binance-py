# SubaccountGetSubAccountStatusV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**insert_time** | **int** |  | [optional] 
**is_future_enabled** | **bool** |  | [optional] 
**is_margin_enabled** | **bool** |  | [optional] 
**is_sub_user_enabled** | **bool** |  | [optional] 
**is_user_active** | **bool** |  | [optional] 
**mobile** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_status_v1_resp_item import SubaccountGetSubAccountStatusV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountStatusV1RespItem from a JSON string
subaccount_get_sub_account_status_v1_resp_item_instance = SubaccountGetSubAccountStatusV1RespItem.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountStatusV1RespItem.to_json())

# convert the object into a dict
subaccount_get_sub_account_status_v1_resp_item_dict = subaccount_get_sub_account_status_v1_resp_item_instance.to_dict()
# create an instance of SubaccountGetSubAccountStatusV1RespItem from a dict
subaccount_get_sub_account_status_v1_resp_item_from_dict = SubaccountGetSubAccountStatusV1RespItem.from_dict(subaccount_get_sub_account_status_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


