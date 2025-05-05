# OptionsSymbolFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** |  | [optional] 
**max_price** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**min_price** | **str** |  | [optional] 
**min_qty** | **str** |  | [optional] 
**step_size** | **str** |  | [optional] 
**tick_size** | **str** |  | [optional] 

## Example

```python
from binance.options.models.options_symbol_filter import OptionsSymbolFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsSymbolFilter from a JSON string
options_symbol_filter_instance = OptionsSymbolFilter.from_json(json)
# print the JSON string representation of the object
print(OptionsSymbolFilter.to_json())

# convert the object into a dict
options_symbol_filter_dict = options_symbol_filter_instance.to_dict()
# create an instance of OptionsSymbolFilter from a dict
options_symbol_filter_from_dict = OptionsSymbolFilter.from_dict(options_symbol_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


