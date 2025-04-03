# AlgoCreateAlgoSpotNewOrderTwapV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_algo_id** | **str** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.algo.models.algo_create_algo_spot_new_order_twap_v1_resp import AlgoCreateAlgoSpotNewOrderTwapV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of AlgoCreateAlgoSpotNewOrderTwapV1Resp from a JSON string
algo_create_algo_spot_new_order_twap_v1_resp_instance = AlgoCreateAlgoSpotNewOrderTwapV1Resp.from_json(json)
# print the JSON string representation of the object
print(AlgoCreateAlgoSpotNewOrderTwapV1Resp.to_json())

# convert the object into a dict
algo_create_algo_spot_new_order_twap_v1_resp_dict = algo_create_algo_spot_new_order_twap_v1_resp_instance.to_dict()
# create an instance of AlgoCreateAlgoSpotNewOrderTwapV1Resp from a dict
algo_create_algo_spot_new_order_twap_v1_resp_from_dict = AlgoCreateAlgoSpotNewOrderTwapV1Resp.from_dict(algo_create_algo_spot_new_order_twap_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


