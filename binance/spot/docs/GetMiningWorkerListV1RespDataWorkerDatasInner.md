# GetMiningWorkerListV1RespDataWorkerDatasInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_hash_rate** | **int** |  | [optional] 
**hash_rate** | **int** |  | [optional] 
**last_share_time** | **int** |  | [optional] 
**reject_rate** | **int** |  | [optional] 
**status** | **int** |  | [optional] 
**worker_id** | **str** |  | [optional] 
**worker_name** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_worker_list_v1_resp_data_worker_datas_inner import GetMiningWorkerListV1RespDataWorkerDatasInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningWorkerListV1RespDataWorkerDatasInner from a JSON string
get_mining_worker_list_v1_resp_data_worker_datas_inner_instance = GetMiningWorkerListV1RespDataWorkerDatasInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningWorkerListV1RespDataWorkerDatasInner.to_json())

# convert the object into a dict
get_mining_worker_list_v1_resp_data_worker_datas_inner_dict = get_mining_worker_list_v1_resp_data_worker_datas_inner_instance.to_dict()
# create an instance of GetMiningWorkerListV1RespDataWorkerDatasInner from a dict
get_mining_worker_list_v1_resp_data_worker_datas_inner_from_dict = GetMiningWorkerListV1RespDataWorkerDatasInner.from_dict(get_mining_worker_list_v1_resp_data_worker_datas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


