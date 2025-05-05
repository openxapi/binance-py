# GetIndexInfoV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset_list** | [**List[GetIndexInfoV1RespItemBaseAssetListInner]**](GetIndexInfoV1RespItemBaseAssetListInner.md) |  | [optional] 
**component** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_index_info_v1_resp_item import GetIndexInfoV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndexInfoV1RespItem from a JSON string
get_index_info_v1_resp_item_instance = GetIndexInfoV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetIndexInfoV1RespItem.to_json())

# convert the object into a dict
get_index_info_v1_resp_item_dict = get_index_info_v1_resp_item_instance.to_dict()
# create an instance of GetIndexInfoV1RespItem from a dict
get_index_info_v1_resp_item_from_dict = GetIndexInfoV1RespItem.from_dict(get_index_info_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


