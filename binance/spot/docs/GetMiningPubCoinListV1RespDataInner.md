# GetMiningPubCoinListV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_id** | **int** |  | [optional] 
**algo_name** | **str** |  | [optional] 
**coin_id** | **int** |  | [optional] 
**coin_name** | **str** |  | [optional] 
**pool_index** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_pub_coin_list_v1_resp_data_inner import GetMiningPubCoinListV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPubCoinListV1RespDataInner from a JSON string
get_mining_pub_coin_list_v1_resp_data_inner_instance = GetMiningPubCoinListV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningPubCoinListV1RespDataInner.to_json())

# convert the object into a dict
get_mining_pub_coin_list_v1_resp_data_inner_dict = get_mining_pub_coin_list_v1_resp_data_inner_instance.to_dict()
# create an instance of GetMiningPubCoinListV1RespDataInner from a dict
get_mining_pub_coin_list_v1_resp_data_inner_from_dict = GetMiningPubCoinListV1RespDataInner.from_dict(get_mining_pub_coin_list_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


