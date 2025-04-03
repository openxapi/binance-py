# OptionsGetOpenInterestV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum_open_interest** | **str** |  | [optional] 
**sum_open_interest_usd** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_open_interest_v1_resp_item import OptionsGetOpenInterestV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetOpenInterestV1RespItem from a JSON string
options_get_open_interest_v1_resp_item_instance = OptionsGetOpenInterestV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetOpenInterestV1RespItem.to_json())

# convert the object into a dict
options_get_open_interest_v1_resp_item_dict = options_get_open_interest_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetOpenInterestV1RespItem from a dict
options_get_open_interest_v1_resp_item_from_dict = OptionsGetOpenInterestV1RespItem.from_dict(options_get_open_interest_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


