# AlgoGetAlgoFuturesOpenOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner]**](AlgoGetAlgoFuturesHistoricalOrdersV1RespOrdersInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.algo.models.algo_get_algo_futures_open_orders_v1_resp import AlgoGetAlgoFuturesOpenOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoGetAlgoFuturesOpenOrdersV1Resp from a JSON string
algo_get_algo_futures_open_orders_v1_resp_instance = AlgoGetAlgoFuturesOpenOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(AlgoGetAlgoFuturesOpenOrdersV1Resp.to_json())

# convert the object into a dict
algo_get_algo_futures_open_orders_v1_resp_dict = algo_get_algo_futures_open_orders_v1_resp_instance.to_dict()
# create an instance of AlgoGetAlgoFuturesOpenOrdersV1Resp from a dict
algo_get_algo_futures_open_orders_v1_resp_from_dict = AlgoGetAlgoFuturesOpenOrdersV1Resp.from_dict(algo_get_algo_futures_open_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


