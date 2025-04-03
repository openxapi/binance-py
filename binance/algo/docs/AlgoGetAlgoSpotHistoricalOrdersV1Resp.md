# AlgoGetAlgoSpotHistoricalOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner]**](AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.algo.models.algo_get_algo_spot_historical_orders_v1_resp import AlgoGetAlgoSpotHistoricalOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoGetAlgoSpotHistoricalOrdersV1Resp from a JSON string
algo_get_algo_spot_historical_orders_v1_resp_instance = AlgoGetAlgoSpotHistoricalOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(AlgoGetAlgoSpotHistoricalOrdersV1Resp.to_json())

# convert the object into a dict
algo_get_algo_spot_historical_orders_v1_resp_dict = algo_get_algo_spot_historical_orders_v1_resp_instance.to_dict()
# create an instance of AlgoGetAlgoSpotHistoricalOrdersV1Resp from a dict
algo_get_algo_spot_historical_orders_v1_resp_from_dict = AlgoGetAlgoSpotHistoricalOrdersV1Resp.from_dict(algo_get_algo_spot_historical_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


