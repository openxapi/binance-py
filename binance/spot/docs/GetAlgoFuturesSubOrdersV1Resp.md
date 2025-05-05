# GetAlgoFuturesSubOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executed_amt** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**sub_orders** | [**List[GetAlgoFuturesSubOrdersV1RespSubOrdersInner]**](GetAlgoFuturesSubOrdersV1RespSubOrdersInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_algo_futures_sub_orders_v1_resp import GetAlgoFuturesSubOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlgoFuturesSubOrdersV1Resp from a JSON string
get_algo_futures_sub_orders_v1_resp_instance = GetAlgoFuturesSubOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAlgoFuturesSubOrdersV1Resp.to_json())

# convert the object into a dict
get_algo_futures_sub_orders_v1_resp_dict = get_algo_futures_sub_orders_v1_resp_instance.to_dict()
# create an instance of GetAlgoFuturesSubOrdersV1Resp from a dict
get_algo_futures_sub_orders_v1_resp_from_dict = GetAlgoFuturesSubOrdersV1Resp.from_dict(get_algo_futures_sub_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


