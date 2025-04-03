# OptionsGetTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**side** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_trades_v1_resp_item import OptionsGetTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetTradesV1RespItem from a JSON string
options_get_trades_v1_resp_item_instance = OptionsGetTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetTradesV1RespItem.to_json())

# convert the object into a dict
options_get_trades_v1_resp_item_dict = options_get_trades_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetTradesV1RespItem from a dict
options_get_trades_v1_resp_item_from_dict = OptionsGetTradesV1RespItem.from_dict(options_get_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


