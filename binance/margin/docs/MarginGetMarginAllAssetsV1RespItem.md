# MarginGetMarginAllAssetsV1RespItem


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
from binance.margin.models.margin_get_margin_all_assets_v1_resp_item import MarginGetMarginAllAssetsV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginAllAssetsV1RespItem from a JSON string
margin_get_margin_all_assets_v1_resp_item_instance = MarginGetMarginAllAssetsV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginAllAssetsV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_all_assets_v1_resp_item_dict = margin_get_margin_all_assets_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginAllAssetsV1RespItem from a dict
margin_get_margin_all_assets_v1_resp_item_from_dict = MarginGetMarginAllAssetsV1RespItem.from_dict(margin_get_margin_all_assets_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


