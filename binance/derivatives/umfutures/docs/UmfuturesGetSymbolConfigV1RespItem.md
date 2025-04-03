# UmfuturesGetSymbolConfigV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_add_margin** | **str** |  | [optional] 
**leverage** | **int** |  | [optional] 
**margin_type** | **str** |  | [optional] 
**max_notional_value** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_symbol_config_v1_resp_item import UmfuturesGetSymbolConfigV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetSymbolConfigV1RespItem from a JSON string
umfutures_get_symbol_config_v1_resp_item_instance = UmfuturesGetSymbolConfigV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetSymbolConfigV1RespItem.to_json())

# convert the object into a dict
umfutures_get_symbol_config_v1_resp_item_dict = umfutures_get_symbol_config_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetSymbolConfigV1RespItem from a dict
umfutures_get_symbol_config_v1_resp_item_from_dict = UmfuturesGetSymbolConfigV1RespItem.from_dict(umfutures_get_symbol_config_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


