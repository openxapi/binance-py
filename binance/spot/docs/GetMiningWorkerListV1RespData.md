# GetMiningWorkerListV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**total_num** | **int** |  | [optional] 
**worker_datas** | [**List[GetMiningWorkerListV1RespDataWorkerDatasInner]**](GetMiningWorkerListV1RespDataWorkerDatasInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_worker_list_v1_resp_data import GetMiningWorkerListV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningWorkerListV1RespData from a JSON string
get_mining_worker_list_v1_resp_data_instance = GetMiningWorkerListV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetMiningWorkerListV1RespData.to_json())

# convert the object into a dict
get_mining_worker_list_v1_resp_data_dict = get_mining_worker_list_v1_resp_data_instance.to_dict()
# create an instance of GetMiningWorkerListV1RespData from a dict
get_mining_worker_list_v1_resp_data_from_dict = GetMiningWorkerListV1RespData.from_dict(get_mining_worker_list_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


