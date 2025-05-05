# GetOpenInterestV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum_open_interest** | **str** |  | [optional] 
**sum_open_interest_usd** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_open_interest_v1_resp_item import GetOpenInterestV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenInterestV1RespItem from a JSON string
get_open_interest_v1_resp_item_instance = GetOpenInterestV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetOpenInterestV1RespItem.to_json())

# convert the object into a dict
get_open_interest_v1_resp_item_dict = get_open_interest_v1_resp_item_instance.to_dict()
# create an instance of GetOpenInterestV1RespItem from a dict
get_open_interest_v1_resp_item_from_dict = GetOpenInterestV1RespItem.from_dict(get_open_interest_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


