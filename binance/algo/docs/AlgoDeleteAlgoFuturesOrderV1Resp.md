# AlgoDeleteAlgoFuturesOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_id** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.algo.models.algo_delete_algo_futures_order_v1_resp import AlgoDeleteAlgoFuturesOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoDeleteAlgoFuturesOrderV1Resp from a JSON string
algo_delete_algo_futures_order_v1_resp_instance = AlgoDeleteAlgoFuturesOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(AlgoDeleteAlgoFuturesOrderV1Resp.to_json())

# convert the object into a dict
algo_delete_algo_futures_order_v1_resp_dict = algo_delete_algo_futures_order_v1_resp_instance.to_dict()
# create an instance of AlgoDeleteAlgoFuturesOrderV1Resp from a dict
algo_delete_algo_futures_order_v1_resp_from_dict = AlgoDeleteAlgoFuturesOrderV1Resp.from_dict(algo_delete_algo_futures_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


