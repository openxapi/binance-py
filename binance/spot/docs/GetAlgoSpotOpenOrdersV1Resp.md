# GetAlgoSpotOpenOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[GetAlgoSpotHistoricalOrdersV1RespOrdersInner]**](GetAlgoSpotHistoricalOrdersV1RespOrdersInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_algo_spot_open_orders_v1_resp import GetAlgoSpotOpenOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlgoSpotOpenOrdersV1Resp from a JSON string
get_algo_spot_open_orders_v1_resp_instance = GetAlgoSpotOpenOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAlgoSpotOpenOrdersV1Resp.to_json())

# convert the object into a dict
get_algo_spot_open_orders_v1_resp_dict = get_algo_spot_open_orders_v1_resp_instance.to_dict()
# create an instance of GetAlgoSpotOpenOrdersV1Resp from a dict
get_algo_spot_open_orders_v1_resp_from_dict = GetAlgoSpotOpenOrdersV1Resp.from_dict(get_algo_spot_open_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


