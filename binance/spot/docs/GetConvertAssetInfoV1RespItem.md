# GetConvertAssetInfoV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**fraction** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_convert_asset_info_v1_resp_item import GetConvertAssetInfoV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetConvertAssetInfoV1RespItem from a JSON string
get_convert_asset_info_v1_resp_item_instance = GetConvertAssetInfoV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetConvertAssetInfoV1RespItem.to_json())

# convert the object into a dict
get_convert_asset_info_v1_resp_item_dict = get_convert_asset_info_v1_resp_item_instance.to_dict()
# create an instance of GetConvertAssetInfoV1RespItem from a dict
get_convert_asset_info_v1_resp_item_from_dict = GetConvertAssetInfoV1RespItem.from_dict(get_convert_asset_info_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


