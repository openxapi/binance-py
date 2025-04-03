# ConvertGetConvertAssetInfoV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**fraction** | **int** |  | [optional] 

## Example

```python
from binance.convert.models.convert_get_convert_asset_info_v1_resp_item import ConvertGetConvertAssetInfoV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGetConvertAssetInfoV1RespItem from a JSON string
convert_get_convert_asset_info_v1_resp_item_instance = ConvertGetConvertAssetInfoV1RespItem.from_json(json)
# print the JSON string representation of the object
print(ConvertGetConvertAssetInfoV1RespItem.to_json())

# convert the object into a dict
convert_get_convert_asset_info_v1_resp_item_dict = convert_get_convert_asset_info_v1_resp_item_instance.to_dict()
# create an instance of ConvertGetConvertAssetInfoV1RespItem from a dict
convert_get_convert_asset_info_v1_resp_item_from_dict = ConvertGetConvertAssetInfoV1RespItem.from_dict(convert_get_convert_asset_info_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


