# CmfuturesSymbolFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**max_price** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**min_price** | **str** |  | [optional] 
**min_qty** | **str** |  | [optional] 
**multiplier_decimal** | **int** |  | [optional] 
**multiplier_down** | **str** |  | [optional] 
**multiplier_up** | **str** |  | [optional] 
**step_size** | **str** |  | [optional] 
**tick_size** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_symbol_filter import CmfuturesSymbolFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesSymbolFilter from a JSON string
cmfutures_symbol_filter_instance = CmfuturesSymbolFilter.from_json(json)
# print the JSON string representation of the object
print(CmfuturesSymbolFilter.to_json())

# convert the object into a dict
cmfutures_symbol_filter_dict = cmfutures_symbol_filter_instance.to_dict()
# create an instance of CmfuturesSymbolFilter from a dict
cmfutures_symbol_filter_from_dict = CmfuturesSymbolFilter.from_dict(cmfutures_symbol_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


