# GetIndexV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_price** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.options.models.get_index_v1_resp import GetIndexV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndexV1Resp from a JSON string
get_index_v1_resp_instance = GetIndexV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetIndexV1Resp.to_json())

# convert the object into a dict
get_index_v1_resp_dict = get_index_v1_resp_instance.to_dict()
# create an instance of GetIndexV1Resp from a dict
get_index_v1_resp_from_dict = GetIndexV1Resp.from_dict(get_index_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


