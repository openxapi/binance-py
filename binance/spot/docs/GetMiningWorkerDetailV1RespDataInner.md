# GetMiningWorkerDetailV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashrate_datas** | [**List[GetMiningWorkerDetailV1RespDataInnerHashrateDatasInner]**](GetMiningWorkerDetailV1RespDataInnerHashrateDatasInner.md) |  | [optional] 
**type** | **str** |  | [optional] 
**worker_name** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_worker_detail_v1_resp_data_inner import GetMiningWorkerDetailV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningWorkerDetailV1RespDataInner from a JSON string
get_mining_worker_detail_v1_resp_data_inner_instance = GetMiningWorkerDetailV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningWorkerDetailV1RespDataInner.to_json())

# convert the object into a dict
get_mining_worker_detail_v1_resp_data_inner_dict = get_mining_worker_detail_v1_resp_data_inner_instance.to_dict()
# create an instance of GetMiningWorkerDetailV1RespDataInner from a dict
get_mining_worker_detail_v1_resp_data_inner_from_dict = GetMiningWorkerDetailV1RespDataInner.from_dict(get_mining_worker_detail_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


