# CreateAssetDustBtcV1RespDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_free** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**asset_full_name** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**to_bnb** | **str** |  | [optional] 
**to_bnb_off_exchange** | **str** |  | [optional] 
**to_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_asset_dust_btc_v1_resp_details_inner import CreateAssetDustBtcV1RespDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetDustBtcV1RespDetailsInner from a JSON string
create_asset_dust_btc_v1_resp_details_inner_instance = CreateAssetDustBtcV1RespDetailsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAssetDustBtcV1RespDetailsInner.to_json())

# convert the object into a dict
create_asset_dust_btc_v1_resp_details_inner_dict = create_asset_dust_btc_v1_resp_details_inner_instance.to_dict()
# create an instance of CreateAssetDustBtcV1RespDetailsInner from a dict
create_asset_dust_btc_v1_resp_details_inner_from_dict = CreateAssetDustBtcV1RespDetailsInner.from_dict(create_asset_dust_btc_v1_resp_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


