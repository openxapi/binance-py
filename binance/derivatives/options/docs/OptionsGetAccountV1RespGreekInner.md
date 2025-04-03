# OptionsGetAccountV1RespGreekInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta** | **str** |  | [optional] 
**gamma** | **str** |  | [optional] 
**theta** | **str** |  | [optional] 
**underlying** | **str** |  | [optional] 
**vega** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_account_v1_resp_greek_inner import OptionsGetAccountV1RespGreekInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetAccountV1RespGreekInner from a JSON string
options_get_account_v1_resp_greek_inner_instance = OptionsGetAccountV1RespGreekInner.from_json(json)
# print the JSON string representation of the object
print(OptionsGetAccountV1RespGreekInner.to_json())

# convert the object into a dict
options_get_account_v1_resp_greek_inner_dict = options_get_account_v1_resp_greek_inner_instance.to_dict()
# create an instance of OptionsGetAccountV1RespGreekInner from a dict
options_get_account_v1_resp_greek_inner_from_dict = OptionsGetAccountV1RespGreekInner.from_dict(options_get_account_v1_resp_greek_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


