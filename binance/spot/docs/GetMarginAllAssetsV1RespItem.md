# GetMarginAllAssetsV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_full_name** | **str** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**delist_time** | **int** |  | [optional] 
**is_borrowable** | **bool** |  | [optional] 
**is_mortgageable** | **bool** |  | [optional] 
**user_min_borrow** | **str** |  | [optional] 
**user_min_repay** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_all_assets_v1_resp_item import GetMarginAllAssetsV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginAllAssetsV1RespItem from a JSON string
get_margin_all_assets_v1_resp_item_instance = GetMarginAllAssetsV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginAllAssetsV1RespItem.to_json())

# convert the object into a dict
get_margin_all_assets_v1_resp_item_dict = get_margin_all_assets_v1_resp_item_instance.to_dict()
# create an instance of GetMarginAllAssetsV1RespItem from a dict
get_margin_all_assets_v1_resp_item_from_dict = GetMarginAllAssetsV1RespItem.from_dict(get_margin_all_assets_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


