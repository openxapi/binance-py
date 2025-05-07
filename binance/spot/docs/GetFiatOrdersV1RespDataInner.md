# GetFiatOrdersV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**fiat_currency** | **str** |  | [optional] 
**indicated_amount** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_fee** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_fiat_orders_v1_resp_data_inner import GetFiatOrdersV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFiatOrdersV1RespDataInner from a JSON string
get_fiat_orders_v1_resp_data_inner_instance = GetFiatOrdersV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetFiatOrdersV1RespDataInner.to_json())

# convert the object into a dict
get_fiat_orders_v1_resp_data_inner_dict = get_fiat_orders_v1_resp_data_inner_instance.to_dict()
# create an instance of GetFiatOrdersV1RespDataInner from a dict
get_fiat_orders_v1_resp_data_inner_from_dict = GetFiatOrdersV1RespDataInner.from_dict(get_fiat_orders_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


