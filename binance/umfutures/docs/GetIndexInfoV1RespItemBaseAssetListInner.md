# GetIndexInfoV1RespItemBaseAssetListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset** | **str** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**weight_in_percentage** | **str** |  | [optional] 
**weight_in_quantity** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_index_info_v1_resp_item_base_asset_list_inner import GetIndexInfoV1RespItemBaseAssetListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndexInfoV1RespItemBaseAssetListInner from a JSON string
get_index_info_v1_resp_item_base_asset_list_inner_instance = GetIndexInfoV1RespItemBaseAssetListInner.from_json(json)
# print the JSON string representation of the object
print(GetIndexInfoV1RespItemBaseAssetListInner.to_json())

# convert the object into a dict
get_index_info_v1_resp_item_base_asset_list_inner_dict = get_index_info_v1_resp_item_base_asset_list_inner_instance.to_dict()
# create an instance of GetIndexInfoV1RespItemBaseAssetListInner from a dict
get_index_info_v1_resp_item_base_asset_list_inner_from_dict = GetIndexInfoV1RespItemBaseAssetListInner.from_dict(get_index_info_v1_resp_item_base_asset_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


