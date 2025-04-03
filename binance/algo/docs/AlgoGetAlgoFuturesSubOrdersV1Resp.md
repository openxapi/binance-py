# AlgoGetAlgoFuturesSubOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executed_amt** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**sub_orders** | [**List[AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner]**](AlgoGetAlgoFuturesSubOrdersV1RespSubOrdersInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.algo.models.algo_get_algo_futures_sub_orders_v1_resp import AlgoGetAlgoFuturesSubOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoGetAlgoFuturesSubOrdersV1Resp from a JSON string
algo_get_algo_futures_sub_orders_v1_resp_instance = AlgoGetAlgoFuturesSubOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(AlgoGetAlgoFuturesSubOrdersV1Resp.to_json())

# convert the object into a dict
algo_get_algo_futures_sub_orders_v1_resp_dict = algo_get_algo_futures_sub_orders_v1_resp_instance.to_dict()
# create an instance of AlgoGetAlgoFuturesSubOrdersV1Resp from a dict
algo_get_algo_futures_sub_orders_v1_resp_from_dict = AlgoGetAlgoFuturesSubOrdersV1Resp.from_dict(algo_get_algo_futures_sub_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


