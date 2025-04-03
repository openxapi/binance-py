# SpotGetExchangeInfoV3RespExchangeFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** |  | [optional] 
**max_num_orders** | **int** |  | [optional] 
**max_num_algo_orders** | **int** |  | [optional] 
**max_num_iceberg_orders** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_exchange_info_v3_resp_exchange_filters_inner import SpotGetExchangeInfoV3RespExchangeFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetExchangeInfoV3RespExchangeFiltersInner from a JSON string
spot_get_exchange_info_v3_resp_exchange_filters_inner_instance = SpotGetExchangeInfoV3RespExchangeFiltersInner.from_json(json)
# print the JSON string representation of the object
print(SpotGetExchangeInfoV3RespExchangeFiltersInner.to_json())

# convert the object into a dict
spot_get_exchange_info_v3_resp_exchange_filters_inner_dict = spot_get_exchange_info_v3_resp_exchange_filters_inner_instance.to_dict()
# create an instance of SpotGetExchangeInfoV3RespExchangeFiltersInner from a dict
spot_get_exchange_info_v3_resp_exchange_filters_inner_from_dict = SpotGetExchangeInfoV3RespExchangeFiltersInner.from_dict(spot_get_exchange_info_v3_resp_exchange_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


