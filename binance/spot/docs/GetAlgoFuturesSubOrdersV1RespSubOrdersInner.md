# GetAlgoFuturesSubOrdersV1RespSubOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_id** | **int** |  | [optional] 
**avg_price** | **str** |  | [optional] 
**book_time** | **int** |  | [optional] 
**executed_amt** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fee_amt** | **str** |  | [optional] 
**fee_asset** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_status** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**sub_id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_algo_futures_sub_orders_v1_resp_sub_orders_inner import GetAlgoFuturesSubOrdersV1RespSubOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlgoFuturesSubOrdersV1RespSubOrdersInner from a JSON string
get_algo_futures_sub_orders_v1_resp_sub_orders_inner_instance = GetAlgoFuturesSubOrdersV1RespSubOrdersInner.from_json(json)
# print the JSON string representation of the object
print(GetAlgoFuturesSubOrdersV1RespSubOrdersInner.to_json())

# convert the object into a dict
get_algo_futures_sub_orders_v1_resp_sub_orders_inner_dict = get_algo_futures_sub_orders_v1_resp_sub_orders_inner_instance.to_dict()
# create an instance of GetAlgoFuturesSubOrdersV1RespSubOrdersInner from a dict
get_algo_futures_sub_orders_v1_resp_sub_orders_inner_from_dict = GetAlgoFuturesSubOrdersV1RespSubOrdersInner.from_dict(get_algo_futures_sub_orders_v1_resp_sub_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


