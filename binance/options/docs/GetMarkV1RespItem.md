# GetMarkV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_iv** | **str** |  | [optional] 
**bid_iv** | **str** |  | [optional] 
**delta** | **str** |  | [optional] 
**gamma** | **str** |  | [optional] 
**high_price_limit** | **str** |  | [optional] 
**low_price_limit** | **str** |  | [optional] 
**mark_iv** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**risk_free_interest** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**theta** | **str** |  | [optional] 
**vega** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_mark_v1_resp_item import GetMarkV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarkV1RespItem from a JSON string
get_mark_v1_resp_item_instance = GetMarkV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarkV1RespItem.to_json())

# convert the object into a dict
get_mark_v1_resp_item_dict = get_mark_v1_resp_item_instance.to_dict()
# create an instance of GetMarkV1RespItem from a dict
get_mark_v1_resp_item_from_dict = GetMarkV1RespItem.from_dict(get_mark_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


