# GetMiningHashTransferConfigDetailsListV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_details** | [**List[GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner]**](GetMiningHashTransferConfigDetailsListV1RespDataConfigDetailsInner.md) |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_num** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_hash_transfer_config_details_list_v1_resp_data import GetMiningHashTransferConfigDetailsListV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningHashTransferConfigDetailsListV1RespData from a JSON string
get_mining_hash_transfer_config_details_list_v1_resp_data_instance = GetMiningHashTransferConfigDetailsListV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetMiningHashTransferConfigDetailsListV1RespData.to_json())

# convert the object into a dict
get_mining_hash_transfer_config_details_list_v1_resp_data_dict = get_mining_hash_transfer_config_details_list_v1_resp_data_instance.to_dict()
# create an instance of GetMiningHashTransferConfigDetailsListV1RespData from a dict
get_mining_hash_transfer_config_details_list_v1_resp_data_from_dict = GetMiningHashTransferConfigDetailsListV1RespData.from_dict(get_mining_hash_transfer_config_details_list_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


