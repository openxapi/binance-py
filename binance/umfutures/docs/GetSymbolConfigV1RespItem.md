# GetSymbolConfigV1RespItem


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
from binance.umfutures.models.get_symbol_config_v1_resp_item import GetSymbolConfigV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetSymbolConfigV1RespItem from a JSON string
get_symbol_config_v1_resp_item_instance = GetSymbolConfigV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetSymbolConfigV1RespItem.to_json())

# convert the object into a dict
get_symbol_config_v1_resp_item_dict = get_symbol_config_v1_resp_item_instance.to_dict()
# create an instance of GetSymbolConfigV1RespItem from a dict
get_symbol_config_v1_resp_item_from_dict = GetSymbolConfigV1RespItem.from_dict(get_symbol_config_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


