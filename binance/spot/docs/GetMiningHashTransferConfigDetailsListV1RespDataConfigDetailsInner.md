# GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_name** | **str** |  | [optional] 
**config_id** | **int** |  | [optional] 
**end_day** | **int** |  | [optional] 
**hash_rate** | **int** |  | [optional] 
**pool_username** | **str** |  | [optional] 
**start_day** | **int** |  | [optional] 
**status** | **int** |  | [optional] 
**to_pool_username** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_hash_transfer_config_details_list_v1_resp_data_config_details_inner import GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner from a JSON string
get_mining_hash_transfer_config_details_list_v1_resp_data_config_details_inner_instance = GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner.to_json())

# convert the object into a dict
get_mining_hash_transfer_config_details_list_v1_resp_data_config_details_inner_dict = get_mining_hash_transfer_config_details_list_v1_resp_data_config_details_inner_instance.to_dict()
# create an instance of GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner from a dict
get_mining_hash_transfer_config_details_list_v1_resp_data_config_details_inner_from_dict = GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner.from_dict(get_mining_hash_transfer_config_details_list_v1_resp_data_config_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


