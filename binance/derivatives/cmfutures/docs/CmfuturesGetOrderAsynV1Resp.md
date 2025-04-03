# CmfuturesGetOrderAsynV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_cost_timestamp_of_last30d** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_order_asyn_v1_resp import CmfuturesGetOrderAsynV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetOrderAsynV1Resp from a JSON string
cmfutures_get_order_asyn_v1_resp_instance = CmfuturesGetOrderAsynV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetOrderAsynV1Resp.to_json())

# convert the object into a dict
cmfutures_get_order_asyn_v1_resp_dict = cmfutures_get_order_asyn_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetOrderAsynV1Resp from a dict
cmfutures_get_order_asyn_v1_resp_from_dict = CmfuturesGetOrderAsynV1Resp.from_dict(cmfutures_get_order_asyn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


