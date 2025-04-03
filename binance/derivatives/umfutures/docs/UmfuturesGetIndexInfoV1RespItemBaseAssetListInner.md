# UmfuturesGetIndexInfoV1RespItemBaseAssetListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset** | **str** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**weight_in_percentage** | **str** |  | [optional] 
**weight_in_quantity** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_index_info_v1_resp_item_base_asset_list_inner import UmfuturesGetIndexInfoV1RespItemBaseAssetListInner

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetIndexInfoV1RespItemBaseAssetListInner from a JSON string
umfutures_get_index_info_v1_resp_item_base_asset_list_inner_instance = UmfuturesGetIndexInfoV1RespItemBaseAssetListInner.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetIndexInfoV1RespItemBaseAssetListInner.to_json())

# convert the object into a dict
umfutures_get_index_info_v1_resp_item_base_asset_list_inner_dict = umfutures_get_index_info_v1_resp_item_base_asset_list_inner_instance.to_dict()
# create an instance of UmfuturesGetIndexInfoV1RespItemBaseAssetListInner from a dict
umfutures_get_index_info_v1_resp_item_base_asset_list_inner_from_dict = UmfuturesGetIndexInfoV1RespItemBaseAssetListInner.from_dict(umfutures_get_index_info_v1_resp_item_base_asset_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


