# GetAssetTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetAssetTransferV1RespRowsInner]**](GetAssetTransferV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_transfer_v1_resp import GetAssetTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTransferV1Resp from a JSON string
get_asset_transfer_v1_resp_instance = GetAssetTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAssetTransferV1Resp.to_json())

# convert the object into a dict
get_asset_transfer_v1_resp_dict = get_asset_transfer_v1_resp_instance.to_dict()
# create an instance of GetAssetTransferV1Resp from a dict
get_asset_transfer_v1_resp_from_dict = GetAssetTransferV1Resp.from_dict(get_asset_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


