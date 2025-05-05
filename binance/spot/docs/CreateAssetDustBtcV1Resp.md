# CreateAssetDustBtcV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[CreateAssetDustBtcV1RespDetailsInner]**](CreateAssetDustBtcV1RespDetailsInner.md) |  | [optional] 
**dribblet_percentage** | **str** |  | [optional] 
**total_transfer_bnb** | **str** |  | [optional] 
**total_transfer_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_asset_dust_btc_v1_resp import CreateAssetDustBtcV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetDustBtcV1Resp from a JSON string
create_asset_dust_btc_v1_resp_instance = CreateAssetDustBtcV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateAssetDustBtcV1Resp.to_json())

# convert the object into a dict
create_asset_dust_btc_v1_resp_dict = create_asset_dust_btc_v1_resp_instance.to_dict()
# create an instance of CreateAssetDustBtcV1Resp from a dict
create_asset_dust_btc_v1_resp_from_dict = CreateAssetDustBtcV1Resp.from_dict(create_asset_dust_btc_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


