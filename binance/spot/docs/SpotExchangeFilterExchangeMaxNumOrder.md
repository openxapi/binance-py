# SpotExchangeFilterExchangeMaxNumOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** |  | [optional] 
**max_num_orders** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_exchange_filter_exchange_max_num_order import SpotExchangeFilterExchangeMaxNumOrder

# TODO update the JSON string below
json = "{}"
# create an instance of SpotExchangeFilterExchangeMaxNumOrder from a JSON string
spot_exchange_filter_exchange_max_num_order_instance = SpotExchangeFilterExchangeMaxNumOrder.from_json(json)
# print the JSON string representation of the object
print(SpotExchangeFilterExchangeMaxNumOrder.to_json())

# convert the object into a dict
spot_exchange_filter_exchange_max_num_order_dict = spot_exchange_filter_exchange_max_num_order_instance.to_dict()
# create an instance of SpotExchangeFilterExchangeMaxNumOrder from a dict
spot_exchange_filter_exchange_max_num_order_from_dict = SpotExchangeFilterExchangeMaxNumOrder.from_dict(spot_exchange_filter_exchange_max_num_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


