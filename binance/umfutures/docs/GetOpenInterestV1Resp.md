# GetOpenInterestV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_interest** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_open_interest_v1_resp import GetOpenInterestV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenInterestV1Resp from a JSON string
get_open_interest_v1_resp_instance = GetOpenInterestV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetOpenInterestV1Resp.to_json())

# convert the object into a dict
get_open_interest_v1_resp_dict = get_open_interest_v1_resp_instance.to_dict()
# create an instance of GetOpenInterestV1Resp from a dict
get_open_interest_v1_resp_from_dict = GetOpenInterestV1Resp.from_dict(get_open_interest_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


