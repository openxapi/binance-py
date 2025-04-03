# UmfuturesGetIndexInfoV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset_list** | [**List[UmfuturesGetIndexInfoV1RespItemBaseAssetListInner]**](UmfuturesGetIndexInfoV1RespItemBaseAssetListInner.md) |  | [optional] 
**component** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_index_info_v1_resp_item import UmfuturesGetIndexInfoV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetIndexInfoV1RespItem from a JSON string
umfutures_get_index_info_v1_resp_item_instance = UmfuturesGetIndexInfoV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetIndexInfoV1RespItem.to_json())

# convert the object into a dict
umfutures_get_index_info_v1_resp_item_dict = umfutures_get_index_info_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetIndexInfoV1RespItem from a dict
umfutures_get_index_info_v1_resp_item_from_dict = UmfuturesGetIndexInfoV1RespItem.from_dict(umfutures_get_index_info_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


