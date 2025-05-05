# DeleteAlgoSpotOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_id** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.delete_algo_spot_order_v1_resp import DeleteAlgoSpotOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAlgoSpotOrderV1Resp from a JSON string
delete_algo_spot_order_v1_resp_instance = DeleteAlgoSpotOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteAlgoSpotOrderV1Resp.to_json())

# convert the object into a dict
delete_algo_spot_order_v1_resp_dict = delete_algo_spot_order_v1_resp_instance.to_dict()
# create an instance of DeleteAlgoSpotOrderV1Resp from a dict
delete_algo_spot_order_v1_resp_from_dict = DeleteAlgoSpotOrderV1Resp.from_dict(delete_algo_spot_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


