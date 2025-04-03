# OptionsGetUserTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**liquidity** | **str** |  | [optional] 
**option_side** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**price_scale** | **int** |  | [optional] 
**quantity** | **str** |  | [optional] 
**quantity_scale** | **int** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**realized_profit** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**trade_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**volatility** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_user_trades_v1_resp_item import OptionsGetUserTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetUserTradesV1RespItem from a JSON string
options_get_user_trades_v1_resp_item_instance = OptionsGetUserTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetUserTradesV1RespItem.to_json())

# convert the object into a dict
options_get_user_trades_v1_resp_item_dict = options_get_user_trades_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetUserTradesV1RespItem from a dict
options_get_user_trades_v1_resp_item_from_dict = OptionsGetUserTradesV1RespItem.from_dict(options_get_user_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


