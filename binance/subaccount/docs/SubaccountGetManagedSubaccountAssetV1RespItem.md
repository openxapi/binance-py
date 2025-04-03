# SubaccountGetManagedSubaccountAssetV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_balance** | **str** |  | [optional] 
**btc_value** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**in_order** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**total_balance** | **str** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_asset_v1_resp_item import SubaccountGetManagedSubaccountAssetV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountAssetV1RespItem from a JSON string
subaccount_get_managed_subaccount_asset_v1_resp_item_instance = SubaccountGetManagedSubaccountAssetV1RespItem.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountAssetV1RespItem.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_asset_v1_resp_item_dict = subaccount_get_managed_subaccount_asset_v1_resp_item_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountAssetV1RespItem from a dict
subaccount_get_managed_subaccount_asset_v1_resp_item_from_dict = SubaccountGetManagedSubaccountAssetV1RespItem.from_dict(subaccount_get_managed_subaccount_asset_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


