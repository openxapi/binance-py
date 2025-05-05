# CreateAssetDustV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_service_charge** | **str** |  | [optional] 
**total_transfered** | **str** |  | [optional] 
**transfer_result** | [**List[CreateAssetDustV1RespTransferResultInner]**](CreateAssetDustV1RespTransferResultInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.create_asset_dust_v1_resp import CreateAssetDustV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetDustV1Resp from a JSON string
create_asset_dust_v1_resp_instance = CreateAssetDustV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateAssetDustV1Resp.to_json())

# convert the object into a dict
create_asset_dust_v1_resp_dict = create_asset_dust_v1_resp_instance.to_dict()
# create an instance of CreateAssetDustV1Resp from a dict
create_asset_dust_v1_resp_from_dict = CreateAssetDustV1Resp.from_dict(create_asset_dust_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


