# GetAccountV1RespGreekInner


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
from binance.options.models.get_account_v1_resp_greek_inner import GetAccountV1RespGreekInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV1RespGreekInner from a JSON string
get_account_v1_resp_greek_inner_instance = GetAccountV1RespGreekInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountV1RespGreekInner.to_json())

# convert the object into a dict
get_account_v1_resp_greek_inner_dict = get_account_v1_resp_greek_inner_instance.to_dict()
# create an instance of GetAccountV1RespGreekInner from a dict
get_account_v1_resp_greek_inner_from_dict = GetAccountV1RespGreekInner.from_dict(get_account_v1_resp_greek_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


