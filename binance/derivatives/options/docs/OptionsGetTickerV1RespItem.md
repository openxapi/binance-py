# OptionsGetTickerV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**ask_price** | **str** |  | [optional] 
**bid_price** | **str** |  | [optional] 
**close_time** | **int** |  | [optional] 
**exercise_price** | **str** |  | [optional] 
**first_trade_id** | **int** |  | [optional] 
**high** | **str** |  | [optional] 
**last_price** | **str** |  | [optional] 
**last_qty** | **str** |  | [optional] 
**low** | **str** |  | [optional] 
**open** | **str** |  | [optional] 
**open_time** | **int** |  | [optional] 
**price_change** | **str** |  | [optional] 
**price_change_percent** | **str** |  | [optional] 
**strike_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**trade_count** | **int** |  | [optional] 
**volume** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_ticker_v1_resp_item import OptionsGetTickerV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetTickerV1RespItem from a JSON string
options_get_ticker_v1_resp_item_instance = OptionsGetTickerV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetTickerV1RespItem.to_json())

# convert the object into a dict
options_get_ticker_v1_resp_item_dict = options_get_ticker_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetTickerV1RespItem from a dict
options_get_ticker_v1_resp_item_from_dict = OptionsGetTickerV1RespItem.from_dict(options_get_ticker_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


