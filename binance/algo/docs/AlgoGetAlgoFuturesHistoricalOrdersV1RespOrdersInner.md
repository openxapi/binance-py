# AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_id** | **int** |  | [optional] 
**algo_status** | **str** |  | [optional] 
**algo_type** | **str** |  | [optional] 
**avg_price** | **str** |  | [optional] 
**book_time** | **int** |  | [optional] 
**client_algo_id** | **str** |  | [optional] 
**end_time** | **int** |  | [optional] 
**executed_amt** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**total_qty** | **str** |  | [optional] 
**urgency** | **str** |  | [optional] 

## Example

```python
from binance.algo.models.algo_get_algo_futures_historical_orders_v1_resp_orders_inner import AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner from a JSON string
algo_get_algo_futures_historical_orders_v1_resp_orders_inner_instance = AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner.from_json(json)
# print the JSON string representation of the object
print(AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner.to_json())

# convert the object into a dict
algo_get_algo_futures_historical_orders_v1_resp_orders_inner_dict = algo_get_algo_futures_historical_orders_v1_resp_orders_inner_instance.to_dict()
# create an instance of AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner from a dict
algo_get_algo_futures_historical_orders_v1_resp_orders_inner_from_dict = AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner.from_dict(algo_get_algo_futures_historical_orders_v1_resp_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


