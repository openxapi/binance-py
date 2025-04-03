# OptionsGetIndexV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_price** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_index_v1_resp import OptionsGetIndexV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetIndexV1Resp from a JSON string
options_get_index_v1_resp_instance = OptionsGetIndexV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetIndexV1Resp.to_json())

# convert the object into a dict
options_get_index_v1_resp_dict = options_get_index_v1_resp_instance.to_dict()
# create an instance of OptionsGetIndexV1Resp from a dict
options_get_index_v1_resp_from_dict = OptionsGetIndexV1Resp.from_dict(options_get_index_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


