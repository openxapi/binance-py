# CreateAlgoSpotNewOrderTwapV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_algo_id** | **str** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_algo_spot_new_order_twap_v1_resp import CreateAlgoSpotNewOrderTwapV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlgoSpotNewOrderTwapV1Resp from a JSON string
create_algo_spot_new_order_twap_v1_resp_instance = CreateAlgoSpotNewOrderTwapV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateAlgoSpotNewOrderTwapV1Resp.to_json())

# convert the object into a dict
create_algo_spot_new_order_twap_v1_resp_dict = create_algo_spot_new_order_twap_v1_resp_instance.to_dict()
# create an instance of CreateAlgoSpotNewOrderTwapV1Resp from a dict
create_algo_spot_new_order_twap_v1_resp_from_dict = CreateAlgoSpotNewOrderTwapV1Resp.from_dict(create_algo_spot_new_order_twap_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


