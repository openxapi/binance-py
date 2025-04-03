# UmfuturesGetConvertExchangeInfoV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_asset** | **str** |  | [optional] 
**from_asset_max_amount** | **str** |  | [optional] 
**from_asset_min_amount** | **str** |  | [optional] 
**to_asset** | **str** |  | [optional] 
**to_asset_max_amount** | **str** |  | [optional] 
**to_asset_min_amount** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_convert_exchange_info_v1_resp_item import UmfuturesGetConvertExchangeInfoV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetConvertExchangeInfoV1RespItem from a JSON string
umfutures_get_convert_exchange_info_v1_resp_item_instance = UmfuturesGetConvertExchangeInfoV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetConvertExchangeInfoV1RespItem.to_json())

# convert the object into a dict
umfutures_get_convert_exchange_info_v1_resp_item_dict = umfutures_get_convert_exchange_info_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetConvertExchangeInfoV1RespItem from a dict
umfutures_get_convert_exchange_info_v1_resp_item_from_dict = UmfuturesGetConvertExchangeInfoV1RespItem.from_dict(umfutures_get_convert_exchange_info_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


