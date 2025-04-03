# AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner


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
from binance.algo.models.algo_get_algo_futures_sub_orders_v1_resp_sub_orders_inner import AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner from a JSON string
algo_get_algo_futures_sub_orders_v1_resp_sub_orders_inner_instance = AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner.from_json(json)
# print the JSON string representation of the object
print(AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner.to_json())

# convert the object into a dict
algo_get_algo_futures_sub_orders_v1_resp_sub_orders_inner_dict = algo_get_algo_futures_sub_orders_v1_resp_sub_orders_inner_instance.to_dict()
# create an instance of AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner from a dict
algo_get_algo_futures_sub_orders_v1_resp_sub_orders_inner_from_dict = AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner.from_dict(algo_get_algo_futures_sub_orders_v1_resp_sub_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


