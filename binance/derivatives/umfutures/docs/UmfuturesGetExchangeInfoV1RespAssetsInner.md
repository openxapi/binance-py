# UmfuturesGetExchangeInfoV1RespAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**auto_asset_exchange** | **int** |  | [optional] 
**margin_available** | **bool** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_assets_inner import UmfuturesGetExchangeInfoV1RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetExchangeInfoV1RespAssetsInner from a JSON string
umfutures_get_exchange_info_v1_resp_assets_inner_instance = UmfuturesGetExchangeInfoV1RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetExchangeInfoV1RespAssetsInner.to_json())

# convert the object into a dict
umfutures_get_exchange_info_v1_resp_assets_inner_dict = umfutures_get_exchange_info_v1_resp_assets_inner_instance.to_dict()
# create an instance of UmfuturesGetExchangeInfoV1RespAssetsInner from a dict
umfutures_get_exchange_info_v1_resp_assets_inner_from_dict = UmfuturesGetExchangeInfoV1RespAssetsInner.from_dict(umfutures_get_exchange_info_v1_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


