# GetMiningPubAlgoListV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_id** | **int** |  | [optional] 
**algo_name** | **str** |  | [optional] 
**pool_index** | **int** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_pub_algo_list_v1_resp_data_inner import GetMiningPubAlgoListV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPubAlgoListV1RespDataInner from a JSON string
get_mining_pub_algo_list_v1_resp_data_inner_instance = GetMiningPubAlgoListV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningPubAlgoListV1RespDataInner.to_json())

# convert the object into a dict
get_mining_pub_algo_list_v1_resp_data_inner_dict = get_mining_pub_algo_list_v1_resp_data_inner_instance.to_dict()
# create an instance of GetMiningPubAlgoListV1RespDataInner from a dict
get_mining_pub_algo_list_v1_resp_data_inner_from_dict = GetMiningPubAlgoListV1RespDataInner.from_dict(get_mining_pub_algo_list_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


