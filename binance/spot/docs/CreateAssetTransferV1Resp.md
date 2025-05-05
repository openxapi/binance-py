# CreateAssetTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_asset_transfer_v1_resp import CreateAssetTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetTransferV1Resp from a JSON string
create_asset_transfer_v1_resp_instance = CreateAssetTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateAssetTransferV1Resp.to_json())

# convert the object into a dict
create_asset_transfer_v1_resp_dict = create_asset_transfer_v1_resp_instance.to_dict()
# create an instance of CreateAssetTransferV1Resp from a dict
create_asset_transfer_v1_resp_from_dict = CreateAssetTransferV1Resp.from_dict(create_asset_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


