# GetUmSymbolConfigV1RespItem


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
from binance.pmargin.models.get_um_symbol_config_v1_resp_item import GetUmSymbolConfigV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmSymbolConfigV1RespItem from a JSON string
get_um_symbol_config_v1_resp_item_instance = GetUmSymbolConfigV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetUmSymbolConfigV1RespItem.to_json())

# convert the object into a dict
get_um_symbol_config_v1_resp_item_dict = get_um_symbol_config_v1_resp_item_instance.to_dict()
# create an instance of GetUmSymbolConfigV1RespItem from a dict
get_um_symbol_config_v1_resp_item_from_dict = GetUmSymbolConfigV1RespItem.from_dict(get_um_symbol_config_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


