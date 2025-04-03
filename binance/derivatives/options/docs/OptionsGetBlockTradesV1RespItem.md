# OptionsGetBlockTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**side** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**trade_id** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_block_trades_v1_resp_item import OptionsGetBlockTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetBlockTradesV1RespItem from a JSON string
options_get_block_trades_v1_resp_item_instance = OptionsGetBlockTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetBlockTradesV1RespItem.to_json())

# convert the object into a dict
options_get_block_trades_v1_resp_item_dict = options_get_block_trades_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetBlockTradesV1RespItem from a dict
options_get_block_trades_v1_resp_item_from_dict = OptionsGetBlockTradesV1RespItem.from_dict(options_get_block_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


