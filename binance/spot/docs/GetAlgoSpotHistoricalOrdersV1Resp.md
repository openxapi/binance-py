# GetAlgoSpotHistoricalOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[GetAlgoSpotHistoricalOrdersV1RespOrdersInner]**](GetAlgoSpotHistoricalOrdersV1RespOrdersInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_algo_spot_historical_orders_v1_resp import GetAlgoSpotHistoricalOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlgoSpotHistoricalOrdersV1Resp from a JSON string
get_algo_spot_historical_orders_v1_resp_instance = GetAlgoSpotHistoricalOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAlgoSpotHistoricalOrdersV1Resp.to_json())

# convert the object into a dict
get_algo_spot_historical_orders_v1_resp_dict = get_algo_spot_historical_orders_v1_resp_instance.to_dict()
# create an instance of GetAlgoSpotHistoricalOrdersV1Resp from a dict
get_algo_spot_historical_orders_v1_resp_from_dict = GetAlgoSpotHistoricalOrdersV1Resp.from_dict(get_algo_spot_historical_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


