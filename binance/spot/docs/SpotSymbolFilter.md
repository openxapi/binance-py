# SpotSymbolFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_max_to_market** | **bool** |  | [optional] 
**apply_min_to_market** | **bool** |  | [optional] 
**apply_to_market** | **bool** |  | [optional] 
**ask_multiplier_down** | **str** |  | [optional] 
**ask_multiplier_up** | **str** |  | [optional] 
**avg_price_mins** | **int** |  | [optional] 
**bid_multiplier_down** | **str** |  | [optional] 
**bid_multiplier_up** | **str** |  | [optional] 
**filter_type** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**max_notional_value** | **str** |  | [optional] 
**max_num_algo_orders** | **int** |  | [optional] 
**max_num_iceberg_orders** | **int** |  | [optional] 
**max_num_orders** | **int** |  | [optional] 
**max_position** | **str** |  | [optional] 
**max_price** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**max_trailing_above_delta** | **int** |  | [optional] 
**max_trailing_below_delta** | **int** |  | [optional] 
**min_notional_value** | **str** |  | [optional] 
**min_price** | **str** |  | [optional] 
**min_qty** | **str** |  | [optional] 
**min_trailing_above_delta** | **int** |  | [optional] 
**min_trailing_below_delta** | **int** |  | [optional] 
**multiplier_down** | **str** |  | [optional] 
**multiplier_up** | **str** |  | [optional] 
**step_size** | **str** |  | [optional] 
**tick_size** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_symbol_filter import SpotSymbolFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SpotSymbolFilter from a JSON string
spot_symbol_filter_instance = SpotSymbolFilter.from_json(json)
# print the JSON string representation of the object
print(SpotSymbolFilter.to_json())

# convert the object into a dict
spot_symbol_filter_dict = spot_symbol_filter_instance.to_dict()
# create an instance of SpotSymbolFilter from a dict
spot_symbol_filter_from_dict = SpotSymbolFilter.from_dict(spot_symbol_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


