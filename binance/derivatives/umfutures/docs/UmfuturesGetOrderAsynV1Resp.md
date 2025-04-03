# UmfuturesGetOrderAsynV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_cost_timestamp_of_last30d** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_order_asyn_v1_resp import UmfuturesGetOrderAsynV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetOrderAsynV1Resp from a JSON string
umfutures_get_order_asyn_v1_resp_instance = UmfuturesGetOrderAsynV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetOrderAsynV1Resp.to_json())

# convert the object into a dict
umfutures_get_order_asyn_v1_resp_dict = umfutures_get_order_asyn_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetOrderAsynV1Resp from a dict
umfutures_get_order_asyn_v1_resp_from_dict = UmfuturesGetOrderAsynV1Resp.from_dict(umfutures_get_order_asyn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


