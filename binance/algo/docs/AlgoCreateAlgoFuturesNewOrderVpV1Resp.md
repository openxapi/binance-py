# AlgoCreateAlgoFuturesNewOrderVpV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_algo_id** | **str** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.algo.models.algo_create_algo_futures_new_order_vp_v1_resp import AlgoCreateAlgoFuturesNewOrderVpV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoCreateAlgoFuturesNewOrderVpV1Resp from a JSON string
algo_create_algo_futures_new_order_vp_v1_resp_instance = AlgoCreateAlgoFuturesNewOrderVpV1Resp.from_json(json)
# print the JSON string representation of the object
print(AlgoCreateAlgoFuturesNewOrderVpV1Resp.to_json())

# convert the object into a dict
algo_create_algo_futures_new_order_vp_v1_resp_dict = algo_create_algo_futures_new_order_vp_v1_resp_instance.to_dict()
# create an instance of AlgoCreateAlgoFuturesNewOrderVpV1Resp from a dict
algo_create_algo_futures_new_order_vp_v1_resp_from_dict = AlgoCreateAlgoFuturesNewOrderVpV1Resp.from_dict(algo_create_algo_futures_new_order_vp_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


