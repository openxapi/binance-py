# CreateAssetGetUserAssetV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**btc_valuation** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**freeze** | **str** |  | [optional] 
**ipoable** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**withdrawing** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_asset_get_user_asset_v3_resp_item import CreateAssetGetUserAssetV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetGetUserAssetV3RespItem from a JSON string
create_asset_get_user_asset_v3_resp_item_instance = CreateAssetGetUserAssetV3RespItem.from_json(json)
# print the JSON string representation of the object
print(CreateAssetGetUserAssetV3RespItem.to_json())

# convert the object into a dict
create_asset_get_user_asset_v3_resp_item_dict = create_asset_get_user_asset_v3_resp_item_instance.to_dict()
# create an instance of CreateAssetGetUserAssetV3RespItem from a dict
create_asset_get_user_asset_v3_resp_item_from_dict = CreateAssetGetUserAssetV3RespItem.from_dict(create_asset_get_user_asset_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


