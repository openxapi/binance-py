# GetAssetTransferV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**tran_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_transfer_v1_resp_rows_inner import GetAssetTransferV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTransferV1RespRowsInner from a JSON string
get_asset_transfer_v1_resp_rows_inner_instance = GetAssetTransferV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetTransferV1RespRowsInner.to_json())

# convert the object into a dict
get_asset_transfer_v1_resp_rows_inner_dict = get_asset_transfer_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetAssetTransferV1RespRowsInner from a dict
get_asset_transfer_v1_resp_rows_inner_from_dict = GetAssetTransferV1RespRowsInner.from_dict(get_asset_transfer_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


