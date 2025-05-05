# GetManagedSubaccountAssetV1RespItem


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
from binance.spot.models.get_managed_subaccount_asset_v1_resp_item import GetManagedSubaccountAssetV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountAssetV1RespItem from a JSON string
get_managed_subaccount_asset_v1_resp_item_instance = GetManagedSubaccountAssetV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountAssetV1RespItem.to_json())

# convert the object into a dict
get_managed_subaccount_asset_v1_resp_item_dict = get_managed_subaccount_asset_v1_resp_item_instance.to_dict()
# create an instance of GetManagedSubaccountAssetV1RespItem from a dict
get_managed_subaccount_asset_v1_resp_item_from_dict = GetManagedSubaccountAssetV1RespItem.from_dict(get_managed_subaccount_asset_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


