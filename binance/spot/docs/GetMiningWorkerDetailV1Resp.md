# GetMiningWorkerDetailV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**List[GetMiningWorkerDetailV1RespDataInner]**](GetMiningWorkerDetailV1RespDataInner.md) |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_worker_detail_v1_resp import GetMiningWorkerDetailV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningWorkerDetailV1Resp from a JSON string
get_mining_worker_detail_v1_resp_instance = GetMiningWorkerDetailV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMiningWorkerDetailV1Resp.to_json())

# convert the object into a dict
get_mining_worker_detail_v1_resp_dict = get_mining_worker_detail_v1_resp_instance.to_dict()
# create an instance of GetMiningWorkerDetailV1Resp from a dict
get_mining_worker_detail_v1_resp_from_dict = GetMiningWorkerDetailV1Resp.from_dict(get_mining_worker_detail_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


