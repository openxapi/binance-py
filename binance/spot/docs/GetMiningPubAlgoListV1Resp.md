# GetMiningPubAlgoListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**List[GetMiningPubAlgoListV1RespDataInner]**](GetMiningPubAlgoListV1RespDataInner.md) |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_pub_algo_list_v1_resp import GetMiningPubAlgoListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPubAlgoListV1Resp from a JSON string
get_mining_pub_algo_list_v1_resp_instance = GetMiningPubAlgoListV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMiningPubAlgoListV1Resp.to_json())

# convert the object into a dict
get_mining_pub_algo_list_v1_resp_dict = get_mining_pub_algo_list_v1_resp_instance.to_dict()
# create an instance of GetMiningPubAlgoListV1Resp from a dict
get_mining_pub_algo_list_v1_resp_from_dict = GetMiningPubAlgoListV1Resp.from_dict(get_mining_pub_algo_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


